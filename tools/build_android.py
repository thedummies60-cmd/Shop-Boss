#!/usr/bin/env python3
"""Build the Shop Boss Android app (APK and Play Store AAB) from the web game, with Gradle.

From version 2.0 the app is a full Capacitor project in app/ (it contains the Google Play
Billing plugin for the Shop), so it is built with Gradle instead of patching the old APK.

Needs: Node + npm, JDK 21, the Android SDK (platform 36) and the release keystore.

Usage:
  export ANDROID_HOME=/path/to/android-sdk
  export SHOPBOSS_KEYSTORE=/path/to/shop-boss-release.jks SHOPBOSS_KS_PASS=...
  python3 tools/build_android.py --version 2.0 --code 24

Writes Shop-Boss-<version>.apk (install on a phone) and playstore/Shop-Boss-<version>.aab
(upload to Play Console). Every new version needs a higher --code.
"""
import argparse, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from build_apk import apk_page  # same page as the old APK build: local three.js and fonts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', required=True)
    ap.add_argument('--code', type=int, required=True)
    ap.add_argument('--html', default=os.path.join(ROOT, 'Shop Boss(1).html'))
    a = ap.parse_args()
    for k in ('ANDROID_HOME', 'SHOPBOSS_KEYSTORE', 'SHOPBOSS_KS_PASS'):
        if not os.environ.get(k):
            sys.exit(f'set {k}')
    app = os.path.join(ROOT, 'app')
    www = os.path.join(app, 'www')
    with open(a.html, encoding='utf-8') as f:
        page = apk_page(f.read())
    with open(os.path.join(www, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    if not os.path.isdir(os.path.join(app, 'node_modules')):
        subprocess.run(['npm', 'ci', '--no-audit', '--no-fund'], cwd=app, check=True)
    # Capacitor's JavaScript runtime (registerPlugin), loaded by the page as capacitor.js
    shutil.copy(os.path.join(app, 'node_modules', '@capacitor', 'core', 'dist', 'capacitor.js'), os.path.join(www, 'capacitor.js'))
    sw = os.path.join(www, 'sw.js')
    with open(sw, encoding='utf-8') as f:
        s = f.read()
    with open(sw, 'w', encoding='utf-8') as f:
        f.write(re.sub(r"const CACHE = 'shop-boss-v[0-9.]+';", f"const CACHE = 'shop-boss-v{a.code}';", s))
    gradle = os.path.join(app, 'android', 'app', 'build.gradle')
    with open(gradle, encoding='utf-8') as f:
        g = f.read()
    g = re.sub(r'versionCode \d+', f'versionCode {a.code}', g)
    g = re.sub(r'versionName "[^"]*"', f'versionName "{a.version}"', g)
    with open(gradle, 'w', encoding='utf-8') as f:
        f.write(g)
    subprocess.run(['npx', 'cap', 'sync', 'android'], cwd=app, check=True)
    andr = os.path.join(app, 'android')
    with open(os.path.join(andr, 'local.properties'), 'w') as f:
        f.write(f"sdk.dir={os.environ['ANDROID_HOME']}\n")
    subprocess.run(['./gradlew', '--no-daemon', '-q', 'assembleRelease', 'bundleRelease'], cwd=andr, check=True)
    out = os.path.join(andr, 'app', 'build', 'outputs')
    apk = os.path.join(ROOT, f'Shop-Boss-{a.version}.apk')
    aab = os.path.join(ROOT, 'playstore', f'Shop-Boss-{a.version}.aab')
    shutil.copy(os.path.join(out, 'apk', 'release', 'app-release.apk'), apk)
    shutil.copy(os.path.join(out, 'bundle', 'release', 'app-release.aab'), aab)
    shutil.copy(apk, os.path.join(ROOT, 'Shop-Boss.apk'))
    print('built', apk, 'and', aab)


if __name__ == '__main__':
    main()
