# Fallbeispiel · Eine Hilfsklasse für alles

**Situationstyp:** Eine zentrale Klasse nimmt auf, was keinen eigenen Ort hat. Änderungen in einem Bereich können Tests in einem anderen Bereich treffen.

---

## Ausgangslage

Eine Testsuite für die Terminal-Oberfläche prüft die Freischaltung des Servicemenüs, Einstellungen für Anbaugeräte, Teilbreiten und Überlappung sowie Berichte. 2018 entstand eine Klasse `ImplementTestHelper` mit `unlock_service_menu`, `enter_section` und `load_config`, damit nicht jeder Test die Freischaltung selbst ausprogrammiert.

## Wie es gewachsen ist

Was mehr als ein Test brauchte, kam in diese Klasse: Screenshots im Fehlerfall, HTML-Bericht, Zurücksetzen der Datenbank, `compute_expected_working_width`. Seit 2022 arbeiten drei Teams (Terminal-Bedienung, Section Control, Berichte) an ihr. Heute: 1.870 Zeilen, 94 Methoden, 412 Tests nutzen sie.

Daneben entstand ein Datenobjekt `Implement` mit öffentlichen Attributen `sections`, `working_width_cm`, `status`, `saved_at`, die Testdaten-Builder direkt setzen.

## Was auffällt

**Die Klasse hat keine Verantwortung, die sich in einem Satz sagen lässt.** „Für alles, was Tests brauchen.“

**Berichte und Freischaltung hängen an derselben Methode.** `load_config()` liefert die Berichtseinstellungen und die PIN für das Servicemenü. Eine Änderung für Berichte ändert die Quelle der PIN.

**Drei Teams ändern dieselbe Datei aus verschiedenen Gründen.** Von 61 Commits im letzten Halbjahr endeten 17 in einem Merge-Konflikt.

**Das Anbaugerät hat Zustand, aber keine Regeln.** `status = "saved"` lässt sich ohne `saved_at` setzen; welche Kombination gültig ist, steht nirgends.

**Dieselbe Rechnung steht an vier Stellen.** Die Breite einer Teilbreite ist im Reporting, in zwei Buildern und im Helper ausprogrammiert.

**Tests treffen Entscheidungen, die dem Terminal gehören.** Vor jedem Schalten einer Teilbreite prüfen Tests `terminal.state` und `terminal.implement`. Ein neuer Zustand betrifft 63 Tests.

## Naheliegende Ansätze

**Die Datei nach Zeilen in vier Dateien mit Mixins aufteilen.** Weniger Merge-Konflikte, die gemeinsame Abhängigkeit von `load_config` bleibt.

**Eine Validierungsfunktion vor dem Export.** Ungültige Anbaugeräte fallen beim Export auf, nicht beim Erzeugen.

## Diskussionsfragen

1. Jede Ergänzung war einzeln sinnvoll. Wann hätte jemand eingreifen sollen?
2. Warum löst die Aufteilung in vier Dateien die Abhängigkeit zwischen Berichten und Freischaltung nicht?
3. Warum reicht eine Validierung vor dem Export nicht?
4. Wo haben Sie so etwas?
