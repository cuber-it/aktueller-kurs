# Pro und Contra · Einmal klicken, lesen mit Warten

Bewertet wird der Vorschlag aus dem Lösungspapier: `click_and_wait` klickt einmal, Wiederholen nur über `click_while_exists`, `get_property_value` wartet auf das Objekt.

---

## Pro

**Unabhängig von der Geschwindigkeit der Hardware**
Warten auf Zustand statt auf Zeit. Auf langsamerer Hardware entstehen weder ein zweiter Klick noch „Found: None“.

**Klare Meldungen**
„Layout Manager OK Button did not appear after clicking Layout Manager Button“ statt Erfolg mit geschlossenem Panel. „Turn Radius did not appear“ statt „Found: None“.

**Die Regel wird überflüssig**
Punkt 6c der Abschlussliste und der Warnabschnitt in den Coding-Regeln entfallen. Weder Mensch noch Skill müssen sich daran erinnern.

**Kein Anlass für neue `snooze`**
Wer „Found: None“ sieht, greift leicht wieder zu einem `snooze`. Lesen mit Warten nimmt diesen Anlass, die eigene Snooze-Regel bleibt leichter einzuhalten.

**Wiederholen bleibt möglich**
Wo Klicks verloren gehen, gibt es mit `click_while_exists` einen sicheren Weg.

---

## Contra

**Verlorene Klicks werden sichtbar**
Tests, die heute durch den zweiten Klick grün werden, werden rot. Welche das sind, ist unbekannt.

**Abbruch statt Weiterlaufen**
`raise_exception=True` beendet den Test. Heute läuft er nach einem FAIL weiter und sammelt weitere Befunde.

**Coding-Regeln müssen mit**
Die Regeln beschreiben das heutige Verhalten mit „wrong“ und „right“. Nach der Änderung sind beide Beispiele gleichwertig, die Regeln müssen das sagen.

**Kurzer Lese-Timeout kann zu kurz sein**
5 s sind ein Vorschlag. Menüs mit langen Ladezeiten brauchen einen eigenen Wert.

---

## Bewertung

Der Vorschlag trägt, weil **die Fehler aus Annahmen über Zeit entstehen**, die jede neue Hardware verletzen kann.

Gegenprobe – *nur `iteration_delay` und Timeouts erhöhen, bleiben Nachteile?* Ja: Die Schwelle verschiebt sich, der zweite Klick bleibt möglich, „Found: None“ bleibt eine irreführende Meldung.

**Die Grenzen:**

1. **Übergang.** Vor der Umstellung einen Lauf mit Protokollierung jedes zweiten Klicks, um betroffene Tests zu finden.
2. **Abbruch oder Weiterlaufen.** Ob ein fehlendes Objekt den Test beendet, ist eine Teamentscheidung (2-7).
3. **Animationen.** Wo kein Zustand abfragbar ist, bleibt ein begründetes `snooze`.

---

## Diskussionsfragen

1. Wie finden Sie die Tests, die heute vom zweiten Klick abhängen?
2. Soll ein fehlendes Objekt den Test beenden oder nur einen FAIL eintragen?
3. Wie lang sollte der Lese-Timeout sein, und wer legt ihn je Menü fest?
4. Welche Zeile der Coding-Regeln ändern Sie zuerst?
