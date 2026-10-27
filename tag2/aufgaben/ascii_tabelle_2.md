# Zeichencodes in verschiedenen Zahlensystemen anzeigen

**Schwerpunkt:** `for`-Schleifen, `range()`, `chr()` und Formatierung von Zahlen.

## Stufe 1: ASCII

Erzeuge eine Tabelle der ASCII-Zeichen mit den Codes **32 bis einschließlich 126**.

Gib pro Zeile vier Angaben aus:

1. den Code als Dezimalzahl,
2. das zugehörige Zeichen,
3. den Code als Hexadezimalzahl,
4. den Code als Oktalzahl.

Verwende eine Kopfzeile und feste Spaltenbreiten. Hexadezimalwerte sollen zweistellig mit Kleinbuchstaben erscheinen, Oktalwerte dreistellig mit führenden Nullen. Präfixe für die Zahlensysteme sind nicht erforderlich.

## Kontrollwerte

| Dezimal | Zeichen | Hexadezimal | Oktal |
|---|---|---|---|
| 32 | Leerzeichen | 20 | 040 |
| 65 | A | 41 | 101 |
| 97 | a | 61 | 141 |
| 126 | ~ | 7e | 176 |

Die Bezeichnung „Leerzeichen“ erklärt hier den Kontrollwert. In deiner Tabelle darf an dieser Stelle das tatsächliche Leerzeichen stehen. Die Tabelle enthält 95 Datenzeilen; Code 127 gehört nicht dazu.

## Stufe 2: Latin-1 ergänzen

Hänge eine zweite Tabelle für die Codes **160 bis einschließlich 255** an. Hier genügen Dezimalwert und Zeichen.

Prüfe beispielsweise diese Zuordnungen: 196 → Ä, 223 → ß, 228 → ä, 252 → ü. Die zweite Tabelle enthält 96 Datenzeilen.

## Beobachtungsfragen

- Welche zusätzlichen Zeichen findest du im zweiten Bereich?
- Warum sind manche Einträge kaum oder gar nicht sichtbar?
- Was ist der Unterschied zwischen einem Zeichencode und den Bytes einer Textdatei?

`chr()` erzeugt ein Unicode-Zeichen. Im hier verwendeten Bereich stimmen seine Codepunkte mit den Latin-1-Zeichenwerten überein. Die Ausgabe von Zeichen allein legt noch keine Dateikodierung fest.

Die nächste Aufgabe [Encodings vergleichen](encoding_vergleich.md) untersucht die Bytes.

**Eigene Datei:** `tag2/loesungen/ascii_tabelle_2.py`
