# Lottobude - Bug-Katalog (Kursleitung)

**Nicht an Teilnehmer weitergeben.**

Jeder Bug ist ueber eine Environment-Variable schaltbar. Aenderung wirkt
nach `docker compose up -d` fuer die betroffene Instanz; ein Reset der
Trainingsdaten ist dafuer nicht noetig.

| Toggle | Standard |
|---|---|
| `LOTTOBUDE_BUG_API_ADMIN_OFFEN` | `true` |
| `LOTTOBUDE_BUG_FREMDE_TIPPS_LESBAR` | `true` |
| `LOTTOBUDE_BUG_ELF_TIPPS_ERLAUBT` | `true` |
| `LOTTOBUDE_BUG_GEWINN_VIER_TREFFER` | `true` |
| `LOTTOBUDE_BUG_ABGEGEBENER_SCHEIN_AENDERBAR` | `true` |
| `LOTTOBUDE_BUG_LEERE_DATEI_ERFOLG` | `true` |
| `LOTTOBUDE_BUG_CSV_DUPLIKATE_ERLAUBT` | `true` |
| `LOTTOBUDE_BUG_LEERER_SCHEIN_ABGEBBAR` | `true` |
| `LOTTOBUDE_BUG_GEWINNZAHL_OHNE_BEREICH` | `true` |
| `LOTTOBUDE_BUG_ZAHL_ABSCHNEIDEN` | `true` |
| `LOTTOBUDE_BUG_HEADER_NUR_SPALTENZAHL` | `true` |
| `LOTTOBUDE_BUG_DOPPELTE_AUSWERTUNG` | `true` |
| `LOTTOBUDE_BUG_IMPORTZAEHLER_FALSCH` | `true` |
| `LOTTOBUDE_BUG_GESPERRTER_DARF_ABGEBEN` | `true` |

---

## BUG-001 - Spielleitungs-Endpunkte der API ohne Berechtigungspruefung

**Toggle:** `LOTTOBUDE_BUG_API_ADMIN_OFFEN=true`

**Verletzte Regel:** BR-CONS-001 (GUI, API und CSV-Import muessen dieselben
fachlichen Regeln anwenden), sinngemaess auch die Zugriffsbeschraenkung der
Spielleitung aus LOTTO-501.

**Sollverhalten:** Was in der Oberflaeche der Spielleitung vorbehalten ist,
muss auch ueber die API der Spielleitung vorbehalten sein.

**Istverhalten:** Diese Endpunkte sind ohne Anmeldung aufrufbar:

- `POST /api/draws` - Ziehung anlegen
- `POST /api/draws/{id}/numbers` - Gewinnzahlen erfassen
- `POST /api/draws/{id}/evaluate` - Auswertung starten

Die Weboberflaeche weist dieselben Aktionen fuer Nichtadministratoren mit
403 ab, auch bei direktem POST.

**Reproduktion:**

```
curl -X POST https://<instanz>/api/draws \
     -H 'Content-Type: application/json' \
     -d '{"draw_date":"2026-09-01"}'
```

Ohne jede Anmeldung entsteht eine neue Ziehung.

**Schweregrad:** hoch - unbefugte Dritte koennen den Spielbetrieb steuern,
insbesondere eine Ziehung vorzeitig auswerten.

**Erwarteter Fundweg:** nur ueber API-Tests. Wer ausschliesslich die
Oberflaeche prueft, sieht ein korrekt abgesichertes System. Deckt die
Fehlerklasse "API / GUI-Divergenz" aus TRAINING_CONCEPT.md ab.

**Nicht findbar durch:** GUI-Tests, Unit-Tests der Fachlogik.

---

## BUG-002 - Fremde Tippscheine und Tipps ueber die API lesbar

**Toggle:** `LOTTOBUDE_BUG_FREMDE_TIPPS_LESBAR=true`

**Verletzte Regel:** BR-USER-002 (Ein Benutzer sieht nur seine eigenen
Tippscheine und Ergebnisse), zusammen mit BR-CONS-001.

