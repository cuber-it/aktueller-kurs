# 3-2 · nachher · Derselbe Befund als Gefahr und Routing-Zeile

Eine mögliche Richtung, im Stil der Referenzen des Teams (`controls_and_tests.md`, `code_patterns.md`). Die Einträge sind auf Englisch wie der Skill.

---

### Eintrag in `controls_and_tests.md`, Abschnitt Hazards

```markdown
### ⚠️ `get()` reads without waiting

`Control.get_property_value` checks `object.exists` first, and `object.exists` does not wait.
Read a value right after a navigation click and a field that renders a moment later reads as
`None` — reported as `Expected: X. Found: None`, the same message a missing object produces.
Wait for the field first, then assert.
```

### Zeile in der Routing-Tabelle von `code_patterns.md`

```markdown
| Read a value right after opening a screen | `field.wait_for_exists(timeout_msec=…)`, then `UIElementTest(field).test(…)` |
```

---

## Warum so

| Regel des Teams | umgesetzt |
|---|---|
| 1 Gefahren und Fehlermodi | die Gefahr ist die Überschrift |
| 4 Routing „Absicht → Aufruf“ | eine Zeile, die sagt, was zu tun ist |
| 6–8 keine Inventare, Signaturen, Zeilennummern | nur Methodennamen, `check_references.py` D2 prüft sie |
| 10 jede Regel an einer Stelle | Gefahr in `controls_and_tests.md`, Routing in `code_patterns.md` |

## Und wenn Tag 2 umgesetzt wird

Wartet `get_property_value` künftig selbst (Beispiel 2-3 nachher), entfallen Gefahr und Routing-Zeile. Nach der eigenen Regel des Teams gehört dann nur noch ein Satz in den Skill, falls überhaupt: der geänderte Mechanismus ist aus dem Quelltext ablesbar.

Eine Regel für eine Methode, die es noch nicht gibt (etwa `go_back()` aus 2-2), gehört erst in den Skill, wenn die Methode existiert. Sonst lehrt der Skill einen Namen, der zu einem `AttributeError` führt, genau das, was die No-Hallucination-Regel verhindern soll.
