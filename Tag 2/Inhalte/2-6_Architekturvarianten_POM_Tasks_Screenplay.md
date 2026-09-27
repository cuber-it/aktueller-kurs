# 2-6 · Architekturvarianten: POM, Tasks, Screenplay & direkte Tests

Testautomatisierung lässt sich unterschiedlich strukturieren. Die Varianten sind **Werkzeuge für unterschiedliche Probleme und keine Reifegrade**.

- **Direkter Testcode** – Transparent und kostengünstig, solange technische Details lokal bleiben und Änderungen nicht viele Tests gleichzeitig treffen.
- **Page / Screen Object** – Bündelt Wissen über UI-Bereiche hinter einer stabileren Schnittstelle.
- **Component Object** – Modelliert eigenständig wiederverwendbare oder veränderliche UI-Komponenten.
- **Task Layer** – Kapselt wiederkehrende Abläufe oberhalb einzelner UI-Bereiche.
- **Screenplay** – Strukturiert Testhandlungen über Actor, Task und Interaction und verschiebt den Fokus von UI-Strukturen auf Fähigkeiten und Aufgaben.
- **Hybrid** – Reale Testsysteme können mehrere Ansätze gezielt kombinieren.
- **Kosten** – Jede zusätzliche Ebene erzeugt Indirektion, Lernaufwand und möglicherweise Boilerplate.
- **Evolution statt Migration** – Ein Konzept kann gezielt an einer Problemstelle ergänzt werden, ohne die gesamte Architektur umzustellen.
- **Entscheidung** – Relevant ist, welche Änderung oder welches Fehlerbild ein anderer Ansatz konkret besser beherrscht.

## Leitgedanke

Ein bekanntes Pattern ist nicht automatisch besser als eine projektspezifische Lösung. Sein Nutzen muss sich an einem konkreten Problem zeigen.

> **Merksatz:** Architekturvarianten sind Werkzeuge – keine Reifegrade. Entscheidend ist das Problem, das sie besser lösen sollen.
