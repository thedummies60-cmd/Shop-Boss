# Shop-Boss
A mobile game for Android. Download the APK, skip the warnings and install the app.

**Newest version: 2.1** → download `Shop-Boss-2.1.apk` (the same file as `Shop-Boss.apk`).
On iPhone, play the web version (`Shop Boss(1).html`).

## What's new in 2.1
- **Police:** every 5 minutes a police officer checks your shop. If more than 5 customers are angry you get a fine:
  100 in Sunny Beach, 200 in Snow Village, 500 in Big City, and more in every next world (up to 500K in Coral Reef).
  Your money never goes below 0.

## What was new in 2.0
- **Shop (Android app):** buy cash (bag, pile or treasure chest), **Double cash** (every customer pays 2×,
  in every world, forever), all colors, all hats or the **Legendary pack** with real money. Payments go through
  Google Play, so they only work in the app from the Play Store. Bought something before? **Restore purchases**
  gets it back. On iPhone and on claude.ai there is no shop.
- **New menu:** six big buttons (Missions, Skins, Worlds, Daily gift, Shop, Settings) and your boss level at the top.
- **Daily gift:** a gift every day; it grows for 7 days in a row and day 7 is a new skin. Skip a day and you start again.
- **Boss level:** every customer you serve gives XP. Every new level makes your prices 1% higher (up to +50%).
- **Combo:** serve customers in a row without anyone getting angry. Every customer in the combo pays 2% more
  (up to +50%). Let a customer get angry and the combo is gone.
- **Bug fix:** small fixes in the menu layout on short screens.

## Installing 2.0 on Android
2.0 is signed with the same key as 1.9, so it installs over 1.9 and your progress stays.

## What was new in 1.9
- **4 new worlds, 12 in total:** Jungle Camp, Volcano Island, Cloud Kingdom and Coral Reef.
  Each one has its own products, machines and decorations. Moon Base now has a portal to Jungle Camp.
- **iPhone:** the green bar at the top of the screen is gone. The top of the screen now takes the colour
  of the world you are in, and the game fills the whole screen.
- **More variety:** colorful customers (and small kids), golden VIP customers who pay 3×, gift boxes that
  fall from the sky now and then (money, a jackpot or a boost) and missions.
- **Missions live in the menu:** open **Missions** in the main menu to see 3 missions per world, their
  progress and the prize; a red dot on the menu button shows when a prize is ready to claim.
  Missions are big (sell 50-90, serve 45-80, ...), get up to 3x harder the more you finish, include
  "serve customers in a row with nobody angry", and now and then a legendary mission appears.
  You can finish 3 missions a day; new ones come the next day.
- **Legendary skins:** Rainbow, Diamond, Neon, Halo, Unicorn Horn and Fire Crown can only be won with a
  legendary mission. Every skin shows its rarity: Common, Rare, Epic or Legendary (40 to collect).
- **More settings:** effects and music volume, battery saver, shadows, screen shake, joystick size and
  buttons on the left or right.
- **Better menu:** your worlds, skins and missions at a glance, and the world name on the Play button.
- **Skins are won, not bought:** every mission wins a new color or hat (34 to collect, including a party hat,
  chef hat, cowboy hat, top hat, viking helmet and the golden crown). They can no longer be bought with money.
- **No zooming:** pinching, double-tapping and Ctrl + scroll no longer zoom the game.
- **New 3D models:** a real golden crown (with gems and a velvet cap) and a sneaker with a lightning bolt
  for the Fast Shoes and Staff Speed upgrades.
- **Your progress saves by itself, you never have to do anything:**
  - the game saves every few seconds, after every purchase and when you close the app
  - it keeps a second backup copy, in case the first one gets broken
  - when you play on claude.ai, your progress is also stored with your account, so it is still
    there on another phone or after the browser was cleared
- **Bug fixes:** some Dutch texts were missing ("Your shop is waiting", "Travel →", "Graphics", "Mid"),
  and the game now shows a clear message if it cannot load.

## Installing 1.9 on Android (important)
Version 1.9 is signed with a new key, so Android cannot install it over 1.8.
Uninstall Shop Boss 1.8 first, then install 1.9. Progress from 1.8 on that phone cannot be moved over.

From 1.9 on, every new version is signed with the same key, so it installs over the old one and your
progress stays, without doing anything.

## Nederlands
**Nieuw in 2.1:** om de 5 minuten komt de politie kijken. Zijn er meer dan 5 boze klanten, dan krijg je een boete
(100 in Zonnig Strand, 200 in Sneeuwdorp, 500 in Grote Stad, en meer in elke volgende wereld). Je geld gaat nooit onder 0.

**Nieuw in 2.0:** een **Winkel** in de Android-app (geld, Dubbel geld, alle kleuren, alle hoeden en het
Legendarisch pakket, betalen via Google Play), een nieuw menu met zes knoppen, een **dagcadeau** (7 dagen op rij,
dag 7 is een nieuwe skin), een **baaslevel** (elk level +1% prijzen) en **combo's** (klanten op rij helpen zonder
dat iemand boos wordt geeft tot +50%). 2.0 installeert gewoon over 1.9 heen.

**Nieuw in 1.9:** 4 nieuwe werelden (Junglekamp, Vulkaaneiland, Wolkenrijk, Koraalrif), geen groene
balk meer bovenaan op iPhone, je kunt niet meer inzoomen, een nieuwe kroon en snelle schoen, meer
variatie (kleurrijke klanten, VIP-klanten, cadeaudozen uit de lucht en opdrachten). Met opdrachten win
je nieuwe kleuren en hoeden; kopen met geld kan niet meer. Je voortgang wordt altijd vanzelf bewaard.
Alles voor de Play Store staat in de map `playstore/`.

**Installeren op Android:** verwijder eerst Shop Boss 1.8 en installeer daarna 1.9 (nieuwe
ondertekeningssleutel). Vanaf 1.9 installeert elke nieuwe versie gewoon over de oude heen en blijft je
voortgang vanzelf staan.

## Google Play
Everything for the Play Store listing (texts, icon, banner, screenshots and a step-by-step guide)
is in the `playstore/` folder. The privacy policy is `PRIVACY.md`.

## Building the app
From 2.0 the Android app is a Capacitor project in `app/` with a small Google Play Billing plugin
(`app/android/app/src/main/java/com/shopboss/game/ShopBillingPlugin.java`).
`tools/build_android.py --version 2.0 --code 24` puts the web game into it and builds the signed APK and the
Play Store `.aab` with Gradle. It needs Node, JDK 21, the Android SDK (platform 36) and the release keystore
(`SHOPBOSS_KEYSTORE`, `SHOPBOSS_KS_PASS`). The keystore is never stored in this repository.
(`tools/build_apk.py` is the older way, used up to 1.9.)
