# Pro und Contra · Schnitt nach Änderungsgründen und Anbaugeräte mit Verhalten

Bewertet wird der Vorschlag aus dem Lösungspapier: `ImplementTestHelper` in sechs Module nach Änderungsgründen aufgeteilt, `Implement` mit berechneter Arbeitsbreite und abgeleitetem Speicherzustand, die Bereitschaftsprüfung in `Terminal.switch_section`, die Breite einer Teilbreite in `Section.width_cm`.

---

## Pro

**Abhängigkeiten werden sichtbar**
Wer für den JSON-Bericht die Konfiguration umstellt, ändert `configuration.py`, ein Modul mit genau dieser Aufgabe. Dass dort auch die PIN der Freischaltung liegt, ist beim Öffnen der Datei erkennbar. Im Helper war diese Abhängigkeit zwischen 94 Methoden verborgen.

**Jede Klasse hat einen Satz**
Wer eine Datei öffnet, weiß, wofür sie zuständig ist. Neue Methoden haben einen erkennbaren Ort statt „irgendwo im Helper".

**Weniger Konflikte zwischen Teams**
Das Team Berichte arbeitet in `reporting.py`, das Team Terminal-Bedienung in `service_menu.py` und `implement_page.py`. Die 17 Merge-Konflikte je Halbjahr entstanden, weil alle in derselben Datei arbeiteten.

**Ungültige Anbaugeräte entstehen nicht mehr**
Ein Gerät kann nicht gespeichert sein, ohne einen Zeitpunkt zu haben, und seine Arbeitsbreite kann nicht veralten. Die 14 Abbrüche im Export haben keine Ursache mehr.

**Neue Zustände des Terminals betreffen keine Tests**
Kommt ein Zustand wie „Straßenfahrt" hinzu, ändert sich `Terminal.switch_section`. Vorher waren es 63 Tests.

**Die Breitenregel steht an einer Stelle**
D6 ändert `Section.width_cm`. Reporting, Builder und Anbaugerät folgen automatisch.

---

## Contra

**Sechs Module statt einer Klasse**
Ein Test, der das Servicemenü freischaltet, eine Teilbreite einstellt und einen Bericht schreibt, braucht jetzt Objekte aus vier Modulen. Wie er sie bekommt, ist noch nicht gelöst.

**Die Umstellung berührt 412 Tests**
Jeder Test, der `ImplementTestHelper` verwendet, ändert seine Importe und Aufrufe. Bei drei Teams, die parallel arbeiten, ist das ein Vorhaben über mehrere Wochen.

**Builder verlieren Freiheit**
Ein Builder, der gezielt ein inkonsistentes Anbaugerät erzeugen wollte, um die Fehlerbehandlung des Terminals zu testen, kann das nicht mehr. Solche Fälle brauchen einen eigenen, ausdrücklich benannten Weg.

**Exceptions statt stiller Zustände**
`switch_section` wirft jetzt `TerminalNotReadyError`, wo vorher der Test entschied, nicht zu schalten. Tests, die bisher still übersprungen haben, schlagen nun fehl, bis sie angepasst sind.

**Die Grenze zwischen Freischaltung und Geräteeinstellung ist eine Entscheidung**
Beide bedienen das Terminal. Sie zu trennen ist mit D2 begründet. Kommt D2 nicht, war die Trennung ein Schnitt für eine Änderung, die nicht eintrat.

**Zentimeter als `int` statt Meter als `float`**
Die Umstellung der Längen ist sachlich sinnvoll, vergrößert aber den Umbau um ein Thema, das mit Verantwortung nichts zu tun hat. Außerdem zeigt das Terminal Meter an, die Umrechnung muss an der Oberfläche stattfinden.

---

## Bewertung

Der Fall trägt den Schnitt, weil **die Änderungsgründe belegt sind**: Sechs angekündigte Änderungen von vier verschiedenen Stellen, eine Methode, deren Änderung einen fremden Bereich trifft, und 17 Merge-Konflikte in einem Halbjahr.

Gegenprobe – *`ImplementTestHelper` bleibt, nur `load_config` wird in eine Konfiguration für Berichte und eine für die Freischaltung geteilt, bleiben Nachteile?* Ja: Die gemeinsame Abhängigkeit von `load_config` wäre behoben, aber D1 bis D6 würden weiterhin dieselbe Datei ändern, und die Teams würden weiter in einer Klasse arbeiten. Die Regeln für Anbaugeräte wären davon unberührt.

**Die Grenzen:**

1. **Die Zusammenarbeit der neuen Teile ist offen.** Der Schnitt sagt, wer wofür zuständig ist. Wie ein Test die Teile erhält, ob über eine Basisklasse, über Komposition oder als Parameter, ist nicht entschieden.

2. **Nicht jede Gruppe ist gleich stabil.** Freischaltung und Geräteeinstellung könnten sich als eine Verantwortung herausstellen, wenn sich die Oberfläche anders entwickelt als angekündigt.

3. **Inkonsistente Testdaten können gewollt sein.** Für Negativtests braucht es einen ausdrücklichen Weg, ein fehlerhaftes Anbaugerät zu erzeugen. Der Vorschlag sieht keinen vor.

---

## Diskussionsfragen

1. Würden Sie Freischaltung und Geräteeinstellung trennen, solange D2 nur angekündigt ist?
2. Wie erzeugen Sie für einen Negativtest ein Anbaugerät, das die Regeln verletzt?
3. Ab welcher Zahl von Aufrufern behandeln Sie Testcode wie eine Bibliothek?
4. `TerminalNotReadyError` macht still übersprungene Schaltvorgänge sichtbar. Ist das in jedem Test gewollt?
5. Welche Klasse in Ihrem Testcode würde auf die Frage nach ihrer Verantwortung mit einer Aufzählung antworten?
