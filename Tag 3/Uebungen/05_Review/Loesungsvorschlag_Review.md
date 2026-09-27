# Lösungsvorschlag · Prüfskript, KI-Review oder bessere API?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob jede Regel **die günstigste sichere Prüfart** bekommt.

---

## 1 · Einordnung

| Regel | Prüfart | Begründung |
|---|---|---|
| K1 Umschalter | API ändern; bis dahin C004 mit Liste | Verhalten, nicht Name |
| K2 Lesen nach Navigation | API ändern (`get_property_value` wartet) | statisch nicht sicher erkennbar, ob ein Feld später erscheint |
| K3 `set_setting=True` | statisch | Schlüsselwortargument eindeutig |
| K4 `test.passes`/`test.fail` im Test | statisch (Warnung) | Aufruf eindeutig; Ausnahmen (`_verify_*`-Funktionen) über Ort erkennbar |
| K5 Menüwege als Helper | KI-Review | ob eine Folge ein Menüweg ist, braucht Urteil |
| K6 doppelte Testfälle | KI-Review über die Spezifikation | Vergleich von Texten mit Abweichungen |
| K7 `bool(...)` aus Text | statisch, eng | nur `bool(<Aufruf von get()>)` melden, sonst still |

---

## 2 · Statisch ohne Raten

K3, K4, K7 (eng gefasst), K1 mit Liste.

---

## 3 · Warum C004 den Fall nicht findet

`layout_manager_btn` endet auf `_btn`. Die Prüfung erkennt Umschalter am Namen, die Regel betrifft Verhalten.

---

## 4 · Erweiterung

```python
KNOWN_TOGGLING_SOURCES = {"layout_manager_btn": {"layout_manager_ok_btn"}}

if name in KNOWN_TOGGLING_SOURCES:
    if target_name in KNOWN_TOGGLING_SOURCES[name]:
        report.add(WARN, "C004", path, node.lineno, "documented pattern, still re-clicks if slow", "checklist 6c")
    else:
        report.add(ERROR, "C004", path, node.lineno, "waits inside the panel it toggles", "checklist 6c")
```

Die „right“-Variante bleibt eine Warnung: Sie ist dokumentiert, aber zeitabhängig. 13 Warnungen im Bestand sind zu viel Rauschen; Vorschlag: nur für neue Tests prüfen oder die Warnung erst nach der API-Entscheidung einschalten.

---

## 5 · Nachteil der Liste, Alternative

Die Liste ist ein weiterer Ort, an dem die Regel gepflegt wird. Ein neuer Umschalter fehlt, bis jemand ihn einträgt. Alternative: `click_and_wait` klickt genau einmal (Tag 2, Beispiel 2-3). Dann entfallen Liste, Prüfung und Punkt 6c.

---

## 6 · Prüfauftrag für K5

```text
Prüfe test.py gegen die Platzierungsregel des Skills (SKILL.md, Schritt 4b, Zeile
"multi-step navigation walk"). Nenne jede Folge von mehr als zwei Navigationsaufrufen
(click_and_wait, click_while_exists) über verschiedene Screen Objects, die in einem
anderen Test derselben Suite ebenfalls vorkommt. Gib Datei, Zeilen und den vorhandenen
Helper an, falls einer passt. Keine Änderungen vornehmen.
```

---

## 7 · Ort der Ergebnisse

Als Kommentar im Merge Request mit Regelbezug. Wiederkehrende Befunde werden Kandidaten für eine statische Prüfung oder einen Helper.

---

## Diskussionsanschluss

Welches „wrong“-Beispiel aus Ihren Coding-Regeln würde `check_test.py` heute nicht finden?
