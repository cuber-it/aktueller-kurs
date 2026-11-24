# Kursdaten mit Funktionsbausteinen auswerten

**Schwerpunkt:** Ein vorhandenes Modul verwenden und einen Ablauf strukturieren.

## Aufgabe

1. Verwende die fertige Bibliothek `tag4/data_source.py` und die vorhandene `materialien/HistoricalQuotes.csv`.
2. Lade die Daten, speichere sie mit `save_sql()` in `tag4/ausgabe/quotes.db` und lies sie mit `load_sql()` zurück. Vergleiche die vollständigen Datensätze.
3. Schreibe `erstelle_bericht(daten)`: Liefere Anzahl, Zeitraum, höchsten und niedrigsten Schlusskurs, Mittelwert und prozentuale Änderung vom ersten zum letzten Handelstag als Dictionary.
4. Die Berichtsfunktion verändert ihre Eingabe nicht und führt keinen Dateizugriff und keine Ausgabe aus. Leere Daten werden mit `ValueError` abgewiesen.
5. Das Hauptprogramm speichert den Bericht als `tag4/ausgabe/kursbericht.json`. Formatiere Kennzahlen erst bei der Konsolenausgabe.
6. Bereite die benötigten Ausgabedateien selbst vor; eine bereits vorhandene Datenbank ist keine Voraussetzung.

## Prüfe dein Programm

- Die Beispieldatei enthält 2.517 Datensätze.
- Der aufsteigende Zeitraum reicht von 2010-06-03 bis 2020-06-02.
- Höchster Schlusskurs: 327.2000; niedrigster Schlusskurs: 34.2757; Mittelwert in der Anzeige: 121.19.
- CSV und Datenbank liefern nach Datum sortiert dieselben Daten.
- Ein zweiter Lauf erzeugt keine zusätzlichen Datensätze.
- Ein leerer Datensatzbestand führt nicht zu erfundenen Kennzahlen.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 -m tag4.loesungen.erfahren.kursanalyse
```

## Referenz

- [Referenzlösung](../../loesungen/erfahren/kursanalyse.py)
- [Verwendete Bibliothek](../../data_source.py)
