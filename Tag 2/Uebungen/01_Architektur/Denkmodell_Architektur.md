# Denkmodell · Eine bestehende Testarchitektur sichtbar machen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Testfälle rufen Squish nicht direkt auf | keiner von 983 Testfällen, abgesehen von `snooze` |
| Real Names stehen in Klassen, nicht in Tests | `SubMenuGNSSSource.sae_j1939_btn` |
| Funktionen mit fachlichen Namen fassen Wege zusammen | `open_gnss_source_submenu()` |
| Eine Methode tut mehr, als ihr Name sagt | `Control.wait()` wechselt den Application Context |
| Wartezeiten stehen in Tests oder Helpern | `snooze_time=8`, `squish.snooze(1)` |
| Modul-Singletons unter Kurznamen | `masetth`, `setth`, `uih` |

### Im Team

| Signal | Konkret |
|---|---|
| Neue Kolleginnen und Kollegen fragen, wo etwas hingehört | „Wo stehen die Objektnamen?“ |
| Fehler werden in der falschen Schicht gesucht | Wartezeit im Test statt Real Name im UI-Modul |
| Wissen über Konventionen ist mündlich | „Das macht man bei uns so“ |

---

## Stufe 2 · Erkenntnisse

**1. Eine Architektur existiert auch ohne Diagramm.**
Sie steckt in der Aufteilung des Codes. Sichtbar wird sie, wenn man fragt, welche Änderung wo landet.

**2. Namen von Verzeichnissen sind keine Verantwortung.**
`helper/` kann Wege, Prüfungen und Datenlogik enthalten. Die Frage ist, was eine Datei weiß und tut.

**3. Versteckte Aufgaben sind der teuerste Teil einer Architektur.**
Was eine Schicht zusätzlich erledigt, etwa den Kontext wechseln, fehlt in jeder Fehlersuche, die es nicht kennt.

**4. Kopplung ist nicht das Problem, verteilte Kopplung ist es.**
Ein GUI-Test muss von Squish und AUT abhängen. Entscheidend ist, an wie vielen Stellen.

**Was gesucht wird:** für jede Schicht die Verantwortung und die Änderungen, die dort landen.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Landkarte der Schichten** | neue Teammitglieder oder Werkzeuge die Struktur kennen müssen |
| **Tabelle Änderung → Schicht** | Änderungen regelmäßig an der falschen Stelle landen |
| **Liste versteckter Aufgaben** | Fehlersuchen lange dauern, weil eine Schicht mehr tut als erwartet |
| **Nichts aufschreiben** | das Team klein und stabil ist und niemand neu hinzukommt |

---

## Stufe 4 · Entscheidung

### Frage 1 — Lässt sich für jede Schicht die Verantwortung in einem Satz nennen?

- **Ja** → weiter mit Frage 2.
- **Nein** → die Schicht trägt mehrere Aufgaben. Das ist ein Befund für den Review (2-8), nicht für die Landkarte.

### Frage 2 — Lässt sich für jede typische Änderung sagen, wo sie landet?

- **Ja** → die Architektur ist verständlich. Aufschreiben, was bekannt ist.
- **Nein** → notieren, welche Änderung keinen eindeutigen Ort hat.

### Frage 3 — Gibt es Aufgaben, die eine Schicht erledigt, ohne dass ihr Name darauf hinweist?

- **Ja** → in die Landkarte aufnehmen. Diese Aufgaben kosten bei der Fehlersuche am meisten Zeit.
- **Nein** → fertig.

---

## Der Denkweg auf einen Blick

```
Ausschnitt wählen (ein Testfall, von oben nach unten)
        ↓
Schichten und Verantwortung je Schicht
        ↓
Typische Änderungen: wo landen sie?        kein eindeutiger Ort → Befund für 2-8
        ↓
Versteckte Aufgaben?                        ja → in die Landkarte
        ↓
           LANDKARTE, OHNE BEWERTUNG
```

---

## Die eine Prüffrage

> **Welche Änderung würde genau in dieser Schicht landen?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Stehen in der Landkarte Verzeichnisse statt Verantwortungen? | die Karte beschreibt Ablage, nicht Architektur |
| Enthält die Landkarte Wörter wie „schlecht“ oder „sollte“? | Bewertung ist hineingerutscht |
| Landet eine Änderung in mehr als zwei Schichten? | Kandidat für den Review |
| Fehlt eine Schicht, die ein Testfall indirekt benutzt (Target, Lifecycle)? | die Karte ist unvollständig |

---

## Wenn die Entscheidung steht

**Kurz halten.** Eine Seite genügt. Sie wird gelesen, eine längere nicht.

**Mit Beispielen.** Je Schicht eine typische Klasse und eine typische Änderung.

**Versteckte Aufgaben ausdrücklich nennen.** Kontextwechsel, Neuverbindung, Wartezeiten.

**Für Werkzeuge nutzbar machen.** Dieselbe Übersicht dient an Tag 3 als Kontext für Claude Code.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Landkarte mit Zielarchitektur | die Landkarte beschreibt, was ist |
| Verzeichnisstruktur mit Schichten | eine Schicht kann über Verzeichnisse verteilt sein |
| Kopplung mit Fehler | notwendige Kopplung an einem Ort ist gewollt |
| Pattern-Namen mit Verantwortung | „Page Object“ sagt nichts, solange nicht klar ist, was die Klasse tut |
