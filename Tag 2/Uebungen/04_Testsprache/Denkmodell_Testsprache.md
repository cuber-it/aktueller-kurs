# Denkmodell · Wie fachlich soll ein Test sein?

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| fachliche Variante steht im Attributnamen | `sae_j1939_btn` statt `GnssSource.sae_j1939` |
| Test kennt Objekte fremder Menüs | `traction_unit_title_txt` nach dem Zurück-Klick |
| Positionsargumente mit `None`/`False` | `test_wrapper(None, False)` |
| Wartezeiten als Parameter im Test | `snooze_time=8` |
| Helper für Wege und Prüfungen, nicht für Einstellungen | `open_…`, `assert_…` |

### Im Team

| Signal | Konkret |
|---|---|
| Fachabteilung kann Tests nicht beurteilen | Review abgebrochen |
| Kommentare widersprechen dem Code | kopiert, nicht angepasst |
| Testlisten außerhalb des Codes | Excel, schnell veraltet |

---

## Stufe 2 · Erkenntnisse

**1. Ein Test hat eine Aussage und eine Bedienung.**
Die Aussage sollte im Test stehen, die Bedienung kann woanders stehen.

**2. Eine fachliche Operation benennt eine Absicht.**
`select_gnss_source(GnssSource.sae_j1939)` ist fachlich. `click_sae_j1939_btn()` ist eine umbenannte Bedienung.

**3. Prüfungen sind Aussage, nicht Bedienung.**
Sie gehören sichtbar in den Test.

**4. Jede Ebene kostet.**
Eine Operation mehr heißt eine Stelle mehr beim Lesen und bei der Fehlersuche.

**Was gesucht wird:** die Zeilen, die die Aussage tragen, und die Zeilen, die nur bedienen.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Facade-Funktion** | eine Bedienfolge in mehreren Tests mit fachlicher Bedeutung vorkommt |
| **Parameter mit Enum** | Varianten einer Operation sich nur in einem Wert unterscheiden |
| **Schlüsselwortargumente** | Positionsargumente nicht selbsterklärend sind |
| **Fluent Interface** | lange Ketten fachlicher Schritte lesbar werden sollen und der Zustand zwischen ihnen klar ist |
| **direkter Control-Zugriff** | die Bedienung einmalig und selbst die Aussage des Tests ist |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gehört die Zeile zur Aussage des Tests?

- **Ja** → bleibt sichtbar im Test.
- **Nein** → weiter mit Frage 2.

### Frage 2 — Kommt die Bedienfolge in mehreren Tests vor?

- **Ja** → fachliche Operation mit Parameter.
- **Nein** → im Test lassen, wenn kurz.

### Frage 3 — Versteht ein Fachkundiger den Namen der Operation?

- **Ja** → gut.
- **Nein** → der Name beschreibt die Bedienung, nicht die Absicht.

### Frage 4 — Zeigt die Fehlermeldung, welches Control betroffen ist?

- **Nein** → die Operation verbirgt zu viel.

---

## Der Denkweg auf einen Blick

```
Zeile im Test
        ↓
Teil der Aussage?               ja → sichtbar lassen
        ↓ nein
Mehrfach vorhanden?             nein → im Test, wenn kurz
        ↓ ja
Fachliche Operation mit Parameter (Enum)
        ↓
Name verständlich? Meldung nennt Control?
```

---

## Die eine Prüffrage

> **Welche Information verschwindet, und ist genau diese für den Test wichtig?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Heißt eine Operation wie ein Control? | umbenannte Bedienung |
| Enthält eine Operation eine Assertion, die der Test nicht zeigt? | Aussage versteckt |
| Braucht ein Leser das Screen Object, um den Test zu verstehen? | Bedienung im Test |
| Lässt sich eine Fluent-Kette nicht an einer Stelle unterbrechen und prüfen? | die Kette verbirgt Zustand |

---

## Wenn die Entscheidung steht

**Vorhandenes nutzen.** `GnssSource` gibt es, die Helper gibt es. Neu sind nur Operationen für die Einstellung.

**Prüfungen sichtbar lassen.** Auch wenn eine Operation intern prüft, steht die fachliche Prüfung im Test.

**Meldungen erweitern.** Eine Operation, die ein Control verbirgt, nennt es in ihrer Fehlermeldung.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| fachlich mit kurz | `run_all()` ist kurz, aber sagt nichts |
| Facade mit Umbenennung | die Facade fasst mehrere Schritte zusammen |
| Fluent Interface mit Lesbarkeit | Ketten lesen sich gut, bis ein Glied fehlschlägt |
| Helper mit Domain API | ein Helper kann technisch sein, eine Domain API spricht Fachsprache |
