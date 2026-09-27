# Fallbeispiel · Eine Regel, die nur auf dem Prüfstand läuft

**Situationstyp:** Code wählt seine Kollaborateure selbst aus. Ohne die vollständige Umgebung lässt sich keine seiner Regeln prüfen.

---

## Ausgangslage

Eine GUI-Testsuite mit 860 Tests läuft nachts auf zwei Prüfständen mit Terminal und Testbackend; ein Lauf dauert 5 Stunden 20 Minuten. Workflows kapseln typische Abläufe. `ApplicationWorkflow` legt einen Auftrag an und prüft, ob die angezeigte Ausbringmenge der erwarteten entspricht; 74 Tests verwenden ihn.

## Wie es gewachsen ist

Der erste Workflow holte sich alles an der Stelle, an der er es brauchte: Terminalverbindung, Aufwandmenge aus dem Testbackend, HTML-Report. Auf dem Prüfstand war alles vorhanden. Später kamen ein globales Dictionary `CONFIG` und ein Singleton für das Testbackend dazu. Jeder weitere Workflow folgte demselben Muster.

## Was auffällt

**Die Mengenregel hat keine eigene Existenz.** Sie ist eine private Methode eines Workflows, der beim Aufruf das Terminal verbindet. Eine Änderung von drei Zeilen, etwa eine Mindestmenge von 5 l, ist erst im Nachtlauf prüfbar.

**Die Abhängigkeiten sind nirgends aufgeführt.** `ApplicationWorkflow()` hat einen Konstruktor ohne Parameter. Was er braucht, zeigt sich beim Lesen von `execute` oder beim Scheitern ohne Prüfstand.

**Manche Fehler haben mit der Umgebung nichts zu tun.** `round(2.675, 2)` ergibt `2.67`, `round(0.125, 2)` ergibt `0.12`. Sichtbar wird das trotzdem nur auf dem Prüfstand.

**Das Singleton macht die Reihenfolge wichtig.** Wer eine andere Aufwandmenge braucht, überschreibt `TaskService._instance` und muss es zurücksetzen.

## Naheliegende Ansätze

**`mock.patch`.** Ein Unit-Test für die Mengenregel braucht 43 Zeilen Vorbereitung für eine Assertion und bricht, wenn ein Modul verschoben wird.

**Eine zentrale Registry für Ersatzobjekte.** Austauschbar ist damit alles, sichtbar nichts: Welche Namen ein Workflow holt, steht weiter nur in seiner Implementierung.

## Diskussionsfragen

1. Das Muster funktionierte über Jahre. Ab wann wurde es ein Problem?
2. Warum löst `mock.patch` das Problem nicht, obwohl der Test grün ist?
3. Was unterscheidet eine Registry von einem Konstruktorparameter?
4. Wo haben Sie so etwas?