**Sollverhalten:** Ein Benutzer kann ueber keinen Weg Tippscheine oder Tipps
anderer Spieler einsehen.

**Istverhalten:** Diese Endpunkte liefern ohne Anmeldung Daten aller Spieler:

- `GET /api/tickets` - alle Tippscheine, auch fremde
- `GET /api/tickets/{id}` - beliebiger Tippschein ueber die Kennung
- `GET /api/tips` - alle Tipps aller Spieler
- `GET /api/tips/{id}` - beliebiger Tipp

Die Weboberflaeche zeigt unter "Meine Tipps" korrekt nur die eigenen.

**Reproduktion:**

```
curl https://<instanz>/api/tickets
curl https://<instanz>/api/tickets/2
```

Ohne Anmeldung erscheinen die Tippscheine beider Spieler.

**Schweregrad:** mittel bis hoch - Verletzung der Vertraulichkeit; in einem
echten Spielbetrieb waere die Tippabgabe anderer Teilnehmer einsehbar.

**Erwarteter Fundweg:** API-Tests, oder Vergleich zwischen dem, was die
Oberflaeche zeigt, und dem, was die Schnittstelle herausgibt. Deckt die
Fehlerklassen "Berechtigungen" und "API / GUI-Divergenz" ab.

**Nicht findbar durch:** reine GUI-Tests.

---

## BUG-003 - Ein Tipp zu viel je Tippschein

**Toggle:** `LOTTOBUDE_BUG_ELF_TIPPS_ERLAUBT=true`

**Verletzte Regel:** BR-TICKET-001 (mindestens 1, hoechstens 10 Tipps),
Invariante 2 aus DOMAIN.md.

**Sollverhalten:** Der elfte Tipp wird mit `TICKET_TOO_MANY_TIPS` abgewiesen.

**Istverhalten:** Der elfte Tipp wird angenommen, erst der zwoelfte abgewiesen.
Klassischer Off-by-one an der oberen Grenze.

**Reproduktion:** Tippschein anlegen und elf Tipps hinzufuegen - ueber die
Oberflaeche oder per `POST /api/tickets/{id}/tips`.

**Schweregrad:** mittel

**Erwarteter Fundweg:** Grenzwertanalyse. Wer nur 1 und 10 prueft, findet ihn
nicht - es braucht den Wert direkt oberhalb der Grenze. Fehlerklasse
"Grenzwerte".

---

## BUG-004 - Falscher Gewinnbetrag bei vier Treffern

**Toggle:** `LOTTOBUDE_BUG_GEWINN_VIER_TREFFER=true`

**Verletzte Regel:** Gewinntabelle in BUSINESS_RULES.md (4 Treffer = 100 EUR).

**Sollverhalten:** 4 Treffer ergeben 100 EUR.

**Istverhalten:** 4 Treffer ergeben 10 EUR - denselben Betrag wie 3 Treffer.
Die Gewinnklasse wird korrekt mit 4 ausgewiesen, nur der Betrag ist falsch.

**Reproduktion:** Tipp mit genau vier Gewinnzahlen abgeben, Ziehung
durchfuehren und auswerten, Ergebnis ansehen.

**Schweregrad:** hoch - unmittelbar geldwirksam.

**Erwarteter Fundweg:** Entscheidungstabelle ueber alle Trefferzahlen 0..6.
Wer nur "gewinnt / gewinnt nicht" prueft, uebersieht ihn, weil ein Gewinn ja
angezeigt wird. Auffaellig wird er erst im Vergleich der Betraege
untereinander. Fehlerklasse "Entscheidungslogik".

---

## BUG-005 - Abgegebener Tippschein bleibt aenderbar

**Toggle:** `LOTTOBUDE_BUG_ABGEGEBENER_SCHEIN_AENDERBAR=true`

**Verletzte Regel:** BR-TICKET-003, Invariante 4 aus DOMAIN.md.

