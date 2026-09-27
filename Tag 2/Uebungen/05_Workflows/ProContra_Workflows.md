# Pro und Contra · Zugriff je Typ, Tasks, Workflow

Bewertet wird der Vorschlag aus dem Lösungspapier: `ParameterAccess` je Control-Typ, Tasks als Funktionen, Workflow mit Funktionsparameter.

---

## Pro

**Eine neue Aktion ändert keinen Bestand**
Die Werkswerte sind `set_parameter` mit anderer Referenz. Vorher: fünf Methoden.

**Ein neuer Control-Typ ist ein Eintrag**
Lesen und Setzen an einer Stelle.

**Der Weg ist von der Aktion unabhängig**
`for_each_implement_parameter` kennt keine `TestAction`.

**Fehler sind lokal**
Ein Fehler beim Setzen von Schaltern steht in `_write_check`, nicht in einem von fünfzehn Zweigen.

---

## Contra

**Lambdas und Tabellen sind ungewohnt**
Wer bisher Methoden je Typ gelesen hat, muss sich an `ACCESS[type(control)]` gewöhnen.

**`type(control)` ist streng**
Eine Unterklasse eines Controls (`NumericTextFieldDelegate` erbt von `TextFieldDelegate`) findet keinen Eintrag. Entweder eigener Eintrag oder Suche über die MRO.

**Sonderfälle wandern**
„Off“ → „0.00“ beim Setzen und das Auffüllen mit Nullen beim Vergleich gehören irgendwohin, in den Zugriff oder den Task.

**Umstellung aller Aufrufer**
Tests, die `MachineSettingsParameterTests` nutzen, müssen umgestellt werden.

---

## Bewertung

Der Vorschlag trägt, weil **zwei Änderungsrichtungen belegt sind**: drei Aktionen sind schon gekommen, eine vierte ist angekündigt.

Gegenprobe – *nur einen fünften Zweig einbauen, bleiben Nachteile?* Ja: Die fünfte Aktion kostet wieder fünf Stellen, und ein Fehler wie beim Setzen der Schalter kann wieder zwei Wochen unentdeckt bleiben.

**Die Grenzen:**

1. **Unterklassen.** Den Zugriff über die MRO suchen oder Einträge vollständig halten.
2. **Sonderfälle.** Festlegen, ob sie zum Zugriff oder zum Task gehören.
3. **Übergang.** Die alte Klasse kann die neuen Funktionen intern aufrufen, bis alle Tests umgestellt sind.

---

## Diskussionsfragen

1. Gehört „Off“ → „0.00“ zum Zugriff oder zum Task?
2. Soll `ACCESS` über die MRO suchen?
3. Welche Tests würden Sie zuerst umstellen?
4. Welche weitere Aktion sehen Sie kommen?
