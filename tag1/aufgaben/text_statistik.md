# Eine Zeichenstatistik erstellen

**Schwerpunkt:** String-Länge, Zeichen zählen und Prozentwerte formatieren.

## Grundaufgabe

Lies einen nichtleeren Text ein und ermittle:

1. die Anzahl aller Zeichen,
2. die Anzahl des Kleinbuchstabens `e`,
3. den Anteil dieses Buchstabens an allen Zeichen.

Gib die Länge und die Anzahl aus. Zeige den Anteil als Prozentwert mit genau zwei Nachkommastellen an.

Für den Anteil gilt: **Anteil = Anzahl der kleinen e / Anzahl aller Zeichen**.

Leerzeichen und Satzzeichen zählen zur Gesamtlänge. Ein großes `E` wird in der Grundaufgabe nicht als kleines `e` gezählt. Verändere oder kürze den eingegebenen Text daher nicht vor dem Zählen.

Für die Grundaufgabe darfst du voraussetzen, dass mindestens ein Zeichen eingegeben wird.

## Prüfe dein Programm

| Eingabe | Zeichen insgesamt | Kleine e | Anteil |
|---|---|---|---|
| Tee | 3 | 2 | 66.67% |
| Ebbe und Flut | 13 | 1 | 7.69% |
| EEE | 3 | 0 | 0.00% |
| e e | 3 | 2 | 66.67% |

## Erweiterungen

- Gib zusätzlich die Anzahl der Leerzeichen aus.
- Zähle in einer weiteren Variante große und kleine e gemeinsam. Für `EEE` wären das drei Treffer und 100.00%.
- Sobald du Verzweigungen kennst: Behandle einen leeren Text, ohne durch null zu teilen.

## Hinweis

Bei einer Prozentformatierung wird aus dem Anteil 0,5 die Anzeige 50.00%. Achte darauf, den Faktor 100 nicht zweimal anzuwenden.

**Eigene Datei:** `tag1/loesungen/text_statistik.py`
