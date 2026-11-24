# Eine Kontaktliste verwalten

**Schwerpunkt:** Verschachtelte Daten und ein einfaches Befehlsmenü.

## Aufgabe

1. Speichere Kontakte als Liste von Dictionaries mit `name`, `vorname`, `telefon`, `plz`, `ort` und `strasse`.
2. Biete die Befehle `n` für neu, `f` für Suche, `d` für Löschen, `p` für Anzeigen und `x` für Ende an.
3. Ein neuer Kontakt braucht alle sechs Felder. Rand-Leerraum wird entfernt; eine Telefonnummer darf nur einmal vorkommen.
4. Suche anhand des vollständigen Nachnamens und der Postleitzahl. Der Name wird ohne Beachtung der Großschreibung verglichen. Zeige alle Treffer.
5. Lösche anhand der Telefonnummer nur nach Bestätigung mit `j`.
6. Die Grundaufgabe verwaltet Daten im Speicher; beim Beenden endet die Sitzung.

## Prüfe dein Programm

- Leere Pflichtfelder und doppelte Telefonnummern werden abgewiesen.
- Mehrere Kontakte mit demselben Nachnamen und derselben PLZ werden bei der Suche gemeinsam angezeigt.
- Ein `n` bei der Löschbestätigung erhält den Kontakt.
- Eine unbekannte Telefonnummer oder ein unbekannter Befehl beendet das Programm nicht.
- Nach bestätigtem Löschen erscheint der Kontakt nicht mehr in der Anzeige.

## Erweiterung

- Ergänze ein ausdrücklich gewähltes Dateiformat zum Speichern und Laden, beispielsweise JSON.

## Referenz

- [Referenzlösung](../../loesungen/erfahren/rolodex.py)
