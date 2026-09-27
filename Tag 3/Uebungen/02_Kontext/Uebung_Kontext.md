# Übung · Was gehört in den Skill?

Sie entscheiden, welche Befunde aus Tag 1 und Tag 2 in den Kontext Ihres Testfall-Skills gehören, in welcher Form und an welcher Stelle. Maßstab sind die eigenen Regeln Ihres Teams dafür, was in den Skill gehört und was nur referenziert wird.

---

## Material A · Die Kontextregeln des Teams

Aus dem README des Skills (sinngemäß):

**In den Skill gehört**
1. Gefahren und Fehlermodi, die aus dem Quelltext nicht erkennbar sind.
2. Konventionen und Entscheidungen.
3. Prozessregeln.
4. Routing „Absicht → Aufruf“, nach eigener Aussage der wertvollste Inhalt.
5. generierte, repoübergreifende Übersichten.

**Nur referenziert wird**
6. keine Methodeninventare, 7. keine Signaturen, 8. keine Zeilennummern, 9. Ausnahme: negative Fakten, 10. jede Regel an genau einer Stelle.

`check_references.py` prüft die Skill-Dokumentation gegen den Code: Importe, Methoden, Konstanten, Referenztests, keine Zeilennummern.

---

## Material B · Ein vorhandener Gefahreneintrag

Aus `controls_and_tests.md` (gekürzt):

```markdown
### ⚠️ `click_and_wait` re-clicks the source on every retry

`Control.click_and_wait(b)` loops *clicking `a`* until `b` exists. That is correct when
`a` is idempotent — a statusbar button, a list entry — but **destructive when `a` toggles
something**: clicking the layout-manager button again closes the layout manager.
```

---

## Material C · Befunde aus Tag 1 und Tag 2

| Nr. | Befund |
|---|---|
| B1 | `get()` liest ohne zu warten: Ein Feld, das kurz nach der Navigation erscheint, ergibt „Found: None“, dieselbe Meldung wie ein fehlendes Objekt. Der Skill erwähnt das bisher nur für `NumericTextFieldDelegate` („`test()` does not“ wait). |
| B2 | `deviating_*` stellt den Real Name ohne `try/finally` zurück; nach einer Exception bleibt das geteilte Control verändert. Der Skill empfiehlt `deviating_name_value`, um eine Listenzeile anzusprechen, und warnt, dass es nicht reentrant ist. |
| B3 | `UIElementTest.test(value, set_setting=True)` setzt und prüft in einem Aufruf; scheitert das Setzen, folgen Vergleichsfehler. |
| B4 | Vorschlag aus Tag 2: Screen Objects bekommen Navigationsmethoden wie `go_back()`, die das Zielmenü zurückgeben. Noch nicht umgesetzt. |
| B5 | Tag 1: `get_data_value(..., is_bool=True)` wandelt `"True"` in `False`. |

---

## Aufgabe

### Teil 1 · Einordnen

**1.** Ordnen Sie jeden Befund aus Material C einer Kategorie aus Material A zu, oder begründen Sie, warum er nicht in den Skill gehört.

**2.** Für welche Befunde wäre eine Änderung am Framework besser als ein Eintrag im Skill?

**3.** B4 beschreibt eine Methode, die es noch nicht gibt. Was passiert, wenn sie jetzt schon im Skill steht?

### Teil 2 · Schreiben

**4.** Schreiben Sie für einen Befund einen Gefahreneintrag im Stil von Material B.

**5.** Schreiben Sie für denselben Befund eine Zeile für die Routing-Tabelle „Absicht → Aufruf“.

**6.** In welche Datei gehören die beiden Einträge? Welche Referenz lädt der Skill immer, welche nur bei Bedarf?

### Teil 3 · Pflege

**7.** Welche Ihrer Einträge kann `check_references.py` prüfen, welche nicht?

**8.** Was muss passieren, wenn B1 im Framework behoben ist?

---

## Hinweise zur Bearbeitung

- Die Einträge dürfen auf Englisch sein wie der Skill.
- Nur Methodennamen verwenden, die es im Framework gibt.
- Wenn Sie unsicher sind, fragen Sie: **Kann das Modell das aus dem Quelltext selbst herausfinden?**
