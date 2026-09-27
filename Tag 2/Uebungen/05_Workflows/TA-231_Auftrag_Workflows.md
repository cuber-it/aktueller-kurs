# TA-231 · Rücksetzen auf Werkswerte für alle Geräteparameter

**Typ:** Story
**Komponente:** Helper Maschineneinstellungen
**Priorität:** Mittel

---

## Story

**Als** Verantwortliche der Applikationstechnik
**möchte ich** alle Parameter eines Geräts per Test auf ihre Werkswerte zurücksetzen,
**damit** Tests mit einem definierten Gerät beginnen.

---

## Description

`MachineSettingsParameterTests` liest, vergleicht und setzt alle Parameter eines Geräts. Die Aktion wird über `self.action` gewählt. Jede Methode `process_<Control-Typ>` verzweigt nach der Aktion.

**Bestand:**

| Was | Anzahl |
|---|---|
| Aktionen (`TestAction`) | 3 |
| Methoden `process_<Control-Typ>` | 5 |
| Zweige nach Aktion je Methode | 3 bis 4 (mit „unbekannt“) |
| Menüs in `iterate_through_implement_settings` | alle Untermenüs eines Geräts |

**Befund:** Für eine vierte Aktion braucht jede der fünf Methoden einen weiteren Zweig, und jeder Zweig kennt Control-Typ und Aktion. Ein Fehler in einem Zweig (etwa beim Setzen von Schaltern) fällt erst auf, wenn genau diese Kombination läuft.

**Befund zur Entstehung:** Die Klasse begann mit dem Auslesen. Vergleich und Setzen kamen als weitere Zweige dazu.

**Nicht Gegenstand:** Die Controls und Screen Objects.

## Randbedingungen

- Die drei vorhandenen Aktionen müssen weiter funktionieren.
- Die Referenz-CSV bleibt im heutigen Format.
- Werkswerte stehen in einer eigenen CSV im selben Format.

## Akzeptanzkriterien

- **AK1** – Eine neue Aktion ist eine neue Funktion; kein bestehender Code verzweigt nach ihr.
- **AK2** – Ein neuer Control-Typ braucht eine Stelle für Lesen und Setzen.
- **AK3** – Der Weg durch die Menüs steht an einer Stelle und kennt keine Aktion.
- **AK4** – Die vierte Aktion „auf Werkswerte zurücksetzen“ ist umgesetzt.

## Hinweise

Einen fünften Zweig in jede Methode einzubauen erfüllt AK4, aber nicht AK1.

AK3 wird unbequem: Heute prüft der Weg an einer Stelle `self.action`, um den Fokus zu setzen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche Änderung trifft diese Stelle, und trifft sie auch die anderen?**

---
---

# Addendum · Helper, Task, Workflow

| Art | Verantwortung | Beispiel |
|---|---|---|
| technischer Helper | eine technische Fähigkeit | Wert eines `CheckDelegate` lesen |
| Task | eine Testhandlung mit Bedeutung | einen Parameter mit der Referenz vergleichen |
| Workflow | eine Abfolge mit Zustand über mehrere Bereiche | alle Parameter eines Geräts durchgehen |
| Orakel | Bewertung gegen eine Erwartung | Vergleich mit Referenz-CSV |

## Signale für vermischte Verantwortung

| Signal | Beispiel |
|---|---|
| Verzweigung nach Aktion in jeder Methode | `if self.action == …` |
| Methoden je Typ, die dieselben Zweige enthalten | `process_text_field_delegate`, `process_check_delegate` |
| Zustand als Text | `self.names += ";" + …` |
| Weg durch Menüs kennt die Aktion | `if self.action == TestAction.set_to_ref: enforceFocus()` |
