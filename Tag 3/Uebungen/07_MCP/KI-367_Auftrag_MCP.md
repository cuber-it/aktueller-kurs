# KI-367 · Eigenen MCP-Server und Squish MCP vergleichen

**Typ:** Spike
**Komponente:** KI-Werkzeuge
**Priorität:** Mittel
**Verweist auf:** KI-356 (Testläufe absichern)

---

## Story

**Als** Teamleitung Testautomatisierung
**möchte ich** wissen, ob wir einen eigenen MCP-Server um unsere Skripte bauen oder Squish MCP einsetzen,
**damit** wir die Leitplanken unseres Workflows mit dem geringsten Aufwand technisch absichern.

---

## Description

KI-356 verlangt, Testläufe technisch abzusichern. Zwei Wege liegen vor: ein kleiner eigener Server, der die vorhandenen Skripte kapselt, oder Squish MCP der Qt Company.

**Bestand:**

| Was | Stand |
|---|---|
| eigener Beispielserver | 2 Tools, gegen `mcp` 2.2 getestet |
| Squish MCP, offene Version | Vorabversion, kapselt squishrunner |
| Squish MCP 0.2 | im Qt Customer Portal, Umfang nicht geprüft |
| Leitplanken des Workflows | 6 |

**Befund:** Squish MCP erzeugt Step-Funktionen und Real Names selbst und kennt die Klassen des Frameworks nicht. Laufbegrenzung und Rückfrage vor dem Lauf bringt es nicht mit; die Rückfrage lässt sich über Claude-Code-Freigaben ergänzen.

**Befund zur Entstehung:** Squish MCP kennt Squish, nicht das Framework des Teams. Der eigene Server kennt das Framework, kann aber weniger.

**Nicht Gegenstand:** Die Umsetzung.

## Randbedingungen

- Die Leitplanken aus dem Skill gelten weiter.
- Wartung durch das Team ist begrenzt.
- Portal-Version 0.2 kann für den Vergleich angefragt werden.

## Akzeptanzkriterien

- **AK1** – Für jede Leitplanke ist angegeben, wie sie mit beiden Wegen umgesetzt würde.
- **AK2** – Fähigkeiten von Squish MCP, die der Workflow braucht, sind benannt.
- **AK3** – Der eigene Server ist um ein Tool für den Spy-Dump entworfen.
- **AK4** – Die Empfehlung nennt die Bedingung, unter der sie gilt.

## Hinweise

„Squish MCP ist offiziell“ erfüllt AK4 nicht.

AK1 wird unbequem: Manche Leitplanken lassen sich mit beiden Wegen nur über Claude-Code-Freigaben durchsetzen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche Leitplanke steht im Werkzeug, welche nur in einer Anweisung?**

---
---

# Addendum · Teile eines MCP-Servers

| Teil | sichtbar für den Agenten |
|---|---|
| Name und `instructions` des Servers | ja |
| Toolname, Docstring, Parameter mit Typen | ja |
| Annotationen | ja, Client kann sie für Freigaben nutzen |
| Rückgabeschema | ja |
| Zähler, Prüfungen, Aufruf der Skripte | nein |

Die Rückfrage vor einem Aufruf stellt der Client (Claude Code), nicht der Server.
