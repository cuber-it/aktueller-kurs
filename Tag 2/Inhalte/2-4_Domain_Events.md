# 2-4 · Domain Events

Ein Domain Event ist **etwas fachlich Bedeutsames, das geschehen ist**. Es wird gemeldet, nicht angeordnet — und wer darauf reagiert, entscheidet der Empfänger.

Damit lösen sich zwei Probleme aus 2-3: Was nicht im selben Aggregate liegt, wird über Ereignisse nachgezogen. Und was ein anderer Kontext braucht, holt er sich, statt dass der Sender ihn kennt.

- **Domain Event** – Eine Tatsache aus der Fachwelt, in der Vergangenheit formuliert: „Fahrzeug wurde zurückgenommen".
- **Fachlich, nicht technisch** – Ein Ereignis, das ein Fachvertreter benennen würde. „Datensatz gespeichert" ist keines.
- **Command gegen Event** – Ein Command **fordert** etwas und kann abgelehnt werden. Ein Event **berichtet** und ist nicht verhandelbar.
- **Unveränderlich** – Was geschehen ist, ändert sich nicht. Ein Ereignis wird nicht korrigiert, sondern durch ein neues richtiggestellt.
- **Der Sender kennt die Empfänger nicht** – Er meldet. Wer es braucht, hört zu. Sonst muss der Sender bei jedem neuen Empfänger geändert werden.
- **Konsistenz über Grenzen** – Was nicht sofort stimmen muss, wird über Ereignisse nachgezogen. Zwischen den Aggregaten ist die Welt kurz widersprüchlich.
- **Reihenfolge und Zeitpunkt** – Ereignisse kommen an, aber nicht notwendig sofort und nicht notwendig in Reihenfolge. Das gehört bedacht.
- **Häufiger Fehler** – Ereignisse als Aufforderung formulieren: „Rechnung erstellen" ist ein Command. „Vorgang abgeschlossen" ist ein Event.
- **Zweiter Fehler** – Zu viele Ereignisse. Jede Zustandsänderung zu melden erzeugt Lärm; gemeldet wird, was fachlich bedeutsam ist.
- **Dritter Fehler** – Der Sender wartet auf eine Antwort. Dann ist es kein Ereignis, sondern ein verkleideter Aufruf.
- **Ereignisse als Gesprächsmittel** – Sie sind das, was Fachbereiche von selbst erzählen. Deshalb eignen sie sich zur Modellerhebung.
- **Der Preis** – Der Ablauf ist nicht mehr an einer Stelle ablesbar. Wer wann worauf reagiert, muss dokumentiert werden.
