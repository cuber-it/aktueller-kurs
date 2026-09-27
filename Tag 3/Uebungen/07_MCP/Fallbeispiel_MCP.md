# Fallbeispiel · Fertiger oder eigener Server

**Situationstyp:** Ein abgesicherter Workflow soll um ein Werkzeug erweitert werden. Ein fertiges Werkzeug kann mehr, ein eigenes passt besser.

---

## Ausgangslage

Ein Claude-Code-Skill setzt Testfälle in Squish-Tests um und führt sie über Skripte aus. Testläufe sollen technisch abgesichert werden.

## Wie es gewachsen ist

Es gibt zwei Wege: Squish MCP der Qt Company, das Tests startet, Suiten anlegt und Feature-Dateien schreibt, in einer neueren Version mit Zugriff auf die laufende Oberfläche; oder ein kleiner eigener Server mit wenigen Tools um die vorhandenen Skripte.

## Was auffällt

**Die Diskussion geht um Fähigkeiten, nicht um Grenzen.** Squish MCP kann mehr; der eigene Server zählt Läufe und gibt einen festen Status zurück.

**Die Rückfrage vor dem Lauf ist bei beiden gleich.** Sie kommt aus Claude Code, nicht aus dem Server.

**Squish MCP kennt Squish, nicht das Framework.** Es erzeugt eigene Real Names und Step-Funktionen.

**Die neuere Version ist ohne Kundenzugang nicht einsehbar.**

## Naheliegende Ansätze

**Squish MCP mit eigener Regeldatei.** Die Regeln werden beachtet, die Klassen des Frameworks bleiben unbekannt.

## Diskussionsfragen

1. Welche Frage entscheidet zwischen beiden Wegen?
2. Lassen sich beide kombinieren?
3. Was müsste die neuere Version können, damit sie den eigenen Server ersetzt?
4. Wo haben Sie so etwas?
