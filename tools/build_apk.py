#!/usr/bin/env python3
"""Build a new Shop Boss APK from the web game.

The game is one HTML file ("Shop Boss(1).html"). The APK is a Capacitor app whose
game page lives at assets/public/index.html. This script takes the previous APK,
swaps in the new game page (with local three.js and fonts instead of the CDN),
bumps the version in AndroidManifest.xml, then aligns and signs the result.

Usage:
  SHOPBOSS_KS_PASS=... python3 tools/build_apk.py \
      --base Shop-Boss.apk --html "Shop Boss(1).html" \
      --version 1.9 --code 10 --out Shop-Boss-1.9.apk \
      --build-tools /path/to/android/build-tools --keystore shop-boss.jks --alias shopboss

Android only installs an update over an installed app when both are signed with
the same key, so keep the keystore safe and use the same one every time.
"""
import argparse, os, re, subprocess, sys, tempfile, zipfile

CDN_THREE = 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js'

APK_HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<meta name="theme-color" content="#86d35f">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="description" content="Grow your own shop in 12 colorful worlds.">
<title>Shop Boss</title>
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-512.png">
<script src="capacitor.js"></script>
<style>
@font-face{font-family:"Baloo 2";font-style:normal;font-weight:600;font-display:swap;src:url(fonts/baloo-2-latin-600-normal.woff2) format("woff2")}
@font-face{font-family:"Baloo 2";font-style:normal;font-weight:700;font-display:swap;src:url(fonts/baloo-2-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Baloo 2";font-style:normal;font-weight:800;font-display:swap;src:url(fonts/baloo-2-latin-800-normal.woff2) format("woff2")}
[hidden]{display:none!important}
html,body{margin:0}
</style>
</head>
<body>
'''
APK_TAIL = '''
<script>if ('serviceWorker' in navigator && location.protocol === 'https:' && !(window.Capacitor && Capacitor.isNativePlatform && Capacitor.isNativePlatform())) navigator.serviceWorker.register('sw.js').catch(() => {});</script>
</body>
</html>
'''


def apk_page(web):
    """The game part of the web page (its styles, markup and scripts), wrapped in the APK's own head."""
    start = web.index('<style>\n/* Layout:')
    end = web.rindex('</body></html>')
    body = web[start:end].rstrip() + '\n'
    if body.count(CDN_THREE) != 1:
        sys.exit('three.js import not found exactly once')
    body = body.replace(CDN_THREE, './lib/three/build/three.module.js')
    if 'fonts.googleapis.com' in body or 'cdn.jsdelivr.net' in body:
        sys.exit('page still loads something from the internet')
    return APK_HEAD + body + APK_TAIL


def patch_manifest(axml, old_code, new_code, old_name, new_name):
    """Change versionCode/versionName in the binary AndroidManifest.xml in place."""
    def typed_int(v):  # attribute rawValue=-1, Res_value{size=8, res0=0, type=INT_DEC(0x10), data=v}
        return b'\xff\xff\xff\xff\x08\x00\x00\x10' + v.to_bytes(4, 'little')
    if len(old_name) != len(new_name):
        sys.exit('versionName must keep the same length (e.g. 1.8 -> 1.9)')
    for a, b in ((typed_int(old_code), typed_int(new_code)), (old_name.encode('utf-16-le'), new_name.encode('utf-16-le'))):
        if axml.count(a) != 1:
            sys.exit(f'manifest: expected one match for {a!r}, found {axml.count(a)}')
        axml = axml.replace(a, b)
    return axml


def badging(tools, apk):
    out = subprocess.run([os.path.join(tools, 'aapt2'), 'dump', 'badging', apk], capture_output=True, text=True).stdout
    return dict(re.findall(r"(versionCode|versionName)='([^']*)'", out.splitlines()[0]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', required=True); ap.add_argument('--html', required=True)
    ap.add_argument('--version', required=True); ap.add_argument('--code', type=int, required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--build-tools', required=True)
    ap.add_argument('--keystore', required=True); ap.add_argument('--alias', required=True)
    a = ap.parse_args()
    if not os.environ.get('SHOPBOSS_KS_PASS'):
        sys.exit('set SHOPBOSS_KS_PASS to the keystore password')
    old = badging(a.build_tools, a.base)
    page = apk_page(open(a.html, encoding='utf-8').read())
    with tempfile.TemporaryDirectory() as tmp:
        raw, aligned = os.path.join(tmp, 'raw.apk'), os.path.join(tmp, 'aligned.apk')
        with zipfile.ZipFile(a.base) as zin, zipfile.ZipFile(raw, 'w') as zout:
            for info in zin.infolist():
                data = zin.read(info.filename)
                if info.filename == 'assets/public/index.html':
                    data = page.encode('utf-8')
                elif info.filename == 'assets/public/sw.js':
                    data = re.sub(rb"const CACHE = 'shop-boss-v[0-9.]+';", f"const CACHE = 'shop-boss-v{a.code}';".encode(), data)
                elif info.filename == 'AndroidManifest.xml':
                    data = patch_manifest(data, int(old['versionCode']), a.code, old['versionName'], a.version)
                zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                zi.compress_type, zi.external_attr, zi.create_system = info.compress_type, info.external_attr, info.create_system
                zout.writestr(zi, data)
        subprocess.run([os.path.join(a.build_tools, 'zipalign'), '-p', '-f', '4', raw, aligned], check=True)
        subprocess.run([os.path.join(a.build_tools, 'apksigner'), 'sign', '--ks', a.keystore, '--ks-key-alias', a.alias,
                        '--ks-pass', 'env:SHOPBOSS_KS_PASS', '--key-pass', 'env:SHOPBOSS_KS_PASS', '--v4-signing-enabled', 'false', '--out', a.out, aligned], check=True)
    subprocess.run([os.path.join(a.build_tools, 'apksigner'), 'verify', '--print-certs', a.out], check=True)
    print('built', a.out, badging(a.build_tools, a.out))


if __name__ == '__main__':
    main()
