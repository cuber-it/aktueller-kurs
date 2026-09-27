# Pro und Contra · Context Manager, Zustandsprüfung und eigene Exceptions für die Testumgebung

Bewertet wird der Vorschlag aus dem Lösungspapier: `TestDatabase` und `TerminalApp` als Context Manager, die Datenbank als Konstruktorparameter, `send()` mit Zustandsprüfung, eine kleine Exception-Hierarchie unter `TestEnvironmentError` und Cleanup-Fehler als eigener Protokolleintrag neben dem ursprünglichen Fehler.

---

## Pro

**Das Aufräumen hängt nicht mehr am einzelnen Test**
Ein fehlgeschlagener Test beendet Anwendung und Datenbank, ohne dafür selbst etwas zu tun. Die Kaskade aus Nacht 1, 548 Folgefehler nach einem echten Fehler, kann auf diesem Weg nicht mehr entstehen.

**Der ursprüngliche Fehler bleibt sichtbar**
Stürzt die Anwendung ab und scheitert danach das Beenden, erscheint im Protokoll der Absturz. Der Cleanup-Fehler steht als eigener Eintrag im Log.

**Unzulässige Aufrufe scheitern dort, wo sie passieren**
`send()` ohne laufende Anwendung meldet `TerminalAppNotRunning` mit dem Befehl. Vorher lief der Test weiter und scheiterte später an einer anderen Stelle.

**Die Pflichtabhängigkeit ist am Konstruktor ablesbar**
`TerminalApp(database)` zeigt, was die Anwendung braucht. Der Zustand „erzeugt, aber noch nicht konfiguriert" existiert nicht mehr.

**Die Aufrufer können auf Fehlerarten reagieren**
Ein Timeout des Simulators lässt sich wiederholen, ein falscher Hostname nicht. Die 41 Tickets mit einer einzigen Meldung hätten sich auf drei klar benannte Ursachen verteilt.

**Die Reihenfolge des Aufräumens ergibt sich aus der Struktur**
Die verschachtelten `with`-Blöcke schließen erst die Anwendung, dann die Datenbank. Niemand muss die Reihenfolge kennen.

---

## Contra

**860 Tests müssen umgebaut werden**
Der Umbau ist mechanisch, aber er betrifft jeden Test. Die Einrückung jedes Testkörpers ändert sich, und Diffs werden groß.

**Die Verschachtelung wächst mit jeder Ressource**
Zwei `with`-Ebenen sind lesbar. Kommen Simulator, Aufzeichnung und Protokollserver dazu, entstehen fünf Ebenen. Dann braucht es `ExitStack` oder eine übergeordnete Fixture, und damit eine weitere Struktur.

**Der Cleanup-Fehler steht getrennt vom ursprünglichen Fehler**
Er steht im Log, nicht im Traceback des Tests. Wer nur den Traceback liest, sieht ihn nicht, und wer das Log nicht auswertet, ebenfalls. Der Cleanup-Fehler wäre dann erneut unsichtbar, nur auf andere Weise. Ab Python 3.11 ließe er sich mit `add_note()` direkt an die Exception hängen.

**Eine verbliebene Anwendung blockiert weiterhin den nächsten Test**
Scheitert das Beenden, wird das gemeldet, aber die Umgebung ist nicht sauber. Der Vorschlag löst die Diagnose, nicht die Isolation.

**Eigene Exceptions sind neue Klassen, die gepflegt werden**
Drei Klassen für die Verbindung zum Simulator und eine gemeinsame Basis sind überschaubar. Das Muster lädt aber dazu ein, für jede weitere Ursache eine Klasse zu ergänzen.

**`start()` und `stop()` sind nicht mehr öffentlich**
Einige Tests prüfen bewusst den Neustart der Anwendung, etwa ob Alarme nach einem Neustart erhalten bleiben. Sie brauchen eine eigene Möglichkeit, die der Vorschlag nicht vorsieht.

---

## Bewertung

Der Fall trägt den Umbau, weil **der Lebenszyklus heute in jedem Aufrufer steckt** und genau dort versagt hat: 548 Folgefehler durch ein fehlendes `stop()`, ein verdrängter Absturz durch ein `stop()` im `finally`.

Gegenprobe – *`try/finally` in allen 860 Tests, bleiben Nachteile?* Ja: Der Cleanup-Fehler verdrängt weiterhin den ursprünglichen Fehler, wie in den 64 bereits abgesicherten Tests. Jeder neue Test muss die Verschachtelung richtig wiederholen.

**Die Grenzen:**

1. **Die Protokollausgabe muss mitziehen.** Solange der Nachtlauf nur die letzte Meldung ausgibt, bleiben Protokolleinträge und Ursachenketten unsichtbar. Das ist eine Änderung am Testrunner, nicht an den Klassen.

2. **Isolation ist nicht gelöst.** Ob ein Test starten darf, wenn der vorige nicht sauber aufgeräumt hat, entscheidet der Vorschlag nicht. Dafür braucht es eine Prüfung vor dem Start.

3. **Neustart-Tests brauchen einen eigenen Weg.** Entweder eine Methode `restart()` innerhalb des Blocks oder zwei aufeinanderfolgende Blöcke. Beides ist machbar, aber noch nicht entschieden.

---

## Diskussionsfragen

1. Soll ein gescheitertes Aufräumen den restlichen Nachtlauf abbrechen, oder soll jeder Test selbst prüfen, ob die Umgebung sauber ist?
2. Wie viele `with`-Ebenen halten Sie in einem Test für lesbar? Was tun Sie darüber hinaus?
3. Würden Sie die Datenbank und die Anwendung in einer gemeinsamen Fixture zusammenfassen? Was verlieren Sie dabei?
4. Welche eigenen Exceptions braucht Ihre Testumgebung tatsächlich – gemessen daran, wer sie fängt?
5. Wo verwenden Sie heute `except Exception`, und was geht dort verloren?
