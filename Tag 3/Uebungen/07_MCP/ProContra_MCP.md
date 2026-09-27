# Pro und Contra · Eigener Server mit drei Tools, Squish MCP als mögliche Quelle dahinter

Bewertet wird der Vorschlag aus dem Lösungspapier.

---

## Pro

**Leitplanken im Werkzeug**
Laufgrenze und Spy-Merker gelten unabhängig vom Modell.

**Keine zweite Architektur**
Der Server erzeugt keinen Code, das bleibt beim Skill.

**Klein und verständlich**
Drei Tools um vorhandene Skripte, ein Nachmittag Arbeit für den Kern.

**Offen für Squish MCP**
Wenn die Portal-Version den Spy-Dump ersetzen kann, lässt sie sich dahinter einsetzen.

---

## Contra

**Pflege durch das Team**
Änderungen an Skripten, SDK-Updates (der Wechsel von `FastMCP` zu `MCPServer` in `mcp` 2.x zeigt, dass das vorkommt).

**Weniger Fähigkeiten**
Keine Live-Interaktion mit der Oberfläche.

**Doppelte Arbeit, falls Squish MCP später alles kann**
Der eigene Server wird dann überflüssig.

---

## Bewertung

Der Vorschlag trägt, weil **die Leitplanken des Teams den Ausschlag geben**, nicht die Zahl der Fähigkeiten.

Gegenprobe – *Squish MCP direkt einsetzen, Leitplanken per Regeldatei, bleiben Nachteile?* Ja: L2, L4, L6 hängen am Modell, L5 widerspricht dem, was der Server erzeugt.

**Die Grenzen:**

1. **SDK-Version festhalten** und bei Updates prüfen.
2. **Portal-Version gegen die Leitplanken prüfen**, nicht gegen die Fähigkeitenliste.
3. **Bash-Freigaben zuerst**, der Server folgt.

---

## Diskussionsfragen

1. Reicht der Spy-Dump, oder brauchen Sie Live-Interaktion?
2. Wer pflegt den Server?
3. Wie würden Sie Squish MCP hinter dem eigenen Server einbinden?
4. Welche Leitplanke fehlt in der Liste?
