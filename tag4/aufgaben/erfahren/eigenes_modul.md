# Ein eigenes Textmodul nutzen

**Schwerpunkt:** Funktionen ohne Seiteneffekte und ein getrenntes Hauptprogramm.

## Aufgabe

1. Schreibe in `werkzeug.py` die Funktion `ist_palindrom(text)`: Vergleiche ohne Groß-/Kleinschreibung und ohne Leerraum. Ein danach leerer Text ergibt False. Andere Zeichen bleiben erhalten.
2. Schreibe dort `vokale_zaehlen(text)`: Zähle a, e, i, o, u und ä, ö, ü ohne Beachtung der Großschreibung.
3. Die beiden Funktionen liefern Werte zurück und führen keine Ausgaben aus.
4. Importiere das Modul aus `eigenes_modul.py` und gib je Beispielwort die beiden Ergebnisse aus.
5. Ein Selbsttest darf unter einer `__main__`-Bedingung stehen; er darf beim Import nicht starten.

## Prüfe dein Programm

- `Anna` ist ein Palindrom und enthält 2 Vokale.
- `Python` ist kein Palindrom und enthält 1 Vokal.
- `A n n a` wird wie `Anna` behandelt.
- Ein leerer Text ergibt False und 0; `ÄÖÜ` enthält 3 Vokale.
- `Anna!` ist nach diesem Vertrag kein Palindrom, weil das Ausrufezeichen erhalten bleibt.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 -m tag4.loesungen.erfahren.eigenes_modul
```

## Referenz

- [Textfunktionen](../../loesungen/erfahren/werkzeug.py)
- [Nutzendes Modul](../../loesungen/erfahren/eigenes_modul.py)
