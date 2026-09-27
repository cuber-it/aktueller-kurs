# KI-334 · Szenarien auf die vorhandene Testarchitektur abbilden

**Typ:** Story
**Komponente:** Skill `testcase-implementer`, Maschineneinstellungen
**Priorität:** Mittel

---

## Story

**Als** Entwickler im Testautomatisierungsteam
**möchte ich**, dass Szenarien auf vorhandene Controls, Screen Objects und Helper abgebildet werden,
**damit** keine zweite Schicht entsteht und fehlende Teile an der richtigen Stelle ergänzt werden.

---

## Description

Szenarien aus dem Testentwurf (KI-323) sollen umgesetzt werden. Für einen Teil der Schritte gibt es fertige Aufrufe, für andere nicht.

**Bestand:**

| Was | Stand |
|---|---|
| Button zum Anlegen eines Anbaugeräts | vorhanden: `SubMenuAnyImplement.add_new_implement_btn` |
| Button zum Anlegen eines Traktors | fehlt |
| Screen Object Zugfahrzeug | vorhanden: `SubMenuTractionUnit` |
| Prüfung „Eintrag ausgewählt“ | vorhanden: `UIElementTest(menu_list.get_delegate_by_text(text)).test(True)` |

**Befund:** Werkzeuge, die das Framework nicht kennen, erzeugen Step-Funktionen mit eigener Object Map und bilden fehlende Elemente nach dem Muster ähnlicher. Für den Traktor entstünde so ein Button-Name nach dem Vorbild von `implementAddNew`, ohne Beleg.

**Befund zur Entstehung:** Werkzeuge, die das Framework nicht kennen, bauen es nach. Werkzeuge, die es kennen, stoßen an Lücken und müssen entscheiden, was sie dort tun.

**Nicht Gegenstand:** Ausführbares BDD für die ganze Suite.

## Randbedingungen

- Die No-Hallucination-Regel und die Platzierungstabelle des Skills gelten.
- Neue Elemente entstehen im `UI/*.py` der App, mit Real Name aus Spy-Dump oder Quellcode.

## Akzeptanzkriterien

- **AK1** – Jede Szenariozeile ist einem vorhandenen Aufruf oder einer benannten Lücke zugeordnet.
- **AK2** – Für jede Lücke ist festgelegt, wo das fehlende Element entsteht und woher sein Real Name kommt.
- **AK3** – Step-Funktionen enthalten keine Squish-Aufrufe und keine Real Names.
- **AK4** – Prüfungen verwenden die Aufrufe aus der Routing-Tabelle.

## Hinweise

Einen Button `add_new_tractor_btn` nach dem Muster von `add_new_implement_btn` mit `objectName: "tractorAddNew"` anzulegen erfüllt AK2 nicht. Der Name ist geraten.

AK1 wird unbequem: Eine Lücke im Framework ist ein Befund, keine Aufgabe für den Agenten allein.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Gibt es das schon, und wenn nicht, wer entscheidet, wo es entsteht?**

---
---

# Addendum · Wege an einer Lücke

| Weg | wann |
|---|---|
| Spy-Dump nach Rückfrage | das Element existiert in der AUT, aber nicht im Framework |
| Real Name aus dem QML-Quellcode | Quellcode ist lesbar, `objectName` gesetzt |
| `# TODO: [helper-missing]` und Rückfrage | Spy abgelehnt oder nicht möglich |
| raten | nie |

Aus den Regeln des Teams: Ein Dump, der der generierten Übersicht widerspricht, ist ein Befund, keine Erlaubnis, den Test anzupassen.
