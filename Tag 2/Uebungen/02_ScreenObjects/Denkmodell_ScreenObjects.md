# Denkmodell · Was gehört ins Screen Object?

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Tests greifen auf Controls zu, nicht auf Operationen | `submenu_implement.general_btn.click()` |
| Tests warten auf Objekte eines anderen Menüs | `back_btn.click_and_wait(submenu_traction_unit.traction_unit_title_txt)` |
| Wartezeiten nach Klicks im Test | `squish.snooze(1)` |
| Gleiche Menüwege in mehreren Helpern | Statusleiste → Einstellungen → Maschine |
| Controls werden für einen Aufruf umgebaut | `deviating_text(...)` |
| Screen Objects haben kaum Methoden, nur Attribute | `SubMenuGNSSSource` |

### Im Team

| Signal | Konkret |
|---|---|
| Ein Menüumbau betrifft viele Tests | 58 Aufrufe kennen das Zielmenü |
| Suchen und Ersetzen über Testfälle | Zeilenumbrüche verhindern Treffer |
| Helper kennen die Reihenfolge fremder Menüs | `close_machine_settings_menus` |

---

## Stufe 2 · Erkenntnisse

**1. Ein Screen Object ist mehr als ein Ort für Real Names.**
Es kann beschreiben, was man mit dem Menü tun kann und wohin seine Buttons führen.

**2. Wissen über Navigation gehört dem Menü, von dem sie ausgeht.**
Der Zurück-Button der GNSS-Quelle führt irgendwohin. Das sollte die GNSS-Quelle wissen, nicht der Test.

**3. Warten gehört zu der Stelle, die den Zustand kennt.**
Ob ein Menü erschienen ist, weiß das Screen Object des Ziels. Eine Sekunde Pause weiß gar nichts.

**4. Ein geteiltes Control ist geteilter Zustand.**
Wer seinen Real Name ändert, ändert ihn für alle Tests eines Laufs.

**Was gesucht wird:** die Operationen, die ein Test braucht, und das Menü, zu dem sie gehören.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Navigationsmethode mit Rückgabe des Ziels** | ein Weg in mehreren Tests vorkommt oder sein Ziel sich ändern kann |
| **Aktionsmethode im Screen Object** | dieselbe Abfolge von Klicks mehrfach vorkommt |
| **Control bleibt direkt zugänglich** | eine Bedienung einmalig und lokal ist |
| **Neues Control statt verändertem** | ein Control für einen bestimmten Eintrag gebraucht wird |
| **Warten in der Operation** | der Zustand abfragbar ist; sonst begründetes `snooze` nach der Policy |

---

## Stufe 4 · Entscheidung

### Frage 1 — Kommt diese Abfolge in mehr als einem Test vor?

- **Ja** → Kandidat für eine Operation. Weiter mit Frage 2.
- **Nein** → im Test lassen, sofern er keine fremden Menüs kennen muss.

### Frage 2 — Von welchem Menü geht sie aus?

- Die Operation gehört in dessen Screen Object.

### Frage 3 — Führt sie in ein anderes Menü?

- **Ja** → sie wartet auf dessen Zustand und gibt dessen Screen Object zurück.
- **Nein** → sie gibt nichts oder `self` zurück.

### Frage 4 — Braucht sie eine Variante eines Controls?

- **Ja** → ein neues Control erzeugen, das geteilte unverändert lassen.

---

## Der Denkweg auf einen Blick

```
Abfolge im Test
        ↓
Mehrfach?                          nein → im Test lassen
        ↓ ja
Von welchem Menü geht sie aus?  →  Methode dort
        ↓
Führt sie weg?                     ja → auf Ziel warten, Ziel zurückgeben
        ↓
Braucht sie Control-Varianten?     ja → neues Control, geteiltes unverändert
```

---

## Die eine Prüffrage

> **Muss der Test das wissen, oder das Menü?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Kennt ein Test ein Objekt eines Menüs, das er nicht bedient? | Navigationswissen im Test |
| Steht nach einem Klick ein `snooze` ohne Kommentar? | Kandidat für Warten auf Zustand |
| Hat ein Screen Object nur Attribute? | es beschreibt, bietet aber nichts an |
| Ändert eine Methode den Real Name eines Attributs? | geteilter Zustand |
| Gibt eine Operation nichts zurück, obwohl sie das Menü wechselt? | der Test muss das Ziel selbst kennen |

---

## Wenn die Entscheidung steht

**Schrittweise einführen.** Neue Operationen neben den Controls anbieten. Neue und geänderte Tests verwenden sie, alte laufen weiter.

**Wartezeiten mitnehmen.** Ist ein `snooze` begründet, wandert es in die Operation und in die Tabelle der Snooze-Policy.

**Prüfungen im Test lassen.** Ob ein Screen Object prüfen darf, ist eine eigene Frage (2-7).

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Screen Object mit Object Map | die Object Map sagt, wie man findet, das Screen Object, was man tun kann |
| Operation mit Umbenennung | `click_back()` statt `back_btn.click()` ändert nichts am Wissen des Tests |
| Rückgabe des Ziels mit Fluent API | die Rückgabe folgt der Navigation, nicht dem Stil |
| `click_and_wait` mit Navigation | die Methode wartet, aber der Test entscheidet noch, worauf |
