# Shop Boss op Google Play zetten

In deze map staat alles wat je nodig hebt voor de winkelpagina in Google Play.

| Bestand | Waarvoor |
|---|---|
| `listing-en.md`, `listing-nl.md` | Naam, korte en lange beschrijving (Engels en Nederlands) |
| `icon-512.png` | App-pictogram, 512 × 512 |
| `feature-graphic-en.jpg`, `feature-graphic-nl.jpg` | Banner bovenaan de winkelpagina, 1024 × 500 |
| `screenshots/en/`, `screenshots/nl/` | 8 schermafbeeldingen per taal, 1080 × 1920 |
| `../PRIVACY.md` | Privacybeleid (Google vraagt een link) |

## 1. Ontwikkelaarsaccount
- Je hebt een Google Play-ontwikkelaarsaccount nodig (eenmalig 25 dollar). De eigenaar moet **18 jaar of ouder** zijn, dus vraag dit eventueel aan een ouder.
- Bij een nieuw persoonlijk account eist Google eerst een **gesloten test**: minstens 12 testers die de app 14 dagen lang geïnstalleerd hebben. Pas daarna mag de app openbaar in de winkel.

## 2. Het app-bestand
Google Play aanvaardt voor nieuwe apps alleen een **Android App Bundle (`.aab`)**, geen `.apk`.
Die moet nog gemaakt worden van `Shop-Boss.apk` met Google's programma *bundletool*. Vraag Claude om de `.aab` te maken.

Gebruik altijd de sleutel `shop-boss-release.jks` (die heb je privé gekregen, nooit op GitHub zetten).

**Ondertekenen door Google (Play App Signing):** bij het aanmaken van de app vraagt Google welke sleutel de app ondertekent.
- Kies je *"Door Google gegenereerde sleutel"* (het makkelijkst), dan kan een app uit de Play Store niet over een app van GitHub heen geïnstalleerd worden (en omgekeerd). Wie wisselt, moet de app eerst verwijderen en verliest dan zijn voortgang op die telefoon.
- Wil je dat ze over elkaar heen installeren, kies dan *"Sleutel uit een Java-sleutelopslag gebruiken"* en upload `shop-boss-release.jks` met de tool die Google daar aanbiedt.

## 3. Winkelpagina (Main store listing)
- Standaardtaal: **English (United States)**, daarnaast een vertaling **Nederlands**.
- Kopieer de teksten uit `listing-en.md` en `listing-nl.md`.
- Upload het pictogram, de banner en de schermafbeeldingen van de juiste taal.
- Categorie: **Game → Simulation**.
- Contactgegevens: een e-mailadres is verplicht (vul je eigen adres in).
- Privacybeleid: `https://github.com/thedummies60-cmd/Shop-Boss/blob/main/PRIVACY.md`
  (werkt zodra deze versie op de `main`-branch staat).

## 4. App content (vragenlijsten in Play Console)
| Vraag | Antwoord |
|---|---|
| Privacybeleid | link hierboven |
| Advertenties | **Nee**, de app bevat geen advertenties |
| Toegang tot de app | Alle functies zijn beschikbaar zonder inloggen |
| Gegevensveiligheid (Data safety) | De app **verzamelt en deelt geen gegevens**. Geen account, dus geen account verwijderen. |
| Inhoudsclassificatie (IARC) | Categorie *Game*. Geen geweld, geen grof taalgebruik, geen gokken, geen aankopen, spelers kunnen niet met elkaar praten, geen locatie. De spoken in Spookboerderij zijn vriendelijke tekenfilmspoken. Verwachte uitkomst: **PEGI 3 / Everyone**. |
| Doelgroep | Kies de leeftijden waarvoor je de game echt maakt. Kies je ook kinderen onder 13, dan gelden de regels voor gezinnen ("Families"); Shop Boss voldoet daaraan, want er is geen reclame en er worden geen gegevens verzameld. |
| Overheid, financiën, gezondheid, nieuws | Nee |

## 5. Uitbrengen
1. *Testing → Closed testing*: upload de `.aab`, voeg minstens 12 testers toe (e-mailadressen) en laat ze 14 dagen testen.
2. Daarna: *Production → Create new release* met dezelfde `.aab`.
3. Verhoog bij elke nieuwe versie het versienummer (het bouwscript `tools/build_apk.py` doet dat met `--code`).
