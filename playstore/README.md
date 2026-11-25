# Shop Boss op Google Play zetten – stappenplan

## Wat zit er in deze map
| Bestand | Waarvoor |
|---|---|
| `listing-en.md`, `listing-nl.md` | Naam, korte en lange beschrijving (Engels en Nederlands) |
| `icon-512.png` | App-pictogram, 512 × 512 |
| `feature-graphic-en.jpg`, `feature-graphic-nl.jpg` | Banner bovenaan de winkelpagina, 1024 × 500 |
| `screenshots/en/`, `screenshots/nl/` | 19 schermafbeeldingen per taal voor telefoons, 1080 × 1920 (Google toont er max. 8: kies je favorieten) |
| `screenshots-unfolded/en/`, `screenshots-unfolded/nl/` | 8 schermafbeeldingen per taal voor uitgevouwen telefoons en tablets, 1380 × 1656 |
| `../PRIVACY.md` | Privacybeleid (Google vraagt een link) |
| `Shop-Boss-2.9.aab` | Het app-bestand voor Google Play (versie 2.9, code 33, met de politie, zonder Winkel, ondertekend met je uploadsleutel) |
| `Shop-Boss-1.9.aab` | De oude versie 1.9 (zonder Winkel). Gebruik liever 2.0 |

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
Gebruik `Shop-Boss-2.9.aab` uit deze map.

**Ondertekenen (Play App Signing):** kies bij de eerste upload **"Door Google gegenereerde sleutel"** (dat is het makkelijkst).
Jouw `shop-boss-release.jks` is dan je **uploadsleutel**: elke nieuwe versie moet je daarmee laten ondertekenen.
Let op: een app uit de Play Store kan niet over een app van GitHub heen geïnstalleerd worden (en omgekeerd).
Wie wisselt, moet de app eerst verwijderen.

## 4. Winkelpagina (Grow users → Store presence → Main store listing)
- Kopieer naam en beschrijvingen uit `listing-en.md`. Voeg via **Manage translations** ook **Nederlands** toe met `listing-nl.md`.
- Upload `icon-512.png`, de banner (`feature-graphic-en.jpg` / `-nl.jpg`) en de schermafbeeldingen uit `screenshots/en/` en `screenshots/nl/` (bij **Phone**).
  De foto's uit `screenshots-unfolded/` zet je bij **7-inch tablet** en **10-inch tablet** (daar horen ook uitgevouwen telefoons bij).
- Categorie: **Game → Simulation**. Tags: Simulation, Casual, Management, Offline, Single player.
- Contactgegevens: vul **je eigen e-mailadres** in (verplicht).

## 5. App content (Policy → App content) – wat je moet antwoorden
| Onderdeel | Antwoord |
|---|---|
| Privacy policy | `https://github.com/thedummies60-cmd/Shop-Boss/blob/main/PRIVACY.md` (werkt zodra deze versie op `main` staat) |
| Ads (advertenties) | **No**, de app bevat geen advertenties |
| In-app purchases | **No** (de Winkel staat in 2.4 uit) |
| App access | **All functionality is available without special access** |
| Content rating | Vul de vragenlijst in: categorie **Game**; geen geweld, geen angstaanjagende inhoud (de spoken zijn vriendelijke tekenfilmspoken), geen grof taalgebruik, geen gokken, geen drugs, spelers kunnen niet met elkaar praten, geen locatie. Bij de vraag over **digitale aankopen**: **No**. Verwachte uitkomst: **PEGI 3 / Everyone** |
| Target audience | Kies de leeftijden waarvoor je de game maakt. Kies je ook kinderen onder 13, dan gelden de gezinsregels (Families). Shop Boss voldoet daaraan: geen reclame, geen gegevens, en de Winkel zegt dat kinderen het eerst aan een ouder moeten vragen |
| Data safety | **No**, de app verzamelt geen gegevens en deelt geen gegevens met anderen (betalingen gaan helemaal via Google Play) |
| Advertising ID | **No**, de app gebruikt geen advertentie-ID |
| Government apps / Financial features / Health / News | **No** |

