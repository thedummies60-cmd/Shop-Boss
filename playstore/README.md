# Shop Boss op Google Play zetten – stappenplan

## Wat zit er in deze map
| Bestand | Waarvoor |
|---|---|
| `listing-en.md`, `listing-nl.md` | Naam, korte en lange beschrijving (Engels en Nederlands) |
| `icon-512.png` | App-pictogram, 512 × 512 |
| `feature-graphic-en.jpg`, `feature-graphic-nl.jpg` | Banner bovenaan de winkelpagina, 1024 × 500 |
| `screenshots/en/`, `screenshots/nl/` | 8 schermafbeeldingen per taal, 1080 × 1920 |
| `../PRIVACY.md` | Privacybeleid (Google vraagt een link) |
| `Shop-Boss-1.9.aab` | Het app-bestand voor Google Play (zodra het gemaakt is, zie stap 3) |

Je hebt ook de sleutel `shop-boss-release.jks` en het wachtwoord nodig (die heb je privé gekregen). **Nooit op GitHub zetten.**

## 1. Ontwikkelaarsaccount maken
1. Ga naar **play.google.com/console/signup** en log in met een Google-account.
2. Kies **Persoonlijk account** (Personal).
3. Betaal de eenmalige **25 dollar**.
4. Bevestig je identiteit (identiteitsbewijs), je telefoonnummer en je e-mailadres.
   Google vraagt ook om de **Play Console-app** op een Android-telefoon te installeren om het account te bevestigen.

> De eigenaar van het account moet **18 jaar of ouder** zijn. Vraag dit dus eventueel aan een ouder.

## 2. De app aanmaken
1. In Play Console: **Create app** (App maken).
2. Naam: **Shop Boss** · Standaardtaal: **English (United States)** · **Game** · **Free** (gratis).
3. Vink de verklaringen aan (richtlijnen en exportwetten) en klik **Create app**.

## 3. Het app-bestand (.aab)
Google Play aanvaardt voor nieuwe apps alleen een **.aab**, geen .apk.
- Staat `Shop-Boss-1.9.aab` in deze map, gebruik dat bestand.
- Staat het er nog niet: vraag Claude om de .aab te maken. Zet daarvoor in de Claude-app de modus naast het tekstvak op
  **Accept edits** in plaats van **Auto**, en keur de opdracht goed als Claude erom vraagt
  (Google's programma *bundletool* moet dan even draaien).

**Ondertekenen (Play App Signing):** kies bij de eerste upload **"Door Google gegenereerde sleutel"** (dat is het makkelijkst).
Jouw `shop-boss-release.jks` is dan je **uploadsleutel**: elke nieuwe versie moet je daarmee laten ondertekenen.
Let op: een app uit de Play Store kan niet over een app van GitHub heen geïnstalleerd worden (en omgekeerd).
Wie wisselt, moet de app eerst verwijderen.

## 4. Winkelpagina (Grow users → Store presence → Main store listing)
- Kopieer naam en beschrijvingen uit `listing-en.md`. Voeg via **Manage translations** ook **Nederlands** toe met `listing-nl.md`.
- Upload `icon-512.png`, de banner (`feature-graphic-en.jpg` / `-nl.jpg`) en de schermafbeeldingen uit `screenshots/en/` en `screenshots/nl/`.
- Categorie: **Game → Simulation**. Tags: Simulation, Casual, Management, Offline, Single player.
- Contactgegevens: vul **je eigen e-mailadres** in (verplicht).

## 5. App content (Policy → App content) – wat je moet antwoorden
| Onderdeel | Antwoord |
|---|---|
| Privacy policy | `https://github.com/thedummies60-cmd/Shop-Boss/blob/main/PRIVACY.md` (werkt zodra deze versie op `main` staat) |
| Ads (advertenties) | **No**, de app bevat geen advertenties |
| App access | **All functionality is available without special access** |
| Content rating | Vul de vragenlijst in: categorie **Game**; geen geweld, geen angstaanjagende inhoud (de spoken zijn vriendelijke tekenfilmspoken), geen grof taalgebruik, geen gokken, geen drugs, spelers kunnen niet met elkaar praten, geen aankopen, geen locatie. Verwachte uitkomst: **PEGI 3 / Everyone** |
| Target audience | Kies de leeftijden waarvoor je de game maakt. Kies je ook kinderen onder 13, dan gelden de gezinsregels (Families); Shop Boss voldoet daaraan (geen reclame, geen gegevens) |
| Data safety | **No**, de app verzamelt geen gegevens en deelt geen gegevens met anderen |
| Advertising ID | **No**, de app gebruikt geen advertentie-ID |
| Government apps / Financial features / Health / News | **No** |

## 6. Gesloten test (verplicht voor nieuwe persoonlijke accounts)
1. **Test and release → Testing → Closed testing → Create track**.
2. **Create new release**, upload `Shop-Boss-1.9.aab`, geef de release een naam (bijv. `1.9`) en sla op.
3. Kies de landen (bijv. België en Nederland, of alle landen).
4. **Testers**: maak een e-maillijst met **minstens 12 testers** (Google-accounts van vrienden en familie).
5. **Review release → Start rollout**. Deel de testlink met je testers. Zij moeten de app installeren en **14 dagen** geïnstalleerd houden.

## 7. Toegang tot productie aanvragen
Na 14 dagen met minstens 12 testers: ga naar het **Dashboard → Apply for production** (productie aanvragen)
en beantwoord de vragen over je test (wie testte er, wat heb je verbeterd).

## 8. Openbaar uitbrengen
1. **Production → Create new release**, upload dezelfde `.aab` (of een nieuwere versie).
2. Kies de landen, **Review release → Start rollout to Production**.
3. Google controleert de app; dat duurt meestal een paar dagen. Daarna staat Shop Boss in de Play Store.

## 9. Updates later
- Elke nieuwe versie moet een **hoger versienummer** (versionCode) hebben. Het bouwscript `tools/build_apk.py` doet dat met `--code`.
- Altijd ondertekenen met dezelfde `shop-boss-release.jks`.
- Upload de nieuwe `.aab` in **Production → Create new release**.
