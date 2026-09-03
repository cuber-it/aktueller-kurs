# AV-2412 · Zuständigkeit des Kontextes Anmietung beschreiben

**Typ:** Story
**Komponente:** Fachliche Architektur
**Priorität:** Mittel
**Verweist auf:** AV-2398 (Workshop Zuständigkeit, ohne Ergebnis beendet)

---

## Story

**Als** Product Owner
**möchte ich** bei einer neuen Anforderung entscheiden können, ob sie in meinen Kontext gehört,
**damit** die Zuordnung nicht bei jeder Anforderung neu ausgehandelt wird.

---

## Description

Der Kontext **Anmietung** umfasst inzwischen 14 Aufgaben. Er hat **41 Prozent** aller offenen Tickets bei einem Viertel der Entwickler; die Durchlaufzeit liegt beim Dreifachen der übrigen Kontexte.

**Bei der letzten Quartalsplanung** konnten 3 von 11 Anforderungen nicht zugeordnet werden.

**Der Klärungsworkshop (AV-2398)** endete ohne Ergebnis. Von 14 Aufgaben blieben 6 strittig. Die Diskussion vermischte vier verschiedene Kriterien:

| Kriterium | Beispiel |
|---|---|
| Wo passiert es? | Schadensaufnahme geschieht an der Station |
| Wer braucht das Ergebnis? | Schadensdaten braucht Fakturierung und Werkstatt |
| Wer hat es gebaut? | Anmietung, weil damals Kapazität da war |
| Was gehört fachlich zusammen? | blieb unklar |

**Ein neuer Entwickler** fragte nach zwei Wochen, wofür der Kontext zuständig sei. Die Antwort „alles, was am Tresen passiert" trägt nicht — die Verfügbarkeitsanzeige der Webseite gehört ebenfalls dazu.

**Nicht Gegenstand:** Eine Aufteilung des Kontextes. Zunächst geht es um die Beschreibung des Ist-Zustands und der fachlichen Klammer.

## Randbedingungen

- 14 Aufgaben, davon 6 strittig
- 6 Entwickler, ein Product Owner
- Beziehungen zu allen drei übrigen Kontexten und zum Partnernetzwerk
- Die Einarbeitung eines neuen Entwicklers dauerte zuletzt vier Monate

## Akzeptanzkriterien

- **AK1** – Der Zweck des Kontextes ist in einem Satz benannt, ohne Aufzählung.
- **AK2** – Es ist festgehalten, welche fachlichen Entscheidungen dieser Kontext trifft — und welche er von anderen übernimmt.
- **AK3** – Für jede Aufgabe ist begründet, warum sie hierher gehört. Die Begründung nennt die fachliche Klammer, nicht die Historie.
- **AK4** – Es ist benannt, was **nicht** in diesen Kontext gehört, mit Angabe, wohin es gehört.
- **AK5** – Die Begriffe des Kontextes sind aufgeführt (Verweis auf das Glossar genügt).
- **AK6** – Ein- und ausgehende Information ist benannt, mit dem jeweiligen Gegenüber.
- **AK7** – Für die 6 strittigen Aufgaben ist entschieden oder der Konflikt ausdrücklich als offen ausgewiesen, mit Kriterium für die spätere Entscheidung.
- **AK8** – Die Beschreibung passt auf eine Seite.
- **AK9** – Ein neuer Entwickler kann anhand der Beschreibung sagen, ob eine gegebene Anforderung in den Kontext gehört.

## Hinweise

AK1 ist der schwierigste Punkt. „Alles, was am Tresen passiert" ist kein Zweck, sondern ein Ort. Ein Zweck beantwortet, **welches fachliche Ergebnis** dieser Kontext verantwortet.

AK4 ist genauso wichtig wie AK3. Eine Zuständigkeit ohne Abgrenzung wächst.

AK7 lässt bewusst zu, dass etwas offen bleibt — aber nicht, dass es unbenannt bleibt.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Wofür ist dieser Kontext verantwortlich — und wofür ausdrücklich nicht?**

---
---

# Addendum · Der Bounded Context Canvas

Ein Arbeitsblatt zur Beschreibung eines Kontextes, entwickelt von der DDD Crew. Es zwingt dazu, Fragen zu beantworten, die sonst unausgesprochen bleiben.

## Die Felder

| Feld | Frage | Warum es hilft |
|---|---|---|
| **Name** | Wie heißt der Kontext? | Der Name sollte den Zweck andeuten, nicht den Ort |
| **Zweck** | Welches fachliche Ergebnis verantwortet er? | Ein Satz. Zwingt zur Klammer |
| **Strategische Einordnung** | Core, Supporting oder Generic? | Bestimmt, wie viel Aufwand gerechtfertigt ist |
| **Fachliche Entscheidungen** | Was entscheidet dieser Kontext selbst? | Trennt Eigenverantwortung von Zulieferung |
| **Ubiquitous Language** | Welche Begriffe gelten hier? | Verweis auf das Glossar |
| **Eingehende Nachrichten** | Was kommt herein, von wem? | Macht Abhängigkeiten sichtbar |
| **Ausgehende Nachrichten** | Was geht hinaus, an wen? | Zeigt, wer von diesem Kontext abhängt |
| **Nicht zuständig für** | Was gehört ausdrücklich nicht hierher? | Verhindert Wachstum durch Zweifel |

Das letzte Feld ist eine Ergänzung, die der Katalog nicht vorsieht — sie hat sich in der Praxis als das nützlichste erwiesen.

## Warum ein Canvas und keine Prosa

**Die Felder sind Fragen, die man sonst nicht stellt.** „Welche fachlichen Entscheidungen trifft dieser Kontext?" wird selten gefragt — und ist die Frage, die eine Zuständigkeit begründet.

**Der Platz ist begrenzt.** Ein Kontext, dessen Zweck nicht in einen Satz passt, ist vermutlich zu groß. Das Canvas macht das sichtbar.

**Es ist vergleichbar.** Vier Canvas nebeneinander zeigen Lücken und Überschneidungen, die in vier Prosatexten unsichtbar blieben.

## Die vier Kriterien, die man auseinanderhalten muss

Im Workshop AV-2398 wurden sie vermischt. Sie sind alle relevant, aber nicht gleichrangig:

| Kriterium | Gewicht |
|---|---|
| **Was gehört fachlich zusammen?** | entscheidend |
| Welche Begriffe teilen sich die Aufgaben? | starkes Indiz für Zusammengehörigkeit |
| Wer braucht das Ergebnis? | schwach — Empfänger begründen keine Zuständigkeit |
| Wo passiert es? | schwach — der Ort ist nicht die Fachlichkeit |
| Wer hat es gebaut? | **kein Kriterium** — nur Historie |

**Die Prüffrage:** Würde eine Änderung an dieser Aufgabe auch die übrigen Aufgaben des Kontextes betreffen? Dann gehört sie dazu. Wenn nicht, ist sie nur dort gelandet.
