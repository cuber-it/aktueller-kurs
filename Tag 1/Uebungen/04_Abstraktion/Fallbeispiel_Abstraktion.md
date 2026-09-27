# Fallbeispiel · Eine abstrakte Basisklasse je Komponente

**Situationstyp:** Eine Schnittstelle wird für alle denkbaren Fälle entworfen. Jede Implementierung liefert Methoden, die ihr Nutzer nie aufruft, und jede Erweiterung trifft alle, die davon erben.

---

## Ausgangslage

Eine Lagerverwaltung für Logistikzentren wird mit 1.480 GUI-Tests in Python geprüft. Ergebnisse gehen nach jedem Lauf an vier Kanäle: Konsole, Datei, Mail, Teams-Kanal.

## Wie es gewachsen ist

2020 kam die Regel „Jede Komponente bekommt eine abstrakte Basisklasse“, nachdem ein Wechsel des Mailservers zwei Wochen Nacharbeit gekostet hatte. `Notifier` bekam vier abstrakte Methoden: `connect`, `send`, `send_attachment`, `disconnect`. Die Konsole braucht nur `send` und hat für die übrigen drei leere Rümpfe. Nach demselben Muster entstand `UiDriver` mit neun Methoden; heute gibt es 14 Test-Doubles dafür.

## Was auffällt

**Die Aufrufer brauchen fast nichts.** Drei Klassen verwenden einen `Notifier`, alle nur `send()`. Von 20 Methodenrümpfen der vier Kanäle enthalten 11 nur `pass` oder `raise NotImplementedError`.

**Erweiterungen treffen Unbeteiligte.** Sieben Test-Doubles in Modulen anderer Teams erben von `Notifier`. Eine neue abstrakte Methode macht sie nicht mehr instanziierbar.

**Die Test-Doubles sind größer als ihr Zweck.** Die 14 Fakes für `UiDriver` implementieren 126 Methoden, aufgerufen werden 38.

**Eine passende fremde Klasse passt nicht.** Ein Chat-Client mit `send(message)` braucht einen Adapter mit fünf Methoden, vier davon leer.

**Einige Abstraktionen haben nie eine zweite Implementierung.** Sechs ABCs haben genau eine Unterklasse.

**Type Hints gelten als Absicherung.** Ein Type Checker läuft in der CI nicht.

## Naheliegende Ansätze

**„Bei Änderungen an ABCs alle Unterklassen suchen.“** Test-Doubles in Modulen anderer Teams tauchen bei einer Suche im Framework-Repository nicht auf.

**Standard-Implementierungen in der ABC.** Welche Methoden Pflicht sind, lässt sich danach nur noch am Quelltext ablesen.

## Diskussionsfragen

1. Die Regel hatte einen berechtigten Anlass. Wie hätte sie lauten müssen?
2. Warum trifft eine neue Methode in `Notifier` Klassen, die sie nie aufrufen?
3. Was würde sich mit einem Protocol statt einer ABC ändern?
4. Wo haben Sie so etwas?
