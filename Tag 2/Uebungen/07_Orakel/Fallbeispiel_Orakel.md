# Fallbeispiel · Setzen und Prüfen in einem Aufruf

**Situationstyp:** Aktion und Prüfung stehen in einem Aufruf. Scheitert die Aktion, melden die folgenden Prüfungen Abweichungen, und die Ursache geht zwischen ihnen unter.

---

## Ausgangslage

Geometrie-Tests setzen Werte wie Wenderadius, Arbeitsbreite und Vorgewende und lesen sie zurück. Ein Verifikationsobjekt erledigt beides: `test(value, set_setting=True)`.

## Wie es gewachsen ist

Setzen und Zurücklesen kam in vielen Tests vor, der Parameter `set_setting=True` spart eine Zeile. Er wird heute 16-mal verwendet. Prüfungen tragen bei Abweichung einen FAIL ein und lassen den Test weiterlaufen, damit ein Lauf möglichst viele Befunde liefert.

## Was auffällt

**Eine gescheiterte Eingabe erzeugt mehrere Meldungen.** Öffnet die Bildschirmtastatur nicht, trägt `click_with_entry` „Keyboard didn't open“ ein. Der Test läuft weiter, jede folgende Prüfung meldet eine Abweichung.

**Die Ursache steht im Protokoll, aber nicht allein.** Eine Tastaturmeldung zwischen mehreren Abweichungen wirkt nebensächlich.

**Die gefundenen Werte sind ein Hinweis.** Stehen nach dem Setzen die Werkswerte im Feld, ist das Setzen gescheitert, nicht das Speichern.

## Naheliegende Ansätze

**Videoaufzeichnung der Läufe.** Zeigt die Ursache, kostet aber Speicher und Auswertungszeit.

**Mehr Logging in `set()`.** Die Zeilen stehen im Protokoll, aber zwischen vielen anderen.

## Diskussionsfragen

1. Warum geht die Tastaturmeldung leicht unter?
2. Soll ein Testschritt nach einer gescheiterten Aktion abbrechen?
3. Wer ist zuständig zu melden, dass eine Eingabe nicht ankam?
4. Wo haben Sie so etwas?
