# Übung · Welche Variante für welches Problem?

Sie vergleichen Architekturvarianten an einem Szenario aus Ihrem Framework. Keine Variante wird eingeführt. Die Frage ist, welche Variante welche Änderung leichter macht und was sie kostet.

---

## Material A · Das Szenario im heutigen Stand

„GNSS-Quelle SAE J1939 wählen und prüfen, dass sie ausgewählt ist.“

```python
open_gnss_source_submenu()
masetth.submenu_gnss_source.sae_j1939_btn.set(True)
UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn).test(True)
```

`open_gnss_source_submenu()` ist ein Helper, `submenu_gnss_source` ein Screen Object, `sae_j1939_btn` ein Control.

---

## Material B · Zahlen aus dem Bestand

| Was | Anzahl |
|---|---:|
| Testfälle | 983 |
| Testfälle mit direktem Squish-Aufruf (außer `snooze`) | 0 |
| Screen Objects (`SubMenu…`-Klassen) in den Maschineneinstellungen | 16 |
| Helper-Funktionen mit fachlichem Namen (Auswahl) | `open_gnss_source_submenu`, `close_machine_settings_menus`, … |
| Screenplay-Elemente (Actor, Ability, Question) | 0 |

---

## Material C · Ein Vorschlag zur Diskussion

Ein Vorschlag, wie er in Teams häufig aufkommt:

> „Mit Screenplay hätten wir Rollen: Fahrer, Servicetechniker. Jede Rolle hat Fähigkeiten. Tests lesen sich wie Anforderungen. Wir sollten alles darauf umstellen.“

---

## Material D · Vier Change Cases

| Nr. | Änderung |
|---|---|
| C1 | Die GNSS-Quelle wird künftig über eine Auswahlliste im Menü Zugfahrzeug gewählt, das Untermenü entfällt. |
| C2 | Der `objectName` des Eintrags SAE J1939 ändert sich. |
| C3 | Ein Servicetechniker sieht zusätzliche Quellen, die ein Fahrer nicht sieht. |
| C4 | Dieselbe Auswahl soll auch über das Virtual Terminal (zweite AUT) getestet werden. |

---

## Aufgabe

### Teil 1 · Varianten skizzieren

**1.** Skizzieren Sie das Szenario als direkten Testcode, mit Screen Objects ohne Helper, mit Screen Objects und Tasks, mit Screenplay. Wenige Zeilen je Variante genügen.

**2.** Welche Variante entspricht dem heutigen Stand? Wo mischt er Varianten?

### Teil 2 · Change Cases

**3.** Tragen Sie für jede Variante und jeden Change Case ein, welche Stellen sich ändern.

**4.** Welcher Change Case unterscheidet die Varianten am stärksten?

### Teil 3 · Entscheiden

**5.** Welche neuen Konzepte bringt Screenplay gegenüber dem heutigen Stand? Was davon ist im Bestand schon in anderer Form vorhanden?

**6.** Nehmen Sie Stellung zum Vorschlag aus Material C. Unter welchen Umständen würden Sie Screenplay an einer Stelle ergänzen?

**7.** Formulieren Sie eine Teamregel zur Wahl der Variante für neue Tests.

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden.
- Varianten sind keine Reifegrade. „Direkt“ ist nicht schlechter als „Screenplay“.
- Wenn Sie unsicher sind, fragen Sie: **Welche Änderung macht diese Variante leichter, und was kostet sie?**
