# 2-3 · Aggregate und Konsistenzgrenze

Ein Aggregate ist eine **Klammer um Dinge, die gemeinsam gültig bleiben müssen**. Innerhalb der Klammer gilt eine Regel immer; über die Klammer hinweg darf sie zeitweise verletzt sein.

Die Frage lautet nicht „was gehört sachlich zusammen", sondern: **Was muss im selben Moment stimmen?**

- **Aggregate** – Eine Gruppe von Entities und Value Objects, die eine gemeinsame Regel einhalten müssen.
- **Invariante** – Die Regel, die immer gelten muss. Sie ist der Grund für die Klammer — ohne Invariante kein Aggregate.
- **Aggregate Root** – Die eine Entity, über die zugegriffen wird. Nur sie ist von außen ansprechbar.
- **Zugriffsregel** – Von außen wird nur die Wurzel angesprochen. Was innen liegt, wird über sie geändert.
- **Konsistenzgrenze** – Innerhalb: die Regel gilt sofort und immer. Außerhalb: sie darf zeitweise verletzt sein und wird nachgezogen.
- **Sofort oder später** – Die entscheidende Entwurfsfrage. Was sofort stimmen muss, gehört ins selbe Aggregate; alles andere nicht.
- **Klein halten** – Große Aggregate sind schwer zu ändern, sperren viel und behindern gleichzeitiges Arbeiten. Im Zweifel kleiner schneiden.
- **Verweise statt Verschachtelung** – Ein Aggregate verweist auf andere über deren Identität, statt sie zu enthalten.
- **Eine Änderung, ein Aggregate** – Wer in einem Vorgang mehrere Aggregate ändert, hat vermutlich falsch geschnitten oder braucht ein Domain Event.
- **Häufiger Fehler** – Nach Datenzugehörigkeit schneiden statt nach Regel. „Gehört zum Vertrag" ist kein Grund; „muss mit dem Vertrag zusammen stimmen" schon.
- **Zweiter Fehler** – Alles ins selbe Aggregate, weil es bequem ist. Das Ergebnis sperrt bei jeder Änderung halbe Bestände.
- **Der Preis** – Zwischen Aggregaten ist die Welt zeitweise widersprüchlich. Das muss fachlich vertretbar sein — und ist es meistens.
