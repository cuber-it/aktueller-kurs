# Fallbeispiel · Aufräumen als Aufgabe jedes Tests

**Situationstyp:** Ein Objekt wird gestartet und muss wieder beendet werden. Das Beenden ist Aufgabe jedes einzelnen Aufrufers.

---

## Ausgangslage

Tests für eine Terminal-Anwendung brauchen eine Testdatenbank mit definiertem Maschinenzustand und eine laufende Instanz der Anwendung. Die Anwendung darf je Rechner nur einmal laufen, weil sie einen festen Port für die CAN-Anbindung belegt.

## Wie es gewachsen ist

Zwei Klassen, `TestDatabase` und `TerminalApp`, haben Methoden zum Öffnen und Schließen. Die Regel im Wiki: „Wer `start()` aufruft, ruft am Ende `stop()` auf.“ Neue Tests entstehen durch Kopieren. Heute beginnen und enden 860 Tests nach diesem Muster. Eine Hilfsfunktion für die ECU-Simulation fängt jede Exception und liefert `False`, damit sie keine Tests abbricht.

## Was auffällt

**Das Aufräumen hängt an jedem einzelnen Test.** Schlägt eine Prüfung fehl, wird `stop()` nicht erreicht. Jeder folgende Test scheitert am Start einer zweiten Instanz, und im Protokoll steht ein echter Fehler zwischen vielen Folgefehlern.

**`send()` funktioniert auch ohne gestartete Anwendung.** Ein Test ohne `start()` schickt Befehle an die Prozess-ID `None` und scheitert mit einer irreführenden Meldung.

**Zwischen Konstruktor und `configure()` ist die Anwendung unvollständig.** Fehlt `configure()`, bricht `start()` mit `AttributeError: 'NoneType' object has no attribute 'connection'` ab.

**„Simulator nicht erreichbar“ hat drei Ursachen.** Überlastung, nicht gestarteter Simulator, falscher Hostname. Die Hilfsfunktion meldet alle drei gleich.

## Naheliegende Ansätze

**`try/finally` in einzelnen Tests.** Stürzt die Anwendung ab, schlägt im `finally` `stop()` mit `ProcessLookupError` fehl. Im Protokoll steht dann dieser Fehler, der Absturz nicht.

**Ein Aufräumskript vor dem Nachtlauf.** Hilft beim Start des Laufs, nicht zwischen zwei Tests.

## Diskussionsfragen

1. Die Regel im Wiki ist richtig. Warum wirkt sie nicht zuverlässig?
2. Ein falscher Fehler statt vieler Folgefehler: Ist das ein Fortschritt?
3. Warum ist `return False` in einer „robusten“ Hilfsfunktion naheliegend?
4. Wo haben Sie so etwas?
