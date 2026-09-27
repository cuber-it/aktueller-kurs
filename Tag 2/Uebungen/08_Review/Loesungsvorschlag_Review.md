# Lösungsvorschlag · Beibehalten, vereinfachen, ergänzen oder umbauen?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Durchgeführt für Ausschnitt K1 (Warten und Lesen in `Control`). Die Entscheidungen sind Vorschläge, das Team entscheidet.

---

## 1 · Phase 1

| Frage | Antwort |
|---|---|
| Verantwortung | auf UI-Objekte warten, sie finden, lesen, klicken |
| verwendet | `squish.waitForObject`, `waitForObjectExists`, `object.exists`, `waitFor`, Target-Helper |
| verwendet von | allen Screen Objects, Helpern, `UIElementTest`, indirekt allen Tests |
| technisches Wissen | Kontextwechsel vor jedem Zugriff, Neuverbindung bei Null-Objekt, Timeouts, Wiederholungsklick |
| Zustand, Nebenwirkungen | wechselt den aktiven Application Context, kann trennen und neu verbinden |

---

## 2 · Change Cases

| Change Case | Stellen | wo erwartet? |
|---|---|---|
| Feld erscheint 0,3 s nach dem Menü | `get_property_value` liest ohne Warten: „Found: None“ | ja, aber Verhalten falsch |
| Menü öffnet langsamer als 0,5 s | `click_and_wait` klickt erneut | ja, aber Verhalten falsch |
| Objekt in der AUT umbenannt | `get()` meldet „Found: None“ ohne Hinweis | Meldung an falscher Stelle |
| AUT-Neustart im Test | Neuverbindung in `wait`, ohne Log | ja, aber unsichtbar |

---

## 3 · Stärkster Change Case

Das langsamere Panel: betrifft 158 Aufrufe von `click_and_wait`, davon 13 auf `layout_manager_btn`, der das Panel auf- und zuschaltet. Die Coding-Regeln sichern das nur als Regel für den Aufrufer ab.

---

## 4 · Alternativen

| Befund | Alternative | Kosten |
|---|---|---|
| Wiederholungsklick | einmal klicken, dann warten; Wiederholen über `click_while_exists` | Tests mit verlorenen Klicks werden sichtbar |
| Lesen ohne Warten | `get_property_value` wartet, meldet Real Name | kurzer Lese-Timeout festlegen |
| stille Neuverbindung | Log-Eintrag | eine Zeile |

---

## 5 · Entscheidungen

| Punkt | Entscheidung | Begründung |
|---|---|---|
| Kontextwechsel im Control | beibehalten | nimmt jedem Test Arbeit ab und ist ein Ort |
| Wiederholungsklick | gezielt umbauen | belegter Fehler auf langsamer Hardware |
| Lesen ohne Warten | gezielt umbauen | irreführende Meldung, `snooze` als Ausgleich |
| Neuverbindung | ergänzen | Log-Eintrag macht sie sichtbar |

---

## 6 · Ausdrücklich beibehalten

Die Control-Schicht als einziger Ort mit Squish-Aufrufen. Kein Testfall im aktiven Bestand (983) weicht ab. Jede Änderung an der Synchronisation trifft eine Datei.

---

## 7 · Regelkandidaten

| Regel | Problem | Bereich | Ausnahme | Prüfbar | Stufe |
|---|---|---|---|---|---|
| Testfälle rufen Squish nicht direkt auf (außer begründetem `snooze`) | verteiltes Squish-Wissen | Testfälle | keine | automatisch (Suche) | MUST |
| Wiederholte Klicks nur, wenn die Schleife den geklickten Control beobachtet | Klick zu viel | Controls | keine | Review | SHOULD |
| Lesende Methoden warten und melden ein fehlendes Objekt mit Real Name | „Found: None“ | Controls | Prüfung auf Nichtvorhandensein über `exists()` | Review | SHOULD |

---

## Diskussionsanschluss

Welche Entscheidung „beibehalten“ ist Ihnen am wichtigsten, und steht sie schon irgendwo geschrieben?
