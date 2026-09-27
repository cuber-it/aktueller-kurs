# 3-8 · Agentischer Squish-Workflow

Ein agentischer Testworkflow verbindet Testanalyse, Projektkontext, Codeänderung, Werkzeugnutzung und reale Testausführung zu einem **geschlossenen Arbeitszyklus**. Der Agent erhält damit Rückmeldung darüber, ob seine vorherige Änderung tatsächlich zum erwarteten Ergebnis geführt hat.

- **Ausgangspunkt** – Eine Anforderung oder Änderung wird zunächst analysiert. Relevante Szenarien und erwartetes Verhalten werden bestimmt, bevor Testcode verändert wird.
- **Strukturierte Testabsicht** – Gherkin oder eine vergleichbare Intermediate Representation kann die zu prüfenden Szenarien explizit machen und einen Review-Punkt vor der Implementierung schaffen.
- **Architekturkonforme Implementierung** – Der Agent untersucht vorhandene Tests und Abstraktionen und implementiert die Änderung innerhalb der vereinbarten Squish-/Python-Architektur.
- **Werkzeuggestützte Ausführung** – Über definierte Tools kann der Agent den relevanten Test oder eine Testsuite ausführen, ohne dafür uneingeschränkten Zugriff auf die gesamte Umgebung zu benötigen.
- **Beobachtung** – Testergebnis, Fehlermeldungen und relevante Logs bilden die Evidenz für den nächsten Schritt. Der Agent muss zwischen Fehlern im Test, Fehlern der Umgebung und möglichem Fehlverhalten der AUT unterscheiden können.
- **Korrekturschleife** – Eine fehlgeschlagene Ausführung kann zu erneuter Analyse und einer gezielten Änderung führen. Anschließend wird erneut ausgeführt und verifiziert.
- **Closed Loop** – Erst wenn Ergebnisse aus der realen Ausführung wieder in Analyse und Änderung zurückgeführt werden, entsteht ein geschlossener agentischer Workflow. Reine Codegenerierung bleibt ein Open Loop.
- **Stop Conditions** – Schleifen benötigen explizite Abbruchbedingungen, beispielsweise maximale Versuche, nicht klassifizierbare Fehler oder Änderungen außerhalb des erlaubten Bereichs.
- **Human Checkpoints** – Fachliche Entscheidungen, größere Architekturänderungen, unerwartete AUT-Befunde oder sicherheitsrelevante Aktionen können eine menschliche Freigabe erfordern.
- **Nachvollziehbarkeit** – Änderungen, ausgeführte Tests, Ergebnisse und Korrekturen müssen rekonstruierbar bleiben. Autonomie ersetzt weder Diagnosefähigkeit noch reproduzierbare Testausführung.

## Leitgedanke

Agentische Testautomatisierung entsteht durch die **Rückkopplung zwischen Änderung und realer Ausführung**. Der Agent darf dabei nur so autonom handeln, wie Beobachtbarkeit, Werkzeuggrenzen und Kontrollmechanismen eine verlässliche Überprüfung erlauben.

> **Merksatz:** Aus Testgenerierung wird Test Engineering, wenn Ausführung und Ergebnis wieder in den Arbeitsprozess zurückfließen.
