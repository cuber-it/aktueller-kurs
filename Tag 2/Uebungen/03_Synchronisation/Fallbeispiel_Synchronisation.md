# Fallbeispiel · Zeitannahmen in der Control-Schicht

**Situationstyp:** Synchronisation, die auf schneller Hardware unauffällig ist, beruht auf Annahmen über Zeit. Auf langsamerer Hardware werden sie sichtbar.

---

## Ausgangslage

Die Control-Schicht eines Squish-Frameworks kapselt Klicken, Warten und Lesen. `click_and_wait` klickt und wartet auf ein Zielobjekt, `get()` liest einen Wert über `get_property_value`.

## Wie es gewachsen ist

`click_and_wait` klickt erneut, wenn das Ziel nicht innerhalb einer halben Sekunde erscheint, vermutlich um verlorene Klicks aufzufangen. `get_property_value` prüft zuerst, ob das Objekt existiert, damit bei fehlenden Objekten keine Exception entsteht. Die Gefahr des Wiederholungsklicks bei umschaltenden Quellen hat das Team dokumentiert, samt empfohlener Variante für den Layout-Manager.

## Was auffällt

**Der Wiederholungsklick hängt an 500 ms.** Erscheint das Ziel später, folgt ein zweiter Klick. Bei einer umschaltenden Quelle wie `layout_manager_btn` schließt er das Panel wieder, auch in der empfohlenen Variante, wenn der OK-Button langsamer erscheint.

**Lesen wartet nicht.** `object.exists` prüft sofort. Ein Feld, das kurz nach der Navigation erscheint, ergibt „Found: None“, dieselbe Meldung wie ein fehlendes Objekt.

**Die Absicherung liegt beim Aufrufer.** Dokumentation und Abschlussliste des Skills sagen, wann `click_and_wait` nicht verwendet werden darf. Die Methode selbst verhindert es nicht.

## Naheliegende Ansätze

**`iteration_delay` erhöhen.** Verschiebt die Schwelle, beseitigt sie nicht.

**Mehr `snooze` vor dem Lesen.** Verdeckt das Problem und verlängert den Lauf.

## Diskussionsfragen

1. Warum beseitigt ein längeres `iteration_delay` das Problem nicht?
2. Wer sollte wissen, ob ein zweiter Klick harmlos ist: der Aufrufer, die Checkliste oder die Methode?
3. Was müsste „Found: None“ enthalten, damit die Ursache erkennbar ist?
4. Wo haben Sie so etwas?
