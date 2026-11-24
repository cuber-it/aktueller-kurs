# Ein Telefonbuch ergänzen

**Schwerpunkt:** Dictionary-Zugriff und fehlende Schlüssel.

## Aufgabe

1. Beginne mit den Beispielkontakten `anna: 0151-111` und `ben: 0151-222`. Telefonnummern sind Strings.
2. Frage einen Namen ab. Ignoriere Rand-Leerraum und Groß-/Kleinschreibung; melde einen fehlenden Namen verständlich.
3. Frage nach einem neuen Namen. Enter beendet diesen Schritt. Ein vorhandener Name wird nicht überschrieben.
4. Lies für einen neuen Namen eine nicht leere Telefonnummer ein. Gib anschließend das Telefonbuch nach Namen sortiert aus.

## Prüfe dein Programm

- Die Suche nach ` Anna ` findet `0151-111`.
- Ein unbekannter Name löst keinen KeyError aus.
- Ein neuer Kontakt `cem` mit `0123` behält die führende Null.
- Ein vorhandener Kontakt oder eine leere Nummer verändert das Telefonbuch nicht.

## Referenz

- [Referenzlösung](../../loesungen/basic/telefonbuch.py)
