# TA-218 · Sporadische Fehlschläge auf dem langsameren Terminal beheben

**Typ:** Bug
**Komponente:** Control-Schicht (`UI/controls.py`)
**Priorität:** Hoch

---

## Story

**Als** Verantwortliche für den Nachtlauf
**möchte ich**, dass Klicken, Warten und Lesen auf einem langsameren Terminal genauso zuverlässig sind wie auf dem schnellen,
**damit** ein roter Test einen Fehler der AUT bedeutet und nicht eine Frage des Timings.

---

## Description

Seit das neue Terminal im Nachtlauf läuft, schlagen einzelne Tests sporadisch fehl. Auf dem bisherigen Terminal traten diese Fehler nicht auf.

**Bestand:**

| Was | Anzahl |
|---|---|
| `click_and_wait` | 158 |
| davon auf `layout_manager_btn` (schaltet um), alle mit Ziel `layout_manager_ok_btn` | 13 |
| `squish.snooze` im aktiven Code | 51 |
| Lesezugriffe über `get()` in `UIElementTest` | 148 |

**Befund:** Beide Mechanismen hängen an Zeitannahmen. `click_and_wait` klickt erneut, wenn das Ziel nach 500 ms fehlt; bei einer umschaltenden Quelle schließt der zweite Klick das Panel wieder. `get_property_value` liest ohne zu warten; ein Feld, das kurz nach der Navigation erscheint, ergibt „Found: None“. Auf schneller Hardware bleiben beide Effekte unter der Schwelle, auf langsamerer nicht.

**Befund zur Entstehung:** Die Gefahr des Wiederholungsklicks bei umschaltenden Quellen ist dokumentiert, und alle Aufrufe folgen der empfohlenen Variante: Ziel ist der OK-Button im Panel. Erscheint er aber nicht innerhalb von 500 ms, klickt `click_and_wait` trotzdem erneut. `get_property_value` prüft mit `object.exists` und wartet nicht. Auf dem schnellen Terminal blieb beides unter der Schwelle.

**Nicht Gegenstand:** Die Navigation in Screen Objects (TA-212).

## Randbedingungen

- Die Signaturen von `click_and_wait` und `get()` bleiben kompatibel.
- Fälle, in denen der Wiederholungsklick verlorene Klicks auffängt, sind nicht dokumentiert.
- Die Coding-Regeln und die Abschlussliste des Skills (Punkt 6c) behandeln die Gefahr als Regel für den Aufrufer.

## Akzeptanzkriterien

- **AK1** – Eine umschaltende Quelle wird durch `click_and_wait` genau einmal geklickt, unabhängig davon, wie lange das Ziel braucht.
- **AK2** – Erscheint das Ziel nicht, meldet der Test das Ziel und den geklickten Button.
- **AK3** – Lesen über `get()` wartet auf das Objekt. Fehlt es, nennt die Meldung den Real Name.
- **AK4** – Wiederholtes Klicken ist nur dort möglich, wo die Schleife den geklickten Control selbst beobachtet.
- **AK5** – Die Coding-Regeln sind angepasst. Was die API sicherstellt, steht nicht mehr als Regel für den Aufrufer darin.

## Hinweise

Das `iteration_delay` auf 2 s zu erhöhen erfüllt AK1 nicht. Es verschiebt die Schwelle.

AK4 wird unbequem: Niemand weiß, welche Tests heute auf den Wiederholungsklick angewiesen sind.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Worauf genau wird hier gewartet, und wer kennt diesen Zustand?**

---
---

# Addendum · Woran man eine unsichere Synchronisation erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Schleifen mit Klick und kurzem Warten | `click_and_wait`: Klick, `waitFor(…, 500)` |
| Bedingung beobachtet ein anderes Objekt als das geklickte | Ziel statt Button |
| Lesen ohne Warten | `if self.exists(): …` |
| feste Wartezeit nach Aktionen | `squish.snooze(1)` |
| Meldungen ohne Hinweis auf die Ursache | „Found: None“ |

## Wiederholungen: wann sicher?

| Fall | sicher? |
|---|---|
| Klick, bis der geklickte Control verschwindet | ja: ein angekommener Klick beendet die Schleife |
| Klick, bis ein anderes Objekt erscheint, Button verschwindet dabei | meist: solange der Button nicht mehr existiert, trifft ein zweiter Klick nichts |
| Klick, bis ein anderes Objekt erscheint, Button bleibt sichtbar | nein: ein zweiter Klick wird ausgeführt |

## Squish: was wartet, was nicht

| Funktion | wartet? |
|---|---|
| `waitForObject`, `waitForObjectExists` | ja, bis Timeout, dann `LookupError` |
| `object.exists` | nein |
| `waitFor(bedingung, timeout)` | ja, liefert `True`/`False` |
| `snooze(s)` | ja, fest |