**Sollverhalten:** Nach der Abgabe wird ein weiterer Tipp mit
`TICKET_NOT_EDITABLE` abgewiesen.

**Istverhalten:** Auch ein Tippschein im Status ABGEGEBEN nimmt weitere Tipps
an. Der Status bleibt dabei unveraendert.

**Reproduktion:** Tippschein abgeben, danach
`POST /api/tickets/{id}/tips` - liefert 200.

**Schweregrad:** hoch - Tipps koennten nach Kenntnis der Gewinnzahlen
nachgereicht werden.

**Erwarteter Fundweg:** Zustandsbasiertes Testen. Es genuegt nicht, den
Happy Path zu pruefen; man muss nach dem Zustandsuebergang erneut eine
Aktion versuchen, die im neuen Zustand verboten ist. Fehlerklasse "Zustaende".

---

## BUG-006 - Datei ohne Kopfzeile meldet erfolgreichen Import

**Toggle:** `LOTTOBUDE_BUG_LEERE_DATEI_ERFOLG=true`

**Verletzte Regel:** CSV_FORMAT.md - die Kopfzeile ist Pflicht. Sinngemaess
auch BR-CSV-004 und BR-CSV-006.

**Sollverhalten:** Eine leere Datei bzw. eine Datei ohne Kopfzeile wird mit
`CSV_HEADER_INVALID` abgewiesen, der Lauf endet im Status FEHLER.

**Istverhalten:** Der Lauf endet im Status IMPORTIERT mit 0 gelesenen,
0 importierten und 0 abgewiesenen Datensaetzen. Die Annahmestelle erhaelt
also eine Erfolgsmeldung, obwohl nichts uebernommen wurde.

**Reproduktion:** Eine leere Datei hochladen.

**Schweregrad:** mittel - ein fehlgeschlagener Upload bleibt unbemerkt.

**Erwarteter Fundweg:** Testen mit Sonderfaellen von Eingabedateien. Fehlt
die leere Datei in den Testdaten, bleibt der Bug unentdeckt. Fehlerklasse
"CSV / Syntax".

---

## BUG-007 - Doppelte Lottozahlen werden beim CSV-Import nicht erkannt

**Toggle:** `LOTTOBUDE_BUG_CSV_DUPLIKATE_ERLAUBT=true`

**Verletzte Regel:** BR-TIP-003 (Eindeutigkeit), BR-CSV-003 (fuer
importierte Tipps gelten dieselben Regeln wie fuer Web-Tipps),
BR-CONS-001, Invariante 1 aus DOMAIN.md.

**Sollverhalten:** Eine Zeile mit doppelten Zahlen wird mit
`LOTTO_NUMBER_DUPLICATE` abgewiesen.

**Istverhalten:** Ueber den CSV-Import werden doppelte Zahlen gespeichert.
Dieselbe Eingabe wird ueber die Weboberflaeche und ueber
`POST /api/tickets/{id}/tips` korrekt abgewiesen.

**Reproduktion:**

```
ticket_id;draw_date;tip_no;n1;n2;n3;n4;n5;n6
HH-20001;2026-08-15;1;7;7;7;12;18;23
```

Der Import meldet 1 gelesen, 1 importiert, 0 abgewiesen.

**Schweregrad:** mittel bis hoch - erzeugt fachlich unmoegliche Tipps in der
Datenbank und verzerrt die Auswertung.

**Erwarteter Fundweg:** Nur ueber den CSV-Weg. Wer die Regel einmal ueber die
Oberflaeche prueft und sie fuer erledigt haelt, findet ihn nicht - es braucht
den Gedanken, dieselbe Regel auf jedem Eingabekanal zu pruefen. Fehlerklasse
"Aequivalenzklassen / Validierung" in Verbindung mit Kanal-Divergenz.

---

## BUG-008 - Tippschein ohne Tipps kann abgegeben werden

