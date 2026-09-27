# TA-201 · Architekturübersicht des Testframeworks erstellen

**Typ:** Story
**Komponente:** Testframework
**Priorität:** Mittel

---

## Story

**Als** neues Mitglied im Testautomatisierungsteam
**möchte ich** wissen, welche Schicht des Testframeworks welches Wissen trägt,
**damit** ich eine Änderung an der Stelle vornehme, an der sie hingehört.

---

## Description

Das Testframework ist über mehrere Jahre gewachsen. Eine Beschreibung seiner Schichten gibt es nicht. Neue Kolleginnen und Kollegen lernen die Struktur aus dem Code und aus Gesprächen.

**Bestand:**

| Was | Anzahl |
|---|---|
| Testfälle (`test.py`), ohne die als veraltet markierten Suiten | 983 |
| Testsuiten, ohne die als veraltet markierten | 16 |
| UI-Module in `UI/` | 10 |
| Zeilen in `UI/controls.py` | 1.975 |
| Helper-Module in `helper/ui_test_modules/` | 5 |
| Testfälle mit direktem Squish-Aufruf außer `snooze` | 0 |

**Befund:** Ändert die AUT einen `objectName`, meldet der Test „did not become accessible within … milliseconds“. Die Meldung passt zu einem Timing-Problem ebenso wie zu einem geänderten Namen. Wer nicht weiß, dass Real Names nur im UI-Modul stehen, sucht im Testfall.

**Befund zur Entstehung:** Die Schichten sind sauber getrennt, ihre Aufgaben aber nirgends beschrieben. Wer die Konvention nicht kennt, sucht an der falschen Stelle.

**Nicht Gegenstand:** Änderungen am Framework. Dieses Ticket beschreibt den Bestand.

## Randbedingungen

- Die Übersicht soll auf eine Seite passen.
- Sie wird später auch Claude Code als Projektkontext bereitgestellt (Tag 3).
- Bewertungen gehören in ein eigenes Ticket, nicht in die Übersicht.

## Akzeptanzkriterien

- **AK1** – Jede Schicht ist mit Verzeichnis, typischer Klasse und Verantwortung in einem Satz beschrieben.
- **AK2** – Für fünf typische Änderungen (Real Name, Menüstruktur, Anwendungsname, Target-Typ, Synchronisation) ist benannt, welche Schicht sie betrifft.
- **AK3** – Wissen, das eine Schicht versteckt übernimmt (Kontextwechsel, Neuverbindung, Wartezeiten), ist aufgeführt.
- **AK4** – Die Übersicht enthält keine Bewertung und keinen Umbauvorschlag.

## Hinweise

Eine Liste der Verzeichnisse erfüllt AK1 nicht. Gefragt ist die Verantwortung.

AK3 wird unbequem: Manche Aufgaben erledigt eine Schicht, ohne dass ihr Name darauf hinweist. `Control.wait()` wechselt den Application Context.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche Änderung würde genau in dieser Schicht landen?**

---
---

# Addendum · Woran man eine Schicht erkennt

## Drei Fragen je Baustein

| Frage | Beispiel `Control` |
|---|---|
| Was weiß er? | Real Name, Anzeigename, Anwendungsname, Timeouts |
| Was tut er? | warten, klicken, lesen, Kontext wechseln |
| Welche Änderung landet hier? | neues Squish-Verhalten, anderes Warten, neue Bedienart |

## Notwendige und vermeidbare Kopplung

Ein GUI-Test hängt zwangsläufig von Squish, AUT und Oberfläche ab. Die Frage ist, ob dieses Wissen an wenigen Stellen liegt oder über viele Tests verteilt ist.

| Kopplung | notwendig, wenn | vermeidbar, wenn |
|---|---|---|
| an Real Names | sie an einem Ort stehen | sie in Testfällen wiederholt werden |
| an Menüwege | ein Helper sie kapselt | jeder Test den Weg selbst geht |
| an Wartezeiten | eine abfragbare Bedingung fehlt | ein Zustand abfragbar wäre |
| an Squish | in Controls | in Testfällen |

## Beobachten vor Bewerten

Ein einzelner Ausschnitt erlaubt kein Urteil über die gesamte Architektur. Erst beschreiben, dann an Änderungen messen, dann bewerten.
