# 3-1 · Bestandsaufnahme: Claude Code im Testprozess

Claude Code wird bereits zur Entwicklung und Änderung von Squish-Tests eingesetzt. Für den weiteren Ausbau steht deshalb nicht die Codegenerierung selbst im Mittelpunkt, sondern die Frage, **welche Rolle ein Coding Agent im Testentwicklungsprozess übernimmt, welche Informationen er dafür benötigt und wo seine technischen Grenzen liegen**.

- **Coding Agent** – Claude Code arbeitet nicht nur mit einem einzelnen Prompt, sondern kann Projektdateien lesen, Zusammenhänge im Repository untersuchen und Änderungen über mehrere Dateien hinweg durchführen. Damit arbeitet die KI innerhalb eines vorhandenen Softwaresystems statt ausschließlich einzelnen Code zu erzeugen.
- **Arbeitskontext** – Das Modell kennt ein Projekt nicht automatisch. Seine Entscheidungen basieren auf dem Kontext, der ihm durch Aufgabenbeschreibung, gelesene Dateien, Projektregeln, Beispiele und weitere bereitgestellte Informationen zur Verfügung steht.
- **Repository-Zugriff** – Zugriff auf den Quellcode ermöglicht es, vorhandene Tests, Hilfsfunktionen, Abstraktionen und Konventionen zu berücksichtigen. Repository-Zugriff bedeutet jedoch noch keinen Zugriff auf die laufende Anwendung oder die tatsächliche Testausführung.
- **Analyse vor Änderung** – Ein Coding Agent kann vor einer Implementierung relevante Dateien suchen, vorhandene Strukturen untersuchen und Abhängigkeiten erkennen. Die Qualität einer Änderung hängt deshalb auch davon ab, ob vor der Generierung die richtige Umgebung analysiert wurde.
- **Projektkonforme Änderung** – Neuer Testcode muss sich in bestehende Python- und Squish-Strukturen einfügen. Technisch lauffähiger Code kann trotzdem Architekturregeln, Namenskonventionen oder vorhandene Abstraktionen umgehen.
- **Verifikation** – Eine erzeugte Änderung ist zunächst eine Hypothese darüber, wie die Aufgabe gelöst werden kann. Statische Prüfungen, Reviews und insbesondere die reale Testausführung entscheiden, ob diese Hypothese trägt.
- **Tool-Nutzung** – Coding Agents können verfügbare Werkzeuge verwenden, um Informationen zu beschaffen oder Aktionen auszuführen. Welche Teile des Testprozesses erreichbar sind, hängt damit wesentlich von den bereitgestellten Werkzeugen und deren Schnittstellen ab.
- **Feedback Loop** – Ergebnisse aus Testausführung, Logs und Fehlermeldungen werden für die nächste Analyse benötigt. Ohne eine technische Rückführung dieser Informationen endet der automatisierte KI-Workflow vor der eigentlichen Testausführung.
- **Human Control** – Fachliche Erwartungen, Architekturentscheidungen und Freigaben bleiben explizite Verantwortlichkeiten. Der sinnvolle Grad der Automatisierung hängt davon ab, welche Entscheidungen zuverlässig überprüfbar sind und welche menschliches Urteil benötigen.

## Leitgedanke

Der heutige Einsatz von Claude Code ist der Ausgangspunkt für einen weitergehenden Test-Engineering-Workflow. Entscheidend ist, **welchen Kontext der Agent besitzt, welche Teile des Systems er beobachten und verändern kann und wie Ergebnisse aus Verifikation und Testausführung wieder in seine Arbeit zurückfließen**.

> **Merksatz:** Wir optimieren nicht den Prompt, sondern den gesamten Testentwicklungsprozess.
