# Eine ASCII-Tabelle aufbauen

**Schwerpunkt:** Schleifen, Zahlenbereiche, Zeichencodes und Spaltenformatierung.

## Schritt 1: ein Eintrag pro Zeile

Gib für jeden Code von **32 bis einschließlich 127** die Zahl und das zugehörige Zeichen aus.

- Ermittle das Zeichen aus seinem Zahlencode.
- Stelle Code 32 ausdrücklich als `<SPACE>` dar.
- Stelle Code 127 ausdrücklich als `<DEL>` dar.
- Zeige alle anderen Zeichen unverändert an.
- Richte die Zahlen rechtsbündig aus.

32 steht für das Leerzeichen. 127 ist ein nicht druckbares Steuerzeichen; deshalb erhält es eine sichtbare Ersatzdarstellung.

## Schritt 2: drei Einträge pro Zeile

Gestalte dieselben Daten als Tabelle. Jede Zeile enthält drei aufeinanderfolgende Paare aus Code und Zeichen.

Die Anordnung soll so aussehen:

| Code | Zeichen | Code | Zeichen | Code | Zeichen |
|---|---|---|---|---|---|
| 32 | `<SPACE>` | 33 | ! | 34 | " |
| 35 | # | 36 | $ | 37 | % |
| 125 | } | 126 | ~ | 127 | `<DEL>` |

Die letzte Beispielzeile zeigt das Tabellenende; dazwischen müssen alle weiteren Codes erscheinen.

- Ergänze eine Kopfzeile mit Spaltennamen und passende Trennlinien.
- Richte die Codes rechtsbündig und die Zeichen zentriert aus.
- Verwende feste Spaltenbreiten, damit auch `<SPACE>` und `<DEL>` hineinpassen.

## Prüfe dein Programm

- Jeder Code von 32 bis 127 erscheint pro Darstellung genau einmal.
- Die erste Darstellung hat 96 Eintragszeilen.
- Die zweite Darstellung hat 32 Datenzeilen mit jeweils drei Einträgen.
- Die beiden Sonderdarstellungen stehen an der richtigen Stelle.

## Hinweis

Überlege bei der zweiten Darstellung, um wie viel der Schleifenzähler pro Durchlauf weitergehen muss. Funktionen und Listen sind für diese Aufgabe nicht erforderlich.

**Eigene Datei:** `tag2/loesungen/ascii_tabelle_1.py`
