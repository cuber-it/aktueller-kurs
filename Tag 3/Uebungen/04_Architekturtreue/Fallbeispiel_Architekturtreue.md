# Fallbeispiel · Werkzeuge, die das Framework nicht kennen

**Situationstyp:** Ein Werkzeug erzeugt Tests, ohne das vorhandene Framework zu kennen. Es baut dessen Aufgaben nach und bildet fehlende Informationen nach Mustern.

---

## Ausgangslage

Ein Squish-Framework hat Controls, Screen Objects und Helper, und ein eigener Skill setzt Testfälle mit der Regel um, keine Namen zu erfinden. Fremde Werkzeuge wie ein MCP-Server für Squish können aus Szenarien Feature-Dateien und Step-Funktionen erzeugen.

## Wie es gewachsen ist

Squish zeichnet BDD-Schritte als Step-Funktionen mit direkten Squish-Aufrufen und einer eigenen Object Map auf. Werkzeuge, die darauf aufbauen, erzeugen dieselbe Form.

## Was auffällt

**Step-Funktionen umgehen das Framework.** Kein Control, kein Screen Object, kein Helper; Real Names stehen in einer zweiten Object Map.

**Fehlende Elemente werden nach Muster gebildet.** Einen Button zum Anlegen eines Traktors gibt es im Framework nicht. Nach dem Vorbild von `implementAddNew` entstünde ein plausibler, aber unbelegter Name.

**Die Lücke ist ein echter Befund.** Im eigenen Skill würde sie als `# TODO: [helper-missing]` sichtbar.

## Naheliegende Ansätze

**Die Regeldatei des fremden Werkzeugs mit eigenen Regeln füllen.** Sie kennt Regeln, aber nicht die Klassen des Frameworks.

## Diskussionsfragen

1. Was tut der eigene Skill an derselben Stelle?
2. Wer entscheidet, ob ein fehlender Button ergänzt wird, und wo?
3. Unter welchen Bedingungen wären Step-Funktionen im Framework sinnvoll?
4. Wo haben Sie so etwas?
