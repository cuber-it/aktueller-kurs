# Eine Begrüßungsfunktion schreiben

**Schwerpunkt:** Definition, Rückgabewert und Default-Parameter.

## Aufgabe

1. Schreibe `begruesse(name, gruss="Hallo")`. Die Funktion liefert den Text `Hallo Anna!` für den Namen Anna und den Standardgruß.
2. Die Funktion selbst führt keine Ausgabe aus. Gib ihren Rückgabewert im Hauptprogramm aus.
3. Zeige drei Aufrufe: nur Name, Name mit eigenem Positionsargument und Name mit dem Keyword-Argument `gruss`.

## Prüfe dein Programm

- `begruesse("Anna")` liefert `Hallo Anna!`.
- `begruesse("Ben", "Moin")` liefert `Moin Ben!`.
- `begruesse("Cem", gruss="Servus")` liefert `Servus Cem!`.
- Ein Import des Lösungsmoduls erzeugt keine Ausgabe.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 tag4/loesungen/basic/begruessung.py
```

## Referenz

- [Referenzlösung](../../loesungen/basic/begruessung.py)
