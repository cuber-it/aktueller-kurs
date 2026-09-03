# 2-1 · Vom strategischen zum taktischen Design

Tag 1 hat Grenzen gezogen: Wo gilt welches Modell, welche Sprache, welche Beziehung zu den Nachbarn. **Innerhalb** einer solchen Grenze wird jetzt gebaut.

Das taktische Design liefert die Bausteine dafür. Sie sind keine Vorschrift, sondern ein Vokabular für wiederkehrende Entwurfsfragen — vor allem für die eine: **Was muss zusammen gültig bleiben?**

- **Taktisches Design** – Der Bau des Modells innerhalb eines Bounded Context; Bausteine, Regeln, Zuständigkeiten.
- **Voraussetzung** – Eine Kontextgrenze. Ohne sie ist unklar, für welchen Zweck modelliert wird.
- **Entity** – Etwas mit Identität über die Zeit; bleibt dasselbe, auch wenn sich alle Merkmale ändern.
- **Value Object** – Etwas, das durch seine Werte bestimmt ist; zwei mit gleichen Werten sind austauschbar.
- **Aggregate** – Eine Klammer um mehrere Dinge, die gemeinsam gültig bleiben müssen.
- **Domain Event** – Etwas fachlich Bedeutsames, das geschehen ist; Grundlage für Entkopplung.
- **Repository** – Der Zugang zu Aggregaten; verbirgt, woher sie kommen.
- **Domain Service** – Fachlogik, die zu keinem einzelnen Ding gehört.
- **Kein Baukasten** – Nicht jedes Modell braucht alle Bausteine. Wer sie durchgängig anwendet, baut Struktur ohne Anlass.
- **Die Leitfrage des Tages** – Was muss **zusammen** gültig bleiben, und was darf auseinanderlaufen?
- **Konsistenz kostet** – Was gemeinsam gültig bleiben muss, muss gemeinsam geändert werden. Das begrenzt Nebenläufigkeit und Verteilbarkeit.
- **Was Tag 1 vorgibt** – Die Sprache des Kontextes ist die Sprache des Modells. Wer hier neue Begriffe erfindet, hebt die Arbeit von Tag 1 auf.
- **Grenzen der Bausteine** – Sie beantworten Entwurfsfragen, keine fachlichen. Ob eine Regel gilt, entscheidet der Fachbereich.
