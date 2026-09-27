# Fallbeispiel · Eine Prüfung nach Namen für eine Regel nach Verhalten

**Situationstyp:** Eine Regel ist dokumentiert und hat eine Prüfung. Die Prüfung erkennt nur einen Teil der Fälle, das dokumentierte Beispiel gehört nicht dazu.

---

## Ausgangslage

Generierte Squish-Tests laufen vor dem Merge durch ein statisches Prüfskript. Es arbeitet nach dem Grundsatz „never guess“: lieber nichts melden als falsch melden.

## Wie es gewachsen ist

Die Regel „kein `click_and_wait` auf umschaltenden Quellen“ steht in den Coding-Regeln, mit dem Layout-Manager als Beispiel, und als Punkt 6c in der Abschlussliste. Das Prüfskript erkennt Umschalter am Namen: Endung `_toggle` oder `_switch`.

## Was auffällt

**Die Prüfung ist nach Namen gebaut, die Regel nach Verhalten.** Ob ein Control umschaltet, steht nicht im Namen.

**Das dokumentierte Beispiel fällt durch.** `layout_manager_btn` endet auf `_btn`.

**Die Abschlussliste hilft nur, wenn das Modell sie befolgt.**

## Naheliegende Ansätze

**Den Button umbenennen.** `layout_manager_toggle` würde erkannt, bricht aber 13 Aufrufe und die Coding-Regeln.

## Diskussionsfragen

1. Wie ließe sich eine Prüfung gegen die Beispiele der Coding-Regeln testen?
2. Ist eine Liste bekannter Umschalter besser als die Namensregel?
3. Welche Regeln lassen sich gar nicht statisch prüfen?
4. Wo haben Sie so etwas?
