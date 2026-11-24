# Tipp und Ziehung vergleichen

**Schwerpunkt:** Schnittmengen auf eine konkrete Fragestellung anwenden.

## Aufgabe

1. Verwende den festen Tipp `{7, 13, 19, 23, 31, 42}`.
2. Ziehe sechs verschiedene Zahlen von 1 bis 49 und bestimme die gemeinsame Menge.
3. Gib Tipp, Ziehung und richtige Zahlen sortiert aus, danach die Trefferzahl.

## Prüfe dein Programm

- Kontrolliere den Vergleich zunächst mit der festen Ziehung `{1, 7, 13, 20, 31, 49}`: richtig sind 7, 13 und 31; die Trefferzahl ist 3.
- Ein identischer Tipp und eine identische Ziehung ergeben 6 Treffer.
- Zwei disjunkte Mengen ergeben 0 Treffer.
- Die Trefferzahl liegt immer zwischen 0 und 6.

## Erweiterung

- Wiederhole den Vergleich 1.000-mal und zähle die Häufigkeiten von 0 bis 6 Treffern.

## Referenz

- [Referenzlösung mit Zufallsziehung](../../loesungen/erfahren/lottobudeNG.py)
