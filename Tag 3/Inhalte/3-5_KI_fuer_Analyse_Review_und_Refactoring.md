# 3-5 · KI für Analyse, Review & Refactoring

Der Nutzen eines Coding Agents endet nicht bei der Erzeugung neuen Testcodes. Gerade in gewachsenen Testsuiten kann KI vorhandene Strukturen untersuchen, Auffälligkeiten sichtbar machen und Änderungen vorbereiten. Dabei liefert sie **Analyseergebnisse und Änderungsvorschläge**, keine automatisch gültigen Architekturentscheidungen.

- **Strukturanalyse** – Claude Code kann Abhängigkeiten, wiederkehrende Strukturen und die Nutzung gemeinsamer Testkomponenten über mehrere Dateien hinweg untersuchen.
- **Duplikate** – Wiederholte Abläufe, ähnliche Testdaten oder mehrfach implementierte UI-Interaktionen können Hinweise auf fehlende oder inkonsistent genutzte Abstraktionen sein.
- **Test-Smells** – Lange Tests, technische Details im Testfall, feste Wartezeiten, versteckte Abhängigkeiten oder schwer nachvollziehbare Assertions können systematisch gesucht und zur Diskussion gestellt werden.
- **Architekturverletzungen** – Direkte Squish-Zugriffe außerhalb vereinbarter Schichten, umgangene Domain APIs oder neue Parallelstrukturen lassen sich gegen explizite Projektregeln prüfen.
- **Konsistenzprüfung** – Page und Component Objects, Tasks, Naming, Fehlerbehandlung und Testdatenstrukturen können projektweit auf unterschiedliche Lösungsvarianten untersucht werden.
- **Refactoring-Vorschläge** – KI kann mögliche Extraktionen, Zusammenführungen oder Verschiebungen von Verantwortlichkeiten vorschlagen und Änderungen über mehrere Dateien vorbereiten. Der Nutzen muss gegen zusätzliche Abstraktion und Änderungsrisiko abgewogen werden.
- **Anforderung gegen Tests** – Anforderungen oder strukturierte Szenarien können mit vorhandenen Tests verglichen werden. Daraus können Hinweise auf fehlende, redundante oder nicht mehr passende Tests entstehen.
- **Standardbasierter Review** – Explizite Python-, OO- und Squish-Regeln aus Tag 1 und Tag 2 liefern konkrete Review-Kriterien. Dadurch wird aus einer allgemeinen Einschätzung eine Prüfung gegen den vereinbarten Projektstandard.
- **Deterministische Prüfungen zuerst** – Formatierung, Linting, Typprüfung und andere objektiv automatisierbare Regeln sollten weiterhin durch dafür geeignete Werkzeuge geprüft werden. KI ergänzt diese Prüfungen dort, wo Kontext und Entwurfsurteil erforderlich sind.
- **Fachliches Urteil** – Ob ein Test fachlich notwendig, ein erwartetes Ergebnis korrekt oder ein Risiko ausreichend abgedeckt ist, lässt sich nicht allein aus Codequalität ableiten.

## Leitgedanke

KI kann eine große Testsuite als zusammenhängendes System untersuchen und dadurch Reviews und Refactorings unterstützen. Verlässlich wird diese Unterstützung erst, wenn **explizite Projektregeln und überprüfbare technische Kriterien** als Maßstab dienen.

> **Merksatz:** Der Projektstandard ist die Review-Grundlage – nicht der Geschmack des Modells.
