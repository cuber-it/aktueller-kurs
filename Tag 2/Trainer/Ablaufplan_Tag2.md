# Ablaufplan Tag 2 · Taktisches Design

**Kurszeit:** 09:00–12:00 und 13:00–16:30/17:00
**Sieben Einheiten à 50 Minuten**

---

## Der Plan

| Zeit | ID | Einheit | Übung |
|---|---|---|---|
| 09:00–09:45 | 2-1 | Vom strategischen zum taktischen Design | — |
| 09:45–09:55 | | *Pause* | |
| 09:55–10:45 | 2-2 | Entity und Value Object | Entity oder Wert |
| 10:45–10:55 | | *Pause* | |
| 10:55–11:55 | 2-3 | Aggregate und Konsistenzgrenze | Konsistenzgrenzen ziehen |
| 11:55–12:00 | | Zwischenstand | |
| **12:00–13:00** | | **Mittag** | |
| 13:00–13:50 | 2-4 | Domain Events | Command oder Event |
| 13:50–14:00 | | *Pause* | |
| 14:00–14:45 | 2-5 | Event Storming | gemeinsamer Durchlauf |
| 14:45–15:05 | | *Pause* | |
| 15:05–15:55 | 2-6 | Architektur und Implementierung | Zuordnung der Bausteine |
| 15:55–16:05 | | *Pause* | |
| 16:05–17:00 | 2-7 | Legacy und Evolution, **Kursabschluss** | Ablöseweg entwerfen |

**Zwei Abweichungen vom Gleichtakt:**

**2-1 ist auf 45 Minuten gekürzt.** Der Puffer geht an 2-3.

**2-3 bekommt 60 Minuten.** Die Konsistenzgrenze ist die schwierigste Entscheidung des Tages; die Einheit überzieht erfahrungsgemäß.

**2-7 bekommt 55 Minuten**, davon 15 für den Kursabschluss mit den Transferfragen.

---

## Einheitsablauf

Für 2-2 bis 2-4 und 2-6 bis 2-7:

| Schritt | Minuten |
|---|---|
| Einstieg, Kernbegriffe | 10 |
| Fallbeispiel lesen lassen | 10 |
| Kurz andiskutieren | 5 |
| Übung | 15 |
| Auswertung | 10 |

**2-5 Event Storming** weicht ab: 8 Minuten Methode, 25 Minuten Durchlauf, 12 Minuten Auswertung.

---

## Zeitprobleme und was dann

### Wenn es zu schnell geht

| Vorrat | Wo | Kostet |
|---|---|---|
| **Diskussionsfragen aus ProContra** | jedes Paket, 5 Fragen am Ende | 10–15 min |
| **„Wo haben Sie so etwas?"** | nach jedem Fallbeispiel | 5–10 min |
| **Die Ärgernisse aus Tag 1** | in 1-1 gesammelt, hier aufgreifen | beliebig |
| **Der Preis-Abschnitt** | jedes ProContra | 10 min |
| **Event Storming vertiefen** | Process Level statt nur Big Picture | 20 min |

**Der wirksamste Vorrat an Tag 2:** die eigenen Ärgernisse vom Vortag. Bei 2-3 und 2-7 lassen sie sich direkt anwenden.

### Wenn es zu langsam geht

| Streichen | Verlust |
|---|---|
| 2-6 Übung, nur die zwei Abgrenzungen erklären | gering |
| 2-2 Übung kürzen: nur die ersten fünf Fälle | gering |
| 2-5 Event Storming auf 25 Minuten kürzen | mittel — die Methode braucht den Durchlauf |
| 2-7 Übung streichen, nur Vorgehen erklären | mittel |

**Nicht streichen:** 2-3 und der Kursabschluss in 2-7.

**2-3 nicht**, weil die Konsistenzgrenze der Kern des taktischen Designs ist.
**Den Abschluss nicht**, weil die Transferfragen die einzige belastbare Rückmeldung liefern.

---

## Der Übergang von Tag 1

**In 2-1, erste zehn Minuten.** Nicht dozieren, sondern fragen:

> „Was war gestern die wichtigste Erkenntnis für Sie?"

Falls die Rückmeldefrage vom Vortag gestellt wurde („Welchen Begriff würden Sie als Erstes überprüfen?"), hier darauf zurückkommen.

**Die Vorbedingung aussprechen:** Taktisches Design ohne Kontextgrenze ist sinnlos. Damit ist klar, warum Tag 1 vorher kam.

---

## Der rote Faden

Eine Frage trägt von 2-1 bis 2-4:

> **Was muss zusammen gültig bleiben, und was darf auseinanderlaufen?**

| Einheit | Beitrag |
|---|---|
| 2-1 | setzt die Frage |
| 2-2 | liefert die Dinge, die geklammert werden |
| 2-3 | beantwortet: was zusammen muss |
| 2-4 | beantwortet: wie das Getrennte zusammenkommt |

Wer diesen Zusammenhang ausspricht, macht aus vier Bausteinen eine Argumentationskette.

---

## Online-Besonderheiten

| Was | Wie |
|---|---|
| Lesephasen | Kameras aus anbieten, Zeit ansagen, Zähler stellen |
| **Event Storming (2-5)** | **Board vorher einrichten**, Farben vorbelegen, nicht im Termin |
| Sammeln beim Event Storming | erst still und einzeln, dann gemeinsam ordnen |
| Aggregatgrenzen (2-3) | Modell als Liste zeigen, Gruppen markieren lassen |
| Auswertung | einen Teilnehmer vorstellen lassen |

**Beim Event Storming:** Wenn kein Whiteboard verfügbar ist, als geteilte Liste durchführen. Zeitachse wird zur Reihenfolge, Farben zu Präfixen. Schwächer, aber die Schritte bleiben nachvollziehbar.

---

## Der Kursabschluss

Die letzten fünfzehn Minuten von 2-7. Drei Fragen, jede einzeln beantworten lassen:

> „Was würden Sie nächste Woche als Erstes tun?"

> „Wo sind Sie unsicher geblieben?"

> „Was hätten Sie weggelassen?"

**Antworten notieren.** Sie sind die Grundlage für die nächste Durchführung.

**Nicht tun:** überziehen, neue Themen anschneiden, alle Bausteine zusammenfassen.

---

## Materialübersicht je Einheit

| Einheit | Inhalt | Trainer | Übungspaket |
|---|---|---|---|
| 2-1 | 2-1_Vom_strategischen_zum_taktischen_Design | 2-1_Trainer_… | — |
| 2-2 | 2-2_Entity_und_Value_Object | 2-2_Trainer_… | 01_EntityValueObject |
| 2-3 | 2-3_Aggregate_und_Konsistenzgrenze | 2-3_Trainer_… | 02_Aggregate |
| 2-4 | 2-4_Domain_Events | 2-4_Trainer_… | 03_DomainEvents |
| 2-5 | 2-5_Event_Storming | 2-5_Trainer_… | 04_EventStorming |
| 2-6 | 2-6_Architektur_und_Implementierung | 2-6_Trainer_… | 05_Architektur |
| 2-7 | 2-7_Legacy_und_Evolution | 2-7_Trainer_… | 06_Legacy |
