# Fallbeispiel · Regeln aus Einzelfällen

**Situationstyp:** Regeln werden aus einzelnen Problemen abgeleitet. Sie treffen das Symptom und verhindern zugleich sinnvolle Lösungen.

---

## Ausgangslage

Ein Team will Regeln für neuen Testcode festlegen. Anlass sind schwer verständliche Helper: ein Beispiel mit 180 Zeilen mischt Navigation, Eingaben und Prüfungen.

## Wie es gewachsen ist

Naheliegend ist, zu jedem Problem eine Regel zu formulieren, etwa „Helper-Funktionen haben höchstens 20 Zeilen“.

## Was auffällt

**Das Problem ist nicht die Länge.** Der Helper mit 180 Zeilen mischt Verantwortungen. Ein Weg durch sieben Untermenüs mit 60 Zeilen ohne Verzweigung hat eine Verantwortung.

**Die Regel nennt kein Problem.** Sie nennt ein Symptom. Um sie einzuhalten, würde ein geradliniger Weg auf mehrere Funktionen verteilt, die sich gegenseitig aufrufen.

**Funktionierende Entscheidungen werden nicht aufgeschrieben.** Dass Tests Squish nicht direkt aufrufen, steht nirgends als Regel, obwohl sich alle daran halten.

## Naheliegende Ansätze

**Ausnahmen zur Regel („außer für Workflows“).** Die Grenze zwischen Helper und Workflow ist unklar.

## Diskussionsfragen

1. Welche Regel würde das eigentliche Problem treffen?
2. Warum sollten funktionierende Entscheidungen als Regel aufgeschrieben werden?
3. Wie unterscheiden Sie Symptom und Problem?
4. Wo haben Sie so etwas?
