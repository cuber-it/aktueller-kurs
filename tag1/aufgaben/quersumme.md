# Die Quersumme einer dreistelligen Zahl berechnen

**Schwerpunkt:** Ganzzahldivision und Restoperator.

## Grundaufgabe

Lies eine dreistellige positive ganze Zahl ein und berechne ihre Quersumme.

1. Wandle die Eingabe in eine ganze Zahl um.
2. Ermittle Hunderter-, Zehner- und Einerziffer durch Rechnen.
3. Addiere die drei Ziffern.
4. Gib die Quersumme verständlich beschriftet aus.

Verwende **keine Schleife** und gehe nicht Zeichen für Zeichen durch den Eingabestring. Auch das direkte Auslesen der einzelnen Zeichen per Index gehört nicht zu dieser Übung.

Für die Grundaufgabe darfst du Eingaben von 100 bis 999 ohne Vorzeichen und ohne führende Nullen voraussetzen.

## Prüfe dein Programm

| Eingabe | Hunderter | Zehner | Einer | Quersumme |
|---|---|---|---|---|
| 538 | 5 | 3 | 8 | 16 |
| 900 | 9 | 0 | 0 | 9 |
| 101 | 1 | 0 | 1 | 2 |
| 999 | 9 | 9 | 9 | 27 |

Die einzelnen Ziffern dienen hier zur Kontrolle. Dein Programm muss zunächst nur die Quersumme ausgeben.

## Erweiterung: Länge prüfen

Sobald du `if` kennengelernt hast, prüfe vor der Umwandlung, ob die Eingabe genau drei Zeichen lang ist. Bei einer anderen Länge gibst du eine Fehlermeldung aus und führst keine Berechnung aus.

Probiere dazu `42` und `1234`. Eine vollständige Prüfung auf gültige Ziffern ist eine spätere Erweiterung.

## Hinweis

Überlege, welche Stellen bei einer Ganzzahldivision erhalten bleiben und welche der Restoperator liefert.

**Eigene Datei:** `tag1/loesungen/quersumme.py`
