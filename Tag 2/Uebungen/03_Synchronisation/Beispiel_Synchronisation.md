# Beispiel · Worauf wartet dieser Code? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für das Bedienfeld einer Waschmaschine. Die Starttaste schaltet zwischen Start und Pause um. Ein Test startet ein Programm:

```python
def click_until(button, target, timeout_s=30):
    end = time.monotonic() + timeout_s
    while time.monotonic() < end and not target.exists():
        button.click()
        squish.waitFor(target.exists, 500)


click_until(panel.start_btn, panel.running_indicator)
```

Auf einem neuen Modell erscheint die Laufanzeige erst nach 800 ms.

---

## Schritt 1 · Durchspielen

| Zeit | Ereignis |
|---|---|
| 0 ms | Klick: Start |
| 500 ms | Laufanzeige fehlt noch, zweiter Klick: Pause |
| 800 ms | Laufanzeige erscheint (vom ersten Klick) |
| 800 ms | Schleife endet, Test meldet Erfolg |
| kurz danach | Maschine geht in Pause (zweiter Klick) |

---

## Schritt 2 · Wann ist Wiederholen sicher?

Die Starttaste bleibt sichtbar und schaltet um. Ein zweiter Klick ist nicht harmlos. Sicher wäre Wiederholen bei einer Taste, die nach einem angekommenen Klick verschwindet, etwa „Tür öffnen“, die durch „Tür ist offen“ ersetzt wird.

---

## Schritt 3 · Umbau

```python
def click_and_wait(button, target, timeout_ms=5000):
    button.click()
    if not squish.waitFor(target.exists, timeout_ms):
        raise AssertionError(f"{target} did not appear within {timeout_ms} ms after clicking {button}")


def click_until_gone(button, timeout_ms=5000):
    """Nur für Tasten, die nach einem angekommenen Klick verschwinden."""
    end = time.monotonic() + timeout_ms / 1000
    while button.exists() and time.monotonic() < end:
        button.click()
        squish.waitFor(lambda: not button.exists(), 500)
```

---

## Was dieses Beispiel zeigt

**Eine Schleife mit Klick ist nur so sicher wie ihre Bedingung.** Beobachtet sie ein anderes Objekt als das geklickte, kann sie zu oft klicken.

**Schwellen verschieben nichts.** Ein längeres Warten zwischen den Klicks verschiebt das Problem auf die nächste, noch langsamere Maschine.

**Die Taste weiß, ob sie umschaltet.** Diese Information gehört an die Taste, nicht in jeden Aufruf.
