# Die Lottobude in Funktionen aufteilen

**Schwerpunkt:** Eingabeprüfung, Berechnung und Ausgabe trennen.

## Aufgabe

1. Schreibe `pruefe_tipp(text)`: Der Text enthält sechs durch Leerraum getrennte Zahlen. Liefere eine sortierte Liste mit sechs verschiedenen ganzen Zahlen aus 1 bis 49.
2. Bei falscher Anzahl, nicht ganzzahligen Angaben, Dubletten oder ungültigem Wertebereich entsteht `ValueError` mit einer verständlichen Meldung.
3. Schreibe `ziehe_zahlen()` für sechs zufällige, verschiedene und sortierte Zahlen aus demselben Bereich.
4. Schreibe `ermittle_treffer(tipp, ziehung)` für den sortierten Schnitt zweier bereits gültiger Zahlenfolgen.
5. Das Hauptprogramm liest einen Tipp, behandelt Eingabefehler und gibt Tipp, Ziehung, richtige Zahlen und Trefferzahl aus.

## Prüfe dein Programm

- `1 7 13 22 38 49` ist gültig; zusätzliche Leerzeichen sind erlaubt.
- Fünf Zahlen, ein doppelter Wert, 0, 50 und ein Text wie `abc` sind ungültig.
- Bei Tipp `[1, 2, 3, 4, 5, 6]` und Ziehung `[4, 5, 6, 7, 8, 9]` werden `[4, 5, 6]` geliefert.
- Die Prüf- und Vergleichsfunktionen lesen keine Eingaben und führen keine Ausgaben aus.
- Ein fehlerhafter Tipp führt zu einer Meldung und beendet diesen Lauf kontrolliert.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 tag4/loesungen/basic/lottobude.py
```

## Referenz

- [Referenzlösung](../../loesungen/basic/lottobude.py)