**Toggle:** `LOTTOBUDE_BUG_LEERER_SCHEIN_ABGEBBAR=true`

**Verletzte Regel:** BR-TICKET-001 (mindestens 1 Tipp), Invariante 2.

**Sollverhalten:** Die Abgabe eines leeren Tippscheins wird mit
`TICKET_NO_TIPS` abgewiesen.

**Istverhalten:** Der leere Tippschein wechselt auf ABGEGEBEN.

**Reproduktion:** Tippschein anlegen, ohne Tipp `POST /api/tickets/{id}/submit`.

**Schweregrad:** mittel

**Erwarteter Fundweg:** Grenzwertanalyse an der **unteren** Grenze.
Gegenstueck zu BUG-003 - wer nur nach oben prueft, findet nur einen von beiden.
Fehlerklasse "Grenzwerte".

---

## BUG-009 - Gewinnzahlen ausserhalb des gueltigen Bereichs

**Toggle:** `LOTTOBUDE_BUG_GEWINNZAHL_OHNE_BEREICH=true`

**Verletzte Regel:** BR-DRAW-001 (sechs unterschiedliche Zahlen aus 1..49).

**Sollverhalten:** Die Gewinnzahl 99 wird mit `LOTTO_NUMBER_OUT_OF_RANGE`
abgewiesen.

**Istverhalten:** Beliebige Ganzzahlen werden als Gewinnzahlen gespeichert.
Fuer **Tipps** greift dieselbe Pruefung dagegen korrekt.

**Reproduktion:** `POST /api/draws/{id}/numbers` mit `[1,2,3,4,5,99]`.

**Schweregrad:** hoch - verfaelscht jede folgende Auswertung.

**Erwarteter Fundweg:** Dieselbe Regel auf beiden Objekten pruefen. Wer die
Bereichspruefung nur am Tipp testet und sie fuer die Ziehung als erledigt
ansieht, findet ihn nicht. Fehlerklasse "Grenzwerte".

---

## BUG-010 - Nicht numerische Anhaengsel werden abgeschnitten

**Toggle:** `LOTTOBUDE_BUG_ZAHL_ABSCHNEIDEN=true`

**Verletzte Regel:** CSV_FORMAT.md (n1..n6 sind Ganzzahlen),
Fehlercode `LOTTO_NUMBER_NOT_INTEGER`.

**Sollverhalten:** Der Wert `12a` wird mit `LOTTO_NUMBER_NOT_INTEGER`
abgewiesen.

**Istverhalten:** Fuehrende Ziffern werden uebernommen, der Rest still
verworfen: aus `12a` wird die Zahl 12. Es gibt keine Meldung.

**Reproduktion:** CSV-Zeile mit `12a` als erster Lottozahl importieren, danach
den gespeicherten Tipp ansehen.

**Schweregrad:** hoch - die Anwendung erfindet stillschweigend Daten.

**Erwarteter Fundweg:** Negativtests mit fehlerhaften Werten **und**
anschliessende Kontrolle des gespeicherten Datensatzes. Wer nur prueft, ob
der Import nicht abstuerzt, uebersieht ihn. Fehlerklasse
"Aequivalenzklassen / Validierung".

---

## BUG-011 - Falsche Kopfzeile wird akzeptiert

**Toggle:** `LOTTOBUDE_BUG_HEADER_NUR_SPALTENZAHL=true`

**Verletzte Regel:** CSV_FORMAT.md - die Kopfzeile ist vorgegeben.

**Sollverhalten:** Weicht die Kopfzeile ab, wird der Import mit
`CSV_HEADER_INVALID` abgelehnt.

**Istverhalten:** Geprueft wird nur die **Anzahl** der Spalten. Eine Datei mit
den Spaltennamen `spalte1;spalte2;...` wird anstandslos importiert, solange
neun Spalten vorhanden sind.

**Reproduktion:** Kopfzeile durch `spalte1;spalte2;spalte3;a;b;c;d;e;f`
ersetzen und importieren.

