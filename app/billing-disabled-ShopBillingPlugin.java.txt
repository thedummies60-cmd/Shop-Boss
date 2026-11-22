package com.shopboss.game;

import com.android.billingclient.api.AcknowledgePurchaseParams;
import com.android.billingclient.api.BillingClient;
import com.android.billingclient.api.BillingClientStateListener;
import com.android.billingclient.api.BillingFlowParams;
import com.android.billingclient.api.BillingResult;
import com.android.billingclient.api.ConsumeParams;
import com.android.billingclient.api.PendingPurchasesParams;
import com.android.billingclient.api.ProductDetails;
import com.android.billingclient.api.Purchase;
import com.android.billingclient.api.PurchasesUpdatedListener;
import com.android.billingclient.api.QueryProductDetailsParams;
import com.android.billingclient.api.QueryPurchasesParams;
import com.getcapacitor.JSArray;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Small bridge between the game and Google Play Billing (one-time products only).
 *
 * The game decides what a product gives. It calls finish() only after it has saved the reward,
 * so a purchase is never lost: until it is consumed or acknowledged, owned() keeps returning it.
 */
@CapacitorPlugin(name = "ShopBilling")
public class ShopBillingPlugin extends Plugin implements PurchasesUpdatedListener {

    private BillingClient client;
    private final Map<String, ProductDetails> details = new HashMap<>();
    private PluginCall pendingBuy;
    private final List<Runnable> waiting = new ArrayList<>();
    private boolean connecting;

    @Override
    public void load() {
        client = BillingClient.newBuilder(getContext())
            .setListener(this)
            .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
            .enableAutoServiceReconnection()
            .build();
    }

    /** Runs the task once the connection to Google Play is ready, or fails the call. */
    private void ready(PluginCall call, Runnable task) {
        if (client.isReady()) { task.run(); return; }
        synchronized (waiting) {
            waiting.add(task);
            if (connecting) return;
            connecting = true;
        }
        client.startConnection(new BillingClientStateListener() {
            @Override
            public void onBillingSetupFinished(BillingResult result) {
                List<Runnable> run;
                synchronized (waiting) { run = new ArrayList<>(waiting); waiting.clear(); connecting = false; }
                if (result.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                    for (Runnable r : run) r.run();
                } else if (call != null) {
                    call.reject("Google Play is not available (" + result.getResponseCode() + ")");
                }
            }

            @Override
            public void onBillingServiceDisconnected() {
                synchronized (waiting) { connecting = false; }
            }
        });
    }

    @PluginMethod
    public void getProducts(PluginCall call) {
        JSArray ids = call.getArray("ids");
        List<QueryProductDetailsParams.Product> list = new ArrayList<>();
        try {
            for (Object id : ids.toList()) {
                list.add(QueryProductDetailsParams.Product.newBuilder()
                    .setProductId(String.valueOf(id))
                    .setProductType(BillingClient.ProductType.INAPP).build());
            }
        } catch (Exception e) {
            call.reject("ids missing");
            return;
        }
        ready(call, () -> client.queryProductDetailsAsync(
            QueryProductDetailsParams.newBuilder().setProductList(list).build(),
            (result, res) -> {
                if (result.getResponseCode() != BillingClient.BillingResponseCode.OK) {
                    call.reject("products failed (" + result.getResponseCode() + ")");
                    return;
                }
                JSArray out = new JSArray();
                for (ProductDetails d : res.getProductDetailsList()) {
                    details.put(d.getProductId(), d);
                    ProductDetails.OneTimePurchaseOfferDetails o = d.getOneTimePurchaseOfferDetails();
                    JSObject p = new JSObject();
                    p.put("id", d.getProductId());
                    p.put("title", d.getName());
                    p.put("price", o != null ? o.getFormattedPrice() : "");
                    out.put(p);
                }
                JSObject r = new JSObject();
                r.put("products", out);
                call.resolve(r);
            }));
    }

    @PluginMethod
    public void buy(PluginCall call) {
        String id = call.getString("id", "");
        ProductDetails d = details.get(id);
        if (d == null) { call.reject("unknown product " + id); return; }
        if (pendingBuy != null) { call.reject("busy"); return; }
        ready(call, () -> getActivity().runOnUiThread(() -> {
            List<BillingFlowParams.ProductDetailsParams> p = new ArrayList<>();
            p.add(BillingFlowParams.ProductDetailsParams.newBuilder().setProductDetails(d).build());
            pendingBuy = call;
            BillingResult r = client.launchBillingFlow(getActivity(),
                BillingFlowParams.newBuilder().setProductDetailsParamsList(p).build());
            if (r.getResponseCode() != BillingClient.BillingResponseCode.OK) {
                pendingBuy = null;
                call.resolve(status(r.getResponseCode() == BillingClient.BillingResponseCode.ITEM_ALREADY_OWNED ? "owned" : "error", null));
            }
        }));
    }

    @Override
    public void onPurchasesUpdated(BillingResult result, List<Purchase> purchases) {
        int code = result.getResponseCode();
        String s = code == BillingClient.BillingResponseCode.OK ? "ok"
            : code == BillingClient.BillingResponseCode.USER_CANCELED ? "cancel"
            : code == BillingClient.BillingResponseCode.ITEM_ALREADY_OWNED ? "owned" : "error";
        JSObject r = status(s, purchases);
        PluginCall c = pendingBuy;
        pendingBuy = null;
        if (c != null) c.resolve(r);
        else if (purchases != null) notifyListeners("purchases", r);
    }

    @PluginMethod
    public void owned(PluginCall call) {
        ready(call, () -> client.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder().setProductType(BillingClient.ProductType.INAPP).build(),
            (result, list) -> {
                if (result.getResponseCode() != BillingClient.BillingResponseCode.OK) {
                    call.reject("purchases failed (" + result.getResponseCode() + ")");
                    return;
                }
                call.resolve(status("ok", list));
            }));
    }

    /** Consumes (cash packs, can be bought again) or acknowledges (packs you keep) a rewarded purchase. */
    @PluginMethod
    public void finish(PluginCall call) {
        String token = call.getString("token", "");
        boolean consume = Boolean.TRUE.equals(call.getBoolean("consumable", false));
        if (token.isEmpty()) { call.reject("token missing"); return; }
        ready(call, () -> {
            if (consume) {
                client.consumeAsync(ConsumeParams.newBuilder().setPurchaseToken(token).build(),
                    (result, t) -> done(call, result));
            } else {
                client.acknowledgePurchase(AcknowledgePurchaseParams.newBuilder().setPurchaseToken(token).build(),
                    result -> done(call, result));
            }
        });
    }

    private void done(PluginCall call, BillingResult result) {
        JSObject r = new JSObject();
        r.put("ok", result.getResponseCode() == BillingClient.BillingResponseCode.OK);
        call.resolve(r);
    }

    private JSObject status(String s, List<Purchase> purchases) {
        JSArray list = new JSArray();
        if (purchases != null) {
            for (Purchase p : purchases) {
                JSObject o = new JSObject();
                o.put("products", new JSArray(p.getProducts()));
                o.put("token", p.getPurchaseToken());
                o.put("state", p.getPurchaseState() == Purchase.PurchaseState.PURCHASED ? "purchased"
                    : p.getPurchaseState() == Purchase.PurchaseState.PENDING ? "pending" : "unknown");
                o.put("acknowledged", p.isAcknowledged());
                list.put(o);
            }
        }
        JSObject r = new JSObject();
        r.put("status", s);
        r.put("purchases", list);
        return r;
    }
}
