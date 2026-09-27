# OOP-184 · Section-Control-Tests für JSON-Testdaten und sicheres Aufräumen umbauen

**Typ:** Story
**Komponente:** GUI-Tests Section Control
**Priorität:** Hoch

---

## Story

**Als** Leiterin der Testautomatisierung
**möchte ich**, dass die Section-Control-Tests ihre Testdaten zuverlässig einlesen, zusätzlich Testsätze aus der CI verarbeiten und nach einem Abbruch keine Folgefehler erzeugen,
**damit** ein roter Test im Nachtlauf wieder einen echten Fehler bedeutet.

---

## Description

Die Section-Control-Tests umfassen **312 Tests in 46 Testkonfigurationen**. Alle Konfigurationen folgen dem Muster von `AbstractSectionControlTest`.

**Bestand:**

| Was | Anzahl |
|---|---|
| Testkonfigurationen mit eigenem `__post_init__` | 46 |
| davon mit fest gesetztem `data_set` | 31 |
| Aufrufe von `get_test_config()` in Helpern | 64 |
| `NumValueDTO`-Vorgabewerte in `TractorDTO` und verwandten DTOs | 31 |
| Aufrufe von `get_data_value` mit `is_bool` oder `cast_type` | 0 |

**Befund:** Die Konfigurationen teilen einen veränderlichen Vorgabewert. Ein Section-Control-Test kann dadurch mit dem Wenderadius eines anderen Testsatzes fahren. Scheitert beim Aufräumen ein Schritt, etwa das Sichern der Testdaten, entfallen Target-Cleanup und Simulationsstopp. Die Simulation lässt je Rechner nur eine Instanz zu, alle folgenden Tests scheitern dann beim Start.

**Befund zur Entstehung:** Die Konfigurationsklassen begannen 2020 als reine Datenhalter. Einlesen der Testdaten, Auswahl des Datensatzes und die globale Registrierung kamen nach und nach in `__post_init__` hinzu. Wer Zustand, Testdaten und Aufräumen verantwortet, wurde nie entschieden.

**Nicht Gegenstand:** Die Umstellung aller 46 Konfigurationen. Für dieses Ticket genügt `AbstractSectionControlTest` als Referenz, an der sich die übrigen orientieren.

## Randbedingungen

- Die Tests laufen unter Python 3.10, dem Python aus Squish 9.2.
- Die Simulation darf je Rechner nur einmal laufen.
- Die CI liefert Testsätze als JSON. Die TSV-Dateien der Fachabteilung bleiben erhalten.
- Ein Entwurf, den das Team nicht überblickt, wird nicht übernommen, auch wenn er jede denkbare Variation abdeckt.

## Akzeptanzkriterien

- **AK1** – Die Simulation wird nach jedem Test gestoppt, auch wenn der Test oder das Sichern der Testdaten mit einer Exception abbricht.
- **AK2** – Jeder Testsatz erhält die Werte aus seiner eigenen Zeile. Eine leere Spalte übernimmt keinen Wert aus einem anderen Testsatz.
- **AK3** – Ein Wert außerhalb des erlaubten Bereichs fällt beim Einlesen auf, mit Name des Testsatzes und Spalte.
- **AK4** – Einlesen und Aufbereiten der Testsätze sind ohne Squish und Target prüfbar.
- **AK5** – Testsätze aus TSV und aus JSON durchlaufen denselben Weg, ohne dass der Testablauf dafür geändert wird.
- **AK6** – Der Datensatz eines Tests lässt sich beim Erzeugen der Konfiguration wählen.
- **AK7** – Jede neu eingeführte Klasse, Funktion, jedes Protocol und jeder Context Manager ist mit einem AK oder einem Change Request begründet.
- **AK8** – Mindestens zwei Entwürfe sind verglichen, die Entscheidung ist dokumentiert.

## Hinweise

Ein `try/finally` um jeden einzelnen Cleanup-Schritt erfüllt AK1 für diesen Test, macht `test_wrapper` aber schwer lesbar. Gefragt ist eine Lösung, die der nächste Cleanup-Schritt nicht vergessen kann.

AK2 hat eine Falle: Die Vorgabewerte der DTOs sind nicht nur Vorgaben. Wer sie liest, liest unter Umständen den Wert eines anderen Testsatzes.

AK7 wird unbequem: Ein Entwurf, der jede denkbare Variation vorwegnimmt, wird nicht übernommen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche Änderung soll dieser Entwurf leichter machen – und was kostet er dafür?**

---
---

# Addendum · Wie man gewachsenen Code umbaut

## Erst markieren, dann ändern

| Kategorie | Frage an den Code |
|---|---|
| Verantwortung | Wofür ist diese Klasse zuständig, und aus welchen Gründen ändert sie sich? |
| Abhängigkeit | Was benutzt sie, ohne dass es an Konstruktor oder Signatur sichtbar ist? |
| Zustand und Lifecycle | Was wird gestartet oder geöffnet, und wer beendet es im Fehlerfall? |
| Vererbung | Ist die Unterklasse eine Spezialisierung, oder nutzt sie nur Werkzeuge? |
| Öffentliche API | Was dürfen Tests aufrufen, und was ist Detail? |
| Technische Kopplung | Wo stehen technische Details im Testablauf? |

## Change Requests als Messinstrument

Kopplung ist an einem Klassendiagramm schwer abzulesen. An einer konkreten Änderung wird sie sichtbar:

1. Change Request nehmen.
2. Alle Stellen notieren, die dafür angefasst werden müssten.
3. Für jeden Change Request wiederholen.
4. Stellen, die bei mehreren Change Requests auftauchen, sind **Hotspots**.

Ein Hotspot ist ein Ort, an dem mehrere Änderungsgründe zusammenkommen.

## Wann eine Abstraktion ihren Preis wert ist

| Sie ist es in der Regel, wenn | Sie ist es in der Regel nicht, wenn |
|---|---|
| ein Change Request sie braucht | sie „für später" eingeführt wird |
| es zwei reale Implementierungen gibt oder geben wird | es genau eine gibt und keine zweite absehbar ist |
| ein Test ohne sie nicht isoliert möglich wäre | sie nur einen Aufruf weiterreicht |
| sie einen Lebenszyklus absichert | sie Code nur anders verteilt |

## Die zwei Fragen gegen das Überrefactoren

> **Welches konkrete Problem löst diese Abstraktion?**

> **Was wäre schlechter, wenn wir sie wieder entfernen?**

Wenn auf die zweite Frage keine belastbare Antwort kommt, ist Vereinfachung meist die bessere Entscheidung.

## Vom Entwurf zur Teamregel

| Kategorie | Bedeutung |
|---|---|
| **MUST** | verbindlich |
| **SHOULD** | Standard, begründete Ausnahme möglich |
| **MAY** | zulässige Option |
| **DON'T** | bewusst vermeiden |
| **noch offen** | erkannt, aber noch nicht entschieden |

Nicht jede Erkenntnis aus einem Entwurf wird eine Regel. Eine Regel sollte begründbar sein, für den ganzen Testcode gelten und möglichst prüfbar sein.
