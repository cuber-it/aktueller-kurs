# Beispiel · Welche Werkzeuge, mit welchen Grenzen? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Agent pflegt eine Webanwendung und soll sie auf eine Testumgebung ausliefern können. Vorhanden sind drei Skripte:

| Skript | Wirkung |
|---|---|
| `build.sh` | baut das Paket |
| `deploy.sh <umgebung>` | liefert aus, Umgebung ist 10 Minuten nicht erreichbar |
| `status.sh <umgebung>` | liest den Zustand |

---

## Schritt 1 · Einordnen

| Tool | Wirkung | Freigabe |
|---|---|---|
| `build` | verändert lokal | `allow` |
| `get_status` | liest | `allow` |
| `deploy` | zerstörend für die Dauer | `ask` |

---

## Schritt 2 · Vertrag für `deploy`

| Teil | Inhalt |
|---|---|
| Parameter | `environment: Literal["test", "staging"]` (Produktion ist kein Wert) |
| Rückgabe | `status: deployed / failed / refused / busy`, `version`, `summary` |
| Grenze | `busy`, wenn in der letzten Stunde schon ausgeliefert wurde |
| Annotationen | `destructive_hint: true` |

---

## Schritt 3 · Freigaben

```json
{
  "permissions": {
    "allow": ["mcp__deploy__build", "mcp__deploy__get_status"],
    "ask":   ["mcp__deploy__deploy"],
    "deny":  ["Bash(*deploy.sh*)"]
  }
}
```

---

## Was dieses Beispiel zeigt

**Der Parameter verhindert, was die Regel verbietet.** Produktion ist kein erlaubter Wert.

**Die Grenze steht im Tool.** „Nicht öfter als einmal pro Stunde“ zählt der Server.

**`deny` schließt den Umweg.** Sonst ruft der Agent das Skript direkt.
