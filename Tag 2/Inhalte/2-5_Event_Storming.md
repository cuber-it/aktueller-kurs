# 2-5 · Event Storming

Event Storming ist eine **Werkstattmethode**, um eine Domäne gemeinsam zu erheben — mit Fachbereich und Entwicklung an einer Wand, in wenigen Stunden statt in Wochen von Interviews.

Der Einstieg ist bewusst niedrig: Man beginnt mit dem, was **geschehen ist**, weil Fachleute darüber von selbst erzählen. Modellbegriffe kommen später.

- **Ausgangspunkt** – Ereignisse in der Vergangenheitsform, auf orangen Zetteln: „Fahrzeug wurde zurückgenommen".
- **Zeitachse** – Die Ereignisse werden von links nach rechts geordnet. Lücken und Doppelungen fallen dabei auf.
- **Command** – Was ein Ereignis auslöst, auf blauen Zetteln: „Fahrzeug zurücknehmen".
- **Akteur** – Wer den Command auslöst, auf kleinen gelben Zetteln.
- **Aggregate** – Wo Commands verarbeitet und Ereignisse erzeugt werden, auf hellgelben Zetteln. Sie entstehen erst spät.
- **Hotspot** – Streitpunkte und offene Fragen, auf roten Zetteln. Sie sind das wertvollste Ergebnis.
- **Read Model** – Was jemand sehen muss, um zu entscheiden, auf grünen Zetteln.
- **Externes System** – Beteiligte außerhalb, auf rosa Zetteln.
- **Die Farben sind Konvention** – Sie variieren je nach Quelle. Wichtig ist, dass sie im Raum einheitlich verwendet werden.
- **Big Picture, Process Level, Design Level** – Drei Detailstufen. Der Überblick zuerst, Einzelheiten später und nur wo nötig.
- **Was es leistet** – Gemeinsames Verständnis, aufgedeckte Widersprüche, Kandidaten für Kontextgrenzen und Aggregate.
- **Was es nicht leistet** – Es ersetzt keinen Entwurf. Das Ergebnis ist Rohmaterial, kein Modell.
- **Voraussetzung** – Die Leute, die es wissen, müssen im Raum sein. Ohne Fachbereich ist es eine Entwicklerrunde mit Zetteln.
- **Online** – Machbar, aber schwächer: Die Gleichzeitigkeit vieler Hände an einer Wand ist der Kern der Methode.
