# Shop-Boss
A mobile game for Android. Download the APK, skip the warnings and install the app.

**Newest version: 1.9** → download `Shop-Boss-1.9.apk` (the same file as `Shop-Boss.apk`).
On iPhone, play the web version (`Shop Boss(1).html`).

## What's new in 1.9
- **4 new worlds, 12 in total:** Jungle Camp, Volcano Island, Cloud Kingdom and Coral Reef.
  Each one has its own products, machines and decorations. Moon Base now has a portal to Jungle Camp.
- **iPhone:** the green bar at the top of the screen is gone. The top of the screen now takes the colour
  of the world you are in, and the game fills the whole screen.
- **No zooming:** pinching, double-tapping and Ctrl + scroll no longer zoom the game.
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
**Nieuw in 1.9:** 4 nieuwe werelden (Junglekamp, Vulkaaneiland, Wolkenrijk, Koraalrif), geen groene
balk meer bovenaan op iPhone, je kunt niet meer inzoomen, en je voortgang wordt altijd vanzelf bewaard.

**Installeren op Android:** verwijder eerst Shop Boss 1.8 en installeer daarna 1.9 (nieuwe
ondertekeningssleutel). Vanaf 1.9 installeert elke nieuwe versie gewoon over de oude heen en blijft je
voortgang vanzelf staan.

## Building the APK
`tools/build_apk.py` puts the web game into the previous APK, raises the version number and signs it.
It needs the Android build-tools (`zipalign`, `apksigner`, `aapt2`) and the release keystore.
The keystore is never stored in this repository.
