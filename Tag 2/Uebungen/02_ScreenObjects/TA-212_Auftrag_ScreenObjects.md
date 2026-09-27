# TA-212 · Navigation und Wartezeiten aus den Testfällen in die Screen Objects verlagern

**Typ:** Story
**Komponente:** UI-Module Maschineneinstellungen
**Priorität:** Hoch

---

## Story

**Als** Entwickler im Testautomatisierungsteam
**möchte ich**, dass Testfälle über Operationen der Screen Objects navigieren,
**damit** eine Änderung an einem Menüweg ein Screen Object betrifft und nicht jeden Test, der den Weg geht.

---

## Description

Die Screen Objects der Maschineneinstellungen beschreiben Menüs und ihre Controls. Navigation und Wartezeiten stehen dagegen meist im Testfall.

**Bestand:**

| Was | Anzahl |
|---|---|
| `squish.snooze` direkt nach einem Klick im aktiven Code | 6 |
| `back_btn.click_and_wait(<Objekt des Zielmenüs>)` | 58 |
| Navigationsmethoden in `SubMenuMachineSettings` | 2 (`open_implement_settings_by_text`, `open_settings_default_tractor`) |
| `deviating_text` / `deviating_container` | 23 |

**Befund:** Führt ein Zurück-Button nach einem Umbau in ein anderes Menü, ändern sich alle Stellen, die nach dem Klick auf ein Objekt des bisherigen Zielmenüs warten. Im Bestand sind das bis zu 58 Aufrufe in Tests und Helpern.

**Zweiter Befund:** Die eigene Regel „After a navigation click → never snooze“ ist im aktiven Code umgesetzt. Sie ersetzt das Warten auf Zeit durch `click_and_wait(<Objekt des Zielmenüs>)`. Damit muss jeder Aufrufer das Zielmenü kennen.

**Nicht Gegenstand:** Die Control-Schicht und die Synchronisation innerhalb von Controls (TA-218).

## Randbedingungen

- Bestehende Tests müssen weiterlaufen. Neue Operationen ergänzen die vorhandenen Controls, sie ersetzen sie nicht sofort.
- Begründete Wartezeiten aus der Tabelle der Snooze-Policy bleiben erlaubt, gehören dann aber in die Operation.
- Die Real Names bleiben in den UI-Modulen.

## Akzeptanzkriterien

- **AK1** – Für die Menüs der Maschineneinstellungen gibt es Navigationsoperationen, die das Screen Object des Ziels zurückgeben.
- **AK2** – Eine Änderung des Zielmenüs eines Zurück-Buttons betrifft genau eine Methode.
- **AK3** – Testfälle, die die neuen Operationen verwenden, enthalten kein `snooze` nach Navigation.
- **AK4** – Eine gescheiterte Navigation meldet, welches Menü nicht erschienen ist.
- **AK5** – Varianten eines Controls für einen Listeneintrag verändern kein geteiltes Control.

## Hinweise

Das `snooze` aus dem Test in die Operation zu kopieren erfüllt AK3 nur formal. Es ist nur dort vertretbar, wo die Snooze-Policy es begründet.

AK5 wird unbequem: `deviating_text` ist bequem und wird 23-mal verwendet. Eine Alternative muss genauso knapp sein.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Muss der Test das wissen, oder das Menü?**

---
---

# Addendum · Woran man eine unvollständige UI-Abstraktion erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Tests greifen auf Controls zu, nicht auf Operationen | `masetth.submenu_implement.general_btn.click()` |
| Tests kennen Objekte anderer Menüs | `back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)` |
| Wartezeiten nach Klicks im Test | `squish.snooze(1)` |
| Fast gleiche Navigationsmethoden | `open_implement_settings_by_text`, `open_settings_default_tractor` |
| Controls werden für einen Aufruf umgebaut | `deviating_text(...)` |

## Was ein Screen Object anbieten kann

| Art | Beispiel | Rückgabe |
|---|---|---|
| Navigation | `open_tractor_settings()`, `go_back()` | Screen Object des Ziels |
| Aktion im Menü | `select(GnssSource.sae_j1939)` | nichts oder `self` |
| Zustand | `selected_source()` | Wert |
| Prüfung | `verify_selected(...)` | umstritten, siehe 2-7 |

## Page Object und Object Map

Die Object Map beantwortet: Wie wird ein Objekt gefunden? Das Screen Object beantwortet: Was kann man mit diesem Menü tun? Im Framework liegen beide Antworten im UI-Modul. Das ist vertretbar, solange jeder Real Name einmal steht.
