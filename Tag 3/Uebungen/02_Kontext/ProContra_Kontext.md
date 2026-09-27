# Pro und Contra · Befunde nach Ort einordnen, wenig in den Skill

Bewertet wird der Vorschlag aus dem Lösungspapier: B1 und B3 in den Skill, übergangsweise und mit Ablaufbedingung; B2, B4, B5 nicht.

---

## Pro

**Der Skill bleibt klein**
Zwei Einträge statt fünf. Jede Zeile kostet bei jedem Aufruf.

**Keine erfundenen Methoden**
B4 wartet, bis `go_back()` existiert.

**Framework-Fehler werden dort behoben, wo sie wirken**
B2 und B5 betreffen auch handgeschriebene Tests.

**Ablaufbedingungen**
Einträge verschwinden, wenn ihr Anlass behoben ist.

---

## Contra

**Übergangszeit**
Bis B1 im Framework behoben ist, hängt der Schutz am Modell.

**Ablaufbedingungen müssen jemandem auffallen**
Niemand liest den Skill, wenn ein Ticket geschlossen wird.

**Teilhinweise gibt es schon**
Für B1 und B2 stehen im Skill bereits Hinweise, die den Befund nur teilweise abdecken. Ergänzen oder ersetzen muss jemand bewusst entscheiden.

---

## Bewertung

Der Vorschlag trägt, weil **er die eigenen Kontextregeln des Teams anwendet**, die aus eigener Erfahrung mit veralteten Beschreibungen entstanden sind.

Gegenprobe – *alle fünf Befunde als Abschnitt in den Skill, bleiben Nachteile?* Ja: Fünf Beschreibungen, die veralten, eine davon zu einer Methode, die es nicht gibt.

**Die Grenzen:**

1. **Ablaufbedingung mit Ticket.** Der Eintrag nennt das Ticket, dessen Abschluss ihn überflüssig macht.
2. **B2 ergänzen.** Der vorhandene Hinweis „not reentrant“ bekommt den Zusatz zur Exception, bis das Framework `try/finally` hat.
3. **Framework-Tickets anlegen**, sonst bleibt der Übergang dauerhaft.

---

## Diskussionsfragen

1. Welcher Befund gehört Ihrer Meinung nach doch in den Skill?
2. Wie stellen Sie sicher, dass Ablaufbedingungen beachtet werden?
3. Soll `check_references.py` auch Ablaufbedingungen prüfen?
4. Wer entscheidet, ob ein Befund ins Framework oder in den Skill geht?
