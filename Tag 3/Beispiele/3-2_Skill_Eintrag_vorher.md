# 3-2 · vorher · Ein Befund aus Tag 2 als Methodenbeschreibung im Skill

Akademisches Beispiel. So könnte ein Eintrag aussehen, wenn der Befund „`get()` liest ohne zu warten“ aus Tag 2 (Beispiel 2-3) in die Referenzen des Skills übernommen wird, als Beschreibung der beteiligten Methoden.

---

### Control.get_property_value (controls.py:600)

```python
def get_property_value(self, prop, quiet=UI_ELEMENTS_QUIET_DEFAULT)
```

Provides the value of the specified property of the object. Checks `self.exists()` first and
then reads the property from `self.wait_for_exists()`. Returns the value, or `None` if the object
does not exist.

### Control.get (controls.py:692)

```python
def get(self, quiet=UI_ELEMENTS_QUIET_DEFAULT)
```

Returns the `text` property; if empty, `displayText`; if empty, `value`. Always returns `str`.

### Control.wait_for_exists (controls.py:268)

```python
def wait_for_exists(self, fail_if_not_exists=True, timeout_msec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT)
```

Waits for the object to exist. Default timeout is `testSettings.waitForObjectTimeout`.

---

## Was an diesem Eintrag gegen die eigenen Regeln des Teams verstößt

Das README des Skills legt fest, was in den Skill gehört und was nur referenziert wird:

| Regel des Teams | Verstoß |
|---|---|
| 6 keine Methodeninventare | drei Methoden mit Semantik beschrieben |
| 7 keine Signaturen | drei Signaturen zum Abschreiben |
| 8 keine Zeilennummern | `controls.py:600`, `:692`, `:268`; `check_references.py` meldet das als D8 |
| 1 Gefahren, nicht Mechanismus | die Gefahr (Lesen direkt nach Navigation ergibt `None`) steht nirgends |
| 4 Routing „Absicht → Aufruf“ | es fehlt, was ein Test tun soll |

Ein Agent kann aus diesem Eintrag die Gefahr ableiten, muss es aber nicht. Er liest drei Methodenbeschreibungen, die jeder Quelltext auch liefert.