## 6. Gesloten test (verplicht voor nieuwe persoonlijke accounts)
1. **Test and release → Testing → Closed testing → Create track**.
2. **Create new release**, upload `Shop-Boss-2.9.aab`, geef de release een naam (bijv. `2.9`) en sla op.
3. Kies de landen (bijv. België en Nederland, of alle landen).
4. **Testers**: maak een e-maillijst met **minstens 12 testers** (Google-accounts van vrienden en familie).
5. **Review release → Start rollout**. Deel de testlink met je testers. Zij moeten de app installeren en **14 dagen** geïnstalleerd houden.

## 6b. De Winkel instellen (aankopen met echt geld)
> **Staat uit sinds versie 2.4.** Deze stap heb je nu niet nodig. Wil je de Winkel later terug, vraag dan om hem weer aan te zetten.
Dit moet een **ouder** doen: Google vraagt iemand van 18 jaar of ouder, met een bankrekening en belastinggegevens.
Het geld van de aankopen komt op die bankrekening (Google houdt 15% in).

1. **Betaalprofiel maken:** in Play Console ga je naar **Setup → Payments profile** (of **Monetize with Play → Monetization setup**)
   en maak je een betaalprofiel (*payments profile / merchant account*). Vul naam, adres, bankrekening en belastinggegevens in.
2. **Eerst een .aab uploaden:** producten kun je pas aanmaken nadat er een versie met de Winkel is geüpload
   (stap 6: `Shop-Boss-2.9.aab` in de gesloten test).
3. **Producten aanmaken:** **Monetize with Play → Products → In-app products → Create product**.
   Maak deze 7 producten. De **Product ID** moet precies zo geschreven worden, anders vindt de game ze niet:

   | Product ID | Naam (Engels / Nederlands) | Wat je krijgt | Prijsvoorstel |
   |---|---|---|---|
   | `cash_small` | Bag of cash / Zak met geld | geld in de wereld waar je bent | € 0,99 |
   | `cash_medium` | Pile of cash / Stapel geld | 4× zoveel geld | € 2,99 |
   | `cash_large` | Treasure chest / Schatkist | 12× zoveel geld | € 4,99 |
   | `double_cash` | Double cash / Dubbel geld | elke klant betaalt 2×, voor altijd | € 2,99 |
   | `pack_colors` | All colors / Alle kleuren | alle 15 gewone kleuren | € 1,99 |
   | `pack_hats` | All hats / Alle hoeden | alle 17 gewone hoeden | € 1,99 |
   | `pack_legendary` | Legendary pack / Legendarisch pakket | Regenboog, Diamant, Neon, Aureool, Eenhoornhoorn en Vuurkroon | € 3,99 |

   Bij elk product: vul naam en beschrijving in, kies de prijs (Google rekent hem om voor andere landen),
   klik **Save** en daarna **Activate**. De geldpakketten kun je vaak kopen, de andere maar één keer: dat regelt de game zelf.
4. **Gratis testen:** ga naar **Setup → License testing** en zet de Gmail-adressen van jezelf en je testers erin.
   Die kunnen dan "kopen" zonder te betalen (Google toont "Test card, always approves").
5. **Controleren:** installeer de app via de testlink, open **Menu → Winkel**. Je ziet nu de prijzen.
   Zie je "De winkel werkt nu niet", wacht dan een paar uur: nieuwe producten hebben soms even tijd nodig.

> Ouders kunnen in de Play Store-app instellen dat elke aankoop een wachtwoord of goedkeuring nodig heeft
> (**Profiel → Instellingen → Gezin → Verificatie vereisen voor aankopen**).

## 7. Toegang tot productie aanvragen
Na 14 dagen met minstens 12 testers: ga naar het **Dashboard → Apply for production** (productie aanvragen)
en beantwoord de vragen over je test (wie testte er, wat heb je verbeterd).

## 8. Openbaar uitbrengen
1. **Production → Create new release**, upload dezelfde `.aab` (of een nieuwere versie).
2. Kies de landen, **Review release → Start rollout to Production**.
3. Google controleert de app; dat duurt meestal een paar dagen. Daarna staat Shop Boss in de Play Store.

## 9. Updates later
- Elke nieuwe versie moet een **hoger versienummer** (versionCode) hebben. Het bouwscript `tools/build_android.py` doet dat met `--code` (2.9 heeft code 33).
- Altijd ondertekenen met dezelfde `shop-boss-release.jks`.
- Upload de nieuwe `.aab` in **Production → Create new release**.
