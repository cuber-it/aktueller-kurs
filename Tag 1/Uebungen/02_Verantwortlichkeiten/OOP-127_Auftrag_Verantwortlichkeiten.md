# OOP-127 · Verantwortlichkeiten im Testcode der Geräteeinstellungen nach Änderungsgründen schneiden

**Typ:** Story
**Komponente:** Testframework Geräteeinstellungen
**Priorität:** Hoch

---

## Story

**Als** Entwickler im Testautomatisierungsteam
**möchte ich**, dass eine Änderung am Berichtswesen nur Code berührt, der für Berichte zuständig ist,
**damit** eine Anpassung in einem Bereich nicht Tests in einem anderen Bereich scheitern lässt.

---

## Description

Die Tests der Geräteeinstellungen nutzen eine zentrale Klasse `ImplementTestHelper`. Sie ist seit 2018 gewachsen.

**Bestand:**

| Was | Anzahl |
|---|---|
| Zeilen in `implement_test_helper.py` | 1.870 |
| Methoden in `ImplementTestHelper` | 94 |
| Tests, die `ImplementTestHelper` verwenden | 412 |
| Commits auf die Datei im letzten Halbjahr | 61 |
| davon mit Merge-Konflikt | 17 |
| Teams, die an der Datei arbeiten | 3 |

**Befund:** Berichtskonfiguration und Freischaltung des Servicemenüs lesen über dieselbe Methode `load_config()`. Wer für den JSON-Bericht das Format der Konfigurationsdatei ändert, ändert zugleich die Quelle der PIN, von der fast alle Tests abhängen.

**Zweiter Befund:** Der Export der Testergebnisse brach bei 14 Anbaugeräten ab. Testdaten-Builder hatten `implement.status = "saved"` gesetzt, ohne `saved_at` zu füllen.

**Dritter Befund:** Der Berechnungsweg für die Breite einer Teilbreite steht an vier Stellen: im Reporting, in zwei Testdaten-Buildern und im Helper. Für die angekündigte Überlappung je Teilbreite müssten alle vier geändert werden.

**Nicht Gegenstand:** Wie die neuen Klassen zusammengesetzt und an Tests übergeben werden. Das folgt in eigenen Tickets.

## Randbedingungen

- 412 Tests dürfen während der Umstellung nicht dauerhaft rot sein. Ein schrittweiser Übergang ist zulässig.
- Drei Teams arbeiten parallel an Tests für Terminal-Bedienung, Section Control und Berichte.
- Im nächsten Halbjahr sind sechs Änderungen angekündigt (Lizenzstick, Statusleiste statt Bestätigungsdialog, JSON-Bericht, Konfiguration aus Umgebungsvariablen, Datenbank-Reset per REST, Überlappung je Teilbreite).

## Akzeptanzkriterien

- **AK1** – Für jede der sechs angekündigten Änderungen ist benannt, welche Klasse oder welches Modul sie betrifft. Keine Änderung betrifft mehr als einen Verantwortungsbereich.
- **AK2** – Für jede neue Klasse lässt sich die Verantwortung in einem Satz ohne Aufzählung nennen.
- **AK3** – Ein Anbaugerät kann nicht als gespeichert gelten, ohne einen Speicherzeitpunkt zu haben.
- **AK4** – Die Arbeitsbreite eines Anbaugeräts kann nicht von der Summe seiner Teilbreiten abweichen.
- **AK5** – Tests entscheiden nicht anhand interner Zustände des Terminals, ob eine Aktion zulässig ist.
- **AK6** – Der Berechnungsweg für die Breite einer Teilbreite steht an genau einer Stelle.

## Hinweise

`ImplementTestHelper` in `ImplementTestHelper1` bis `ImplementTestHelper4` aufzuteilen erfüllt AK2 nicht. Eine Aufteilung nach Dateigröße ist keine Aufteilung nach Verantwortung.

AK3 und AK4 werden nicht dadurch erfüllt, dass die Attribute einen Unterstrich bekommen. Die Builder würden dann `_status` setzen.

AK5 heißt nicht, dass Tests keine Zustände mehr abfragen dürfen. Eine Prüfung fragt zwangsläufig nach Zustand.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Wofür ist dieses Objekt verantwortlich – und welche Änderung sollte genau hier stattfinden?**

---
---

# Addendum · Woran man falsch geschnittene Verantwortung erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Namen ohne Aufgabe | `Helper`, `Utils`, `Manager`, `Common` |
| Methoden, die sich nicht gegenseitig brauchen | `unlock_service_menu` und `write_html_report` in derselben Klasse |
| Zustand, den jeder setzen kann | `implement.status = "saved"` |
| Gespeicherte Werte, die sich aus anderen ableiten lassen | `working_width_cm` neben `sections` |
| Entscheidungen außerhalb des Objekts | `if terminal.state == "ready": terminal.switch_section(...)` |
| Methoden, die fast nur fremde Daten verwenden | `section_width(section)` im `ReportWriter` |

## In der Zusammenarbeit

| Signal | Konkret |
|---|---|
| Viele Merge-Konflikte in einer Datei | 17 von 61 Commits |
| Mehrere Teams ändern dieselbe Klasse aus verschiedenen Gründen | Terminal-Bedienung, Section Control, Berichte |
| Eine Änderung bricht Tests in einem fremden Bereich | Berichtskonfiguration bricht Freischaltung |
| Dieselbe Rechnung steht an mehreren Stellen | Breite einer Teilbreite viermal |

## Die Änderungsfrage

Nicht: „Was macht diese Klasse alles?"

Sondern:

1. **Welche Ereignisse würden diese Klasse ändern?**
2. **Ändert dasselbe Ereignis auch den Rest der Klasse?**
3. **Wer würde die Änderung anstoßen?**

Wenn verschiedene Stellen im Unternehmen Änderungen an derselben Klasse auslösen, trägt sie mehr als eine Verantwortung.

## Was Kapselung schützt

Kapselung schützt nicht Attribute, sondern **Regeln über Zustand**. Ein Anbaugerät ist gespeichert genau dann, wenn es einen Speicherzeitpunkt hat. Diese Regel lässt sich nur halten, wenn es genau einen Weg gibt, ein Anbaugerät zu speichern.

Der Unterstrich sagt, worauf fremder Code sich nicht verlassen soll. Welche Zustandsänderungen gültig sind, sagt erst eine Methode wie `save()`.

## Wann eine Sammelklasse vertretbar ist

Eine Hilfsklasse oder ein Hilfsmodul ist nicht automatisch ein Problem. Vertretbar ist sie in der Regel, wenn

- alle Funktionen dieselbe Art von Aufgabe erledigen, etwa Textformatierung,
- sie keinen gemeinsamen Zustand braucht,
- dieselben Ereignisse sie ändern.

Problematisch wird sie, wenn sie der Ort ist, an dem alles landet, was keinen anderen Ort hat.
