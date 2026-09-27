# Lösungsvorschlag · Eigener Server oder Squish MCP?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob die Empfehlung **an Leitplanken begründet** ist.

---

## 1 · Sichtbar für Claude Code

Servername und `instructions`, Toolnamen, Docstrings, Parameter mit Typen, Annotationen, das Schema von `RunResult`. Nicht sichtbar: `_runs`, die Namensprüfung, der Aufruf der Skripte, die Auswertung des Protokolls.

---

## 2 · Leitplanken im Beispielserver

| Leitplanke | im Server |
|---|---|
| L1 Rückfrage | nein, über Claude-Code-Freigabe `ask` |
| L2 zwei Läufe | ja |
| L3 Assertions vergleichen | nein |
| L4 Selector nur nach Spy | nein |
| L5 keine Parallel-Helper | nein, Server schreibt keinen Code |
| L6 keine physischen/Updater-Tests | nein; möglich über Suite-Namen |

---

## 3 · Älteres Protokoll

Der Server merkt sich die Startzeit. Ist `…__latest.log` älter, meldet er `not_started` mit der Ausgabe des Skripts, statt das alte Protokoll auszuwerten.

---

## 4 · `spy_screen`

| Teil | Inhalt |
|---|---|
| Parameter | `target_ip`, `app`, `properties: dict[str, str]` |
| Rückgabe | bis zu 20 passende Objekte mit Real Name und Typ |
| Annotationen | `read_only_hint: false`, `destructive_hint: false` (belegt Target, verändert es nicht) |

Zusätzliche Leitplanke: Der Server merkt sich je Testfall, ob `spy_screen` aufgerufen wurde. Ein Lauf nach einer Selector-Änderung ohne vorherigen Spy wird verweigert, sofern der Server die Änderung erkennt (etwa über den Vergleich mit dem letzten Stand von `test.py`).

---

## 5 · Signatur

```python
@server.tool(annotations=ToolAnnotations(read_only_hint=False, destructive_hint=False))
def spy_screen(target_ip: str, app: str, properties: dict[str, str]) -> list[dict[str, str]]:
    """Find objects on the running AUT screen that match the given properties.

    Takes the target exclusively and a Squish license seat for the duration of the dump.
    Returns at most 20 matches with real name and type. The dump itself is not returned.
    """
    # spy_dump.sh mit SPY_APPS=app, dann find_object.py mit den Eigenschaften
```

---

## 6 · Vergleich

| Leitplanke | eigener Server | Squish MCP |
|---|---|---|
| L1 | Freigabe `ask` | Freigabe `ask` |
| L2 | Zähler im Server | Anweisung oder Schicht davor |
| L3 | `assertion_guard.py` wie heute | wie heute |
| L4 | Spy-Tool mit Merker | Anweisung |
| L5 | kein Code-Tool | Step-Funktionen und Real Names erzeugt der Server selbst: widerspricht L5 |
| L6 | Prüfung über Suite-Namen | Anweisung |

---

## 7 · Fähigkeiten von Squish MCP

Tests und Suiten anlegen, Feature-Dateien und Step-Funktionen erzeugen; in 0.2 Live-Zustand und UI-Interaktion. Der Workflow braucht davon höchstens den Live-Zustand, als Ersatz für den Spy-Dump. Anlegen und Step-Funktionen widersprechen L5.

---

## 8 · Empfehlung

Eigener Server mit drei Tools, **solange** der Workflow nur ausführen, auswerten und spähen muss. Squish MCP 0.2 prüfen, ob sein Live-Zustand den Spy-Dump ersetzen kann; falls ja, hinter dem eigenen Server nutzen.

---

## Diskussionsanschluss

Wer im Team fragt die Portal-Version an, und mit welcher Prüfliste?
