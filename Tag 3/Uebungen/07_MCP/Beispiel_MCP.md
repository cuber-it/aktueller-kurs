# Beispiel · Eigener Server oder fertiger? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Agent bucht Besprechungsräume. Es gibt einen fertigen MCP-Server für das Kalendersystem mit 18 Tools (Termine lesen, anlegen, verschieben, löschen, Teilnehmer verwalten). Leitplanken des Teams: nur Räume, nie Personenkalender; nicht mehr als zwei Stunden; keine Buchung vor 7 Uhr.

---

## Schritt 1 · Eigener Server mit zwei Tools

```python
from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations

server = MCPServer(name="room-booking")
ROOMS = {"Elbe", "Alster", "Bille"}


@server.tool(annotations=ToolAnnotations(read_only_hint=True))
def list_free_rooms(date: str, start: str, end: str) -> list[str]:
    """Rooms that are free for the whole slot."""
    ...


@server.tool(annotations=ToolAnnotations(read_only_hint=False, destructive_hint=False))
def book_room(room: str, date: str, start: str, end: str, title: str) -> str:
    """Book a meeting room. At most two hours, not before 07:00."""
    if room not in ROOMS:
        return "refused: unknown room"
    ...
```

---

## Schritt 2 · Vergleich

| Leitplanke | fertiger Server | eigener Server |
|---|---|---|
| nur Räume | Freigabe je Tool, Personenkalender über dieselben Tools erreichbar | Parameter `room` aus fester Liste |
| höchstens zwei Stunden | Anweisung an das Modell | Prüfung im Tool |
| nicht vor 7 Uhr | Anweisung an das Modell | Prüfung im Tool |
| Pflege | Hersteller | Team |

---

## Schritt 3 · Empfehlung

Eigener Server, solange der Agent nur Räume bucht. Wenn er auch Einladungen verwalten soll, fertiger Server mit eigenem Server davor, der die Leitplanken prüft.

---

## Was dieses Beispiel zeigt

**Fähigkeiten zählen weniger als Grenzen.** 18 Tools helfen nicht, wenn eines davon Personenkalender löschen kann.

**Leitplanken im Parameter sind am stärksten.** Ein Raum, der nicht in der Liste steht, kann nicht gebucht werden.

**Kombinieren geht.** Ein eigener Server kann einen fremden kapseln.
