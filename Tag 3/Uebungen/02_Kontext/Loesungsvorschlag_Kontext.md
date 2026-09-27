# Lösungsvorschlag · Was gehört in den Skill?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob jeder Befund **an dem Ort landet, an dem er am wenigsten veraltet**.

---

## 1 · Einordnung

| Befund | Kategorie | Begründung |
|---|---|---|
| B1 `get()` ohne Warten | Gefahr + Routing, übergangsweise; den vorhandenen Hinweis bei `NumericTextFieldDelegate` verallgemeinern | aus dem Code nur mit Squish-Wissen erkennbar; besser im Framework beheben |
| B2 `deviating_*` ohne `try/finally` | Framework; bis dahin den vorhandenen Hinweis ergänzen | der Skill empfiehlt `deviating_name_value` für Listenzeilen und nennt „not reentrant“, aber nicht, dass eine Exception den Real Name verändert zurücklässt |
| B3 `set_setting=True` | Routing | „Wert setzen und prüfen → `set()`, dann `UIElementTest(...).test(...)`“ |
| B4 `go_back()` | nicht aufnehmen | Methode existiert nicht |
| B5 `is_bool` | nicht aufnehmen, Framework | betrifft datengetriebene Tests, nicht den Skill |

---

## 2 · Besser im Framework

B1, B2, B5. Alle drei sind Fehler oder Fallen im Framework. Eine Korrektur gilt für jeden Test, auch handgeschriebene. Für B1 und B2 enthält der Skill schon Teilhinweise; nach der Korrektur im Framework entfallen sie.

---

## 3 · Methode, die es nicht gibt

Das Modell schreibt `masetth.submenu_gnss_source.go_back()`. `check_test.py` meldet A001, im besten Fall. Im schlimmeren Fall erfindet das Modell passende Methoden, um die Kette zu schließen. Genau das soll die No-Hallucination-Regel verhindern.

---

## 4 · Gefahreneintrag für B1

```markdown
### ⚠️ `get()` reads without waiting

`Control.get_property_value` checks `object.exists` first, and `object.exists` does not wait.
Read a value right after a navigation click and a field that renders a moment later reads as
`None` — reported as `Expected: X. Found: None`, the same message a missing object produces.
Wait for the field first, then assert.
```

---

## 5 · Routing-Zeile für B1

```markdown
| Read a value right after opening a screen | `field.wait_for_exists(timeout_msec=…)`, then `UIElementTest(field).test(…)` |
```

---

## 6 · Ort

Gefahr in `controls_and_tests.md` (immer geladen), Routing in `code_patterns.md` (Schritt 4). So stehen beide einmal, und das Modell hat die Gefahr bei jedem Aufruf.

---

## 7 · Prüfbar

`check_references.py` prüft `Control.get_property_value`, `wait_for_exists`, `UIElementTest` (D2). Die Aussage „`object.exists` does not wait“ prüft es nicht.

---

## 8 · Nach der Behebung von B1

Gefahr und Routing-Zeile entfernen. Ablaufbedingung am Eintrag: „Remove when `get_property_value` waits (see <Ticket>).“

---

## Diskussionsanschluss

Welche Einträge im Skill haben heute keine Ablaufbedingung, obwohl sie eine bräuchten?