**Schweregrad:** mittel - Dateien fremden Formats werden falsch gedeutet.

**Erwarteter Fundweg:** Testfaelle zur Kopfzeile, die nicht nur Spalten
weglassen, sondern sie **umbenennen**. Fehlerklasse "CSV / Syntax".

---

## BUG-012 - Ausgewertete Ziehung kann erneut ausgewertet werden

**Toggle:** `LOTTOBUDE_BUG_DOPPELTE_AUSWERTUNG=true`

**Verletzte Regel:** BR-DRAW-004, Invariante 7 (ein Tipp darf je Ziehung nur
einmal ausgewertet werden).

**Sollverhalten:** Eine erneute Auswertung wird mit
`DRAW_ALREADY_EVALUATED` abgewiesen.

**Istverhalten:** Jede Wiederholung erzeugt einen weiteren Satz
Auswertungssaetze. Nach zwei Wiederholungen erscheinen die Ergebnisse
dreifach; die Gewinnsumme vervielfacht sich entsprechend.

**Reproduktion:** `POST /api/draws/1/evaluate` mehrfach aufrufen, danach
`GET /api/results?user_id=1&draw_id=1`.

**Schweregrad:** hoch - vervielfacht ausgewiesene Gewinne.

**Erwarteter Fundweg:** Wiederholung derselben Aktion im Endzustand, danach
Kontrolle der **Anzahl** der Ergebnissaetze. Ein einzelner Aufruf sieht
korrekt aus. Fehlerklasse "Zustaende".

---

## BUG-013 - Importzaehler meldet Tippscheine statt Tipps

**Toggle:** `LOTTOBUDE_BUG_IMPORTZAEHLER_FALSCH=true`

**Verletzte Regel:** BR-CSV-006 und CSV_FORMAT.md - das Importergebnis weist
die Anzahl importierter **Tipps** aus.

**Sollverhalten:** Zwei Tipps auf einem Tippschein ergeben
`imported_records = 2`.

**Istverhalten:** Gezaehlt werden die angelegten Tippscheine. Zwei Tipps auf
einem Schein werden als 1 gemeldet. Die Zeilen sind tatsaechlich importiert -
nur die Statistik stimmt nicht.

**Reproduktion:** Datei mit zwei Zeilen gleicher `ticket_id` importieren:
gelesen 2, importiert 1, abgewiesen 0.

**Schweregrad:** mittel - die Zahlen gehen nicht auf, was Fehlersuche
erschwert.

**Erwarteter Fundweg:** Pruefen, ob gelesen = importiert + abgewiesen
aufgeht, und Abgleich der Statistik mit dem tatsaechlichen Datenbestand.
Fehlerklasse "Integration / Persistenz".

---

## BUG-014 - Gesperrter Benutzer kann ueber die API abgeben

**Toggle:** `LOTTOBUDE_BUG_GESPERRTER_DARF_ABGEBEN=true`

**Verletzte Regel:** BR-USER-001 (nur aktive Benutzer duerfen neue
Tippscheine abgeben), BR-CONS-001.

**Sollverhalten:** Ein Tippschein fuer einen gesperrten Benutzer wird mit
`USER_INACTIVE` abgewiesen.

**Istverhalten:** Ueber `POST /api/tickets` mit der Kennung des gesperrten
Benutzers entsteht ein Tippschein. Ueber die Oberflaeche ist das nicht
moeglich, weil bereits die Anmeldung mit `USER_INACTIVE` scheitert.

**Reproduktion:** `POST /api/tickets` mit `{"user_id":3,"draw_id":2}`.

**Schweregrad:** mittel

**Erwarteter Fundweg:** Nur ueber die API. Wer die Sperre an der Anmeldung
prueft und sie fuer wirksam haelt, findet ihn nicht - die Regel gilt der
**Abgabe**, nicht der Anmeldung. Fehlerklassen "Berechtigungen" und
"API / GUI-Divergenz".
