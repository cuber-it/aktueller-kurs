# Lösungsvorschlag · Worauf wartet dieser Code?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob jede Wartestelle **auf einen Zustand** wartet und ob Wiederholungen **den Erfolg der Aktion** beobachten.

---

## 1 · Ziel erscheint nach 0,7 s

| Zeit | Schritt |
|---|---|
| 0,0 s | Ziel fehlt → Klick 1 |
| 0,0–0,5 s | `waitFor(…, 500)` liefert `False` |
| 0,5 s | Ziel fehlt → Klick 2 |
| 0,7 s | Ziel erscheint (Klick 1), `waitFor` liefert `True` |
| 0,7 s | Schleife endet, kein FAIL |

Danach wirkt Klick 2.

---

## 2 · Wann ein zweiter Klick harmlos ist

Harmlos, wenn der geklickte Button nach dem ersten Klick nicht mehr existiert oder ein zweiter Klick nichts verändert. `settings_action_btn` gilt laut Coding-Regeln als idempotent. `layout_manager_btn` schaltet das Panel auf und zu, ein zweiter Klick schließt es.

Die „right“-Variante wartet auf den OK-Button im Panel statt auf einen Eintrag. Das Ziel erscheint früher, die Schleife endet meist nach dem ersten Klick. Erscheint der OK-Button aber erst nach 500 ms, klickt sie trotzdem erneut. Die Regel verkleinert das Zeitfenster, schließt den Fehler aber nicht aus.

---

## 3 · `get()` bei fehlendem Objekt

`object.exists` liefert `False`, `get_property_value` gibt `None` zurück, ohne zu warten und ohne Protokolleintrag. `get()` versucht noch `displayText` und `value`, jeweils mit demselben Ergebnis, und liefert `"None"`. Im Protokoll steht nur die Abweichung der Prüfung.

---

## 4 · Die Beobachtungen

- Layout-Manager wieder zu: Aufgabe 1 und 2.
- „Found: None“: Aufgabe 3. Mit `snooze(1)` existiert das Feld beim Lesen.

---

## 5 · `click_and_wait` mit einem Klick

Die Regel („bei umschaltender Quelle auf das Panel warten“) muss heute jeder Aufrufer kennen, Mensch oder Skill. Eine API, die nur einmal klickt, macht die Regel überflüssig.

```python
def click_and_wait(self, wait_object, timeout_msec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT):
    timeout_msec = timeout_msec if timeout_msec else self.wait_timeout
    self.click(quiet=True)
    if not squish.waitFor(lambda: wait_object.exists(quiet=True), timeout_msec):
        fail_test(f"After clicking {self.display_name}: {wait_object.display_name} did not appear "
                  f"within {timeout_msec} ms. Expected: {wait_object}", raise_exception=True)
```

---

## 6 · Sicheres Wiederholen

`click_while_exists()` ohne Argument: Die Schleife läuft, solange der geklickte Control existiert. Ist er weg, ist der Klick angekommen. Für Fälle mit verlorenen Klicks wäre das der Ersatz, sofern der Button nach Erfolg verschwindet.

---

## 7 · Lesen mit Warten

```python
READ_TIMEOUT_MSEC = 5000


def get_property_value(self, prop, quiet=UI_ELEMENTS_QUIET_DEFAULT):
    obj = self.wait_for_exists(fail_if_not_exists=False, timeout_msec=READ_TIMEOUT_MSEC, quiet=True)
    if obj is None:
        fail_test(f"Cannot read {prop}: {self.display_name} did not appear within {READ_TIMEOUT_MSEC} ms.{self}",
                  raise_exception=True)
    return getattr(obj, prop, None)
```

Kürzer als der allgemeine Timeout, weil der Aufrufer ein vorhandenes Objekt erwartet. Wer das Fehlen prüfen will, nutzt `exists()`.

---

## 8 · Verbliebene Wartezeiten prüfen

Im aktiven Bestand stehen 51 `snooze`, davon 6 direkt nach Klicks, dazu Parameter wie `snooze_time=8`. Nach dem Umbau aus Aufgabe 7 diese Stellen einzeln in einem Testlauf entfernen. Bleibt ein Test grün, war die Wartezeit überflüssig. Wird er rot, zeigt die neue Meldung, worauf gewartet werden muss. Begründete Fälle gehören in die Ausnahmetabelle der Snooze-Regel.

---

## 9 · Regelkandidaten

| Regel | Einordnung |
|---|---|
| Wiederholte Klicks nur, wenn die Schleife den geklickten Control beobachtet | SHOULD |
| Eine Gefahr, die die API beseitigen kann, wird nicht als Regel für den Aufrufer dokumentiert | SHOULD |
| Lesende Methoden warten auf das Objekt und melden ein fehlendes Objekt mit Real Name | SHOULD |
| kein `snooze` nach Navigationsklick | MUST (bereits Teamregel) |

---

## Diskussionsanschluss

Welche Tests verlassen sich heute darauf, dass `click_and_wait` verlorene Klicks auffängt? Wie finden Sie sie, bevor Sie die Methode ändern?
