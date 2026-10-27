# Ein Schaltjahr erkennen

**Schwerpunkt:** Restoperator, Vergleiche und logische Verknüpfungen.

## Aufgabe

Lies ein Jahr als ganze Zahl ein und gib aus, ob es nach den Regeln des gregorianischen Kalenders ein Schaltjahr ist.

Es gelten diese Regeln:

- Ein durch 4 teilbares Jahr ist grundsätzlich ein Schaltjahr.
- Durch 100 teilbare Jahre sind davon ausgenommen.
- Durch 400 teilbare Jahre sind trotzdem Schaltjahre.

Verknüpfe die Regeln zu einem Wahrheitswert. Verwende dafür **keine Verzweigung** mit `if`, `elif` oder `else` und auch keinen bedingten Ausdruck.

Gib das eingegebene Jahr und das Ergebnis als `True` oder `False` aus. Du darfst eine gültige positive Jahreszahl voraussetzen.

## Prüfe dein Programm

| Jahr | Erwartetes Ergebnis | Grund |
|---|---|---|
| 2023 | False | Nicht durch 4 teilbar |
| 2024 | True | Durch 4, aber nicht durch 100 teilbar |
| 1900 | False | Durch 100, aber nicht durch 400 teilbar |
| 2000 | True | Durch 400 teilbar |
| 2100 | False | Durch 100, aber nicht durch 400 teilbar |

## Zweite Variante

Berechne die drei Teilbedingungen zunächst in einzeln benannten Variablen. Verknüpfe anschließend diese Variablen zum Ergebnis.

Vergleiche beide Varianten: Liefern sie dieselben Ergebnisse? Bei welcher kannst du die fachlichen Regeln leichter wiederfinden?

**Eigene Datei:** `tag1/loesungen/schaltjahr.py`
