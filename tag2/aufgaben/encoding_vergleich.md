# Zeichen und ihre Byte-Darstellung vergleichen

**Schwerpunkt:** Strings, Bytes, Kodierung, Dekodierung und Fehlerbehandlung.

## Teil 1: Encodings vergleichen

Lies einen Text ein und gib den ursprünglichen Text sowie seine Zeichenanzahl aus.

Untersuche anschließend drei Kodierungen:

1. Kodiere den Text als UTF-8. Gib die Byte-Darstellung und die Anzahl der Bytes aus.
2. Versuche dasselbe mit Latin-1.
3. Versuche, den Text als ASCII zu kodieren, und gib bei Erfolg die Bytes aus.

Wenn Latin-1 oder ASCII ein Zeichen nicht darstellen kann, gib eine verständliche Meldung aus. Die weiteren Untersuchungen sollen trotzdem stattfinden. Ersetze oder entferne unzulässige Zeichen dabei nicht stillschweigend.

## Prüfe dein Programm

| Eingabe | Zeichen | UTF-8: Bytes | Latin-1: Bytes | ASCII |
|---|---|---|---|---|
| Hallo | 5 | 5 | 5 | Möglich |
| Müsli | 5 | 6 | 5 | Nicht möglich |
| € | 1 | 3 | Nicht möglich | Nicht möglich |
| 😀 | 1 | 4 | Nicht möglich | Nicht möglich |

Für diese Eingaben sollen fehlgeschlagene Kodierungen als Meldung erscheinen, ohne das Programm abzubrechen. Die genannten Zeichenanzahlen beziehen sich genau auf die Zeichen in der Tabelle.

## Teil 2: einen falsch dekodierten Text reparieren

Gegeben ist der beschädigte Text **MÃ¼sli**. Er entstand so:

- Der ursprüngliche Text wurde korrekt als UTF-8 kodiert.
- Diese Bytes wurden anschließend fälschlich als Latin-1 dekodiert.

Mache diese beiden Schritte in umgekehrter Richtung rückgängig. Gib den beschädigten und den reparierten Text aus. Das erwartete Ergebnis lautet **Müsli**.

Verwende die bekannte Kodierungsfolge für die Reparatur. Ein direktes Ersetzen der sichtbaren Zeichenfolge ist hier nicht die Aufgabe.

## Erkläre deine Beobachtung

- Warum hat „Müsli“ fünf Zeichen, aber in UTF-8 sechs Bytes?
- Warum können Latin-1 und ASCII nicht jeden eingegebenen Text darstellen?
- Warum lässt sich die gezeigte Reparatur nicht auf beliebige beschädigte Texte übertragen?

Die Anzahl der Zeichen eines Strings und die Anzahl seiner kodierten Bytes sind verschiedene Größen. In den hier gewählten Beispielen entspricht jedes sichtbare Zeichen genau einem Unicode-Codepunkt.

**Eigene Datei:** `tag2/loesungen/encoding_vergleich.py`
