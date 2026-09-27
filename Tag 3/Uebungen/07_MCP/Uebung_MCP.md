# Übung · Eigener Server oder Squish MCP?

Sie untersuchen einen kleinen MCP-Server, der die Skripte Ihres Skills kapselt, erweitern ihn um ein Tool und vergleichen ihn mit dem Squish-MCP-Server der Qt Company. Die Frage ist, welcher Weg Ihre Leitplanken besser trägt.

---

## Material A · Der Beispielserver

`Beispiele/3-7_MCP_Server_minimal.py` (gekürzt), geschrieben für das Python-SDK `mcp` 2.2:

```python
from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations
from pydantic import BaseModel

server = MCPServer(name="squish-tests", instructions="Runs and evaluates single Squish test cases. ...")
_runs: dict[str, int] = {}


class RunResult(BaseModel):
    status: Literal["passed", "failed", "incomplete", "not_started", "refused", "timeout", "error"]
    testcase: str
    log_path: str | None = None
    summary: str
    runs_used: int


@server.tool(annotations=ToolAnnotations(read_only_hint=True))
def get_run_result(log_path: str) -> RunResult:
    """Summarise an existing squishrunner log: verdict, assertions in order, first failure."""
    ...


@server.tool(annotations=ToolAnnotations(read_only_hint=False, destructive_hint=True, idempotent_hint=False))
def run_testcase(target_ip: str, suite: str, testcase: str) -> RunResult:
    """Run one test case on a target. Takes the target exclusively and replaces its data set."""
    # Laufgrenze 2 je Testfall, Namensprüfung, Aufruf von run_testcase.sh,
    # neues Protokoll über <suite>__<testcase>__latest.log, Auswertung mit parse_run.py
    ...
```

---

## Material B · Squish MCP der Qt Company

- Die Squish-9.2-Dokumentation nennt zwei Wege für KI-Assistenten: squishrunner direkt über die Kommandozeile, oder das Squish-MCP-Beispiel, ausdrücklich als Vorabversion.
- Die offene Version auf GitHub kapselt im Kern die squishrunner-Kommandozeile. Sie kann Tests und Suiten ausführen und anlegen, Ergebnisse auswerten, Feature-Dateien und Step-Funktionen erzeugen. Eigene Regeln lassen sich in einer `SQUISH-RULES.yaml` hinterlegen.
- Laut Qt gibt es im Qt Customer Portal eine Version 0.2 mit Live-Zustand der Anwendung und UI-Interaktionswerkzeugen. Ihr Funktionsumfang ist ohne Kundenzugang nicht einsehbar.

---

## Material C · Leitplanken des Teams

| Nr. | Leitplanke |
|---|---|
| L1 | vor jedem Lauf fragen |
| L2 | höchstens 2 Läufe je Testfall |
| L3 | Assertions vor und nach Korrekturen vergleichen (`assertion_guard.py`) |
| L4 | Selector nicht ohne Spy-Dump ändern |
| L5 | keine Parallel-Helper, keine eigenen Real Names außerhalb der UI-Module |
| L6 | keine physischen oder Updater-Tests ausführen |

---

## Aufgabe

### Teil 1 · Lesen

**1.** Welche Teile von Material A sieht Claude Code, welche bleiben Implementierung des Servers?

**2.** Welche Leitplanken aus Material C setzt der Beispielserver durch, welche nicht?

**3.** Was passiert, wenn ein älteres Protokoll desselben Testfalls existiert und der neue Lauf an einer Vorbedingung scheitert? Wie verhindert der Server eine falsche Auswertung?

### Teil 2 · Erweitern

**4.** Entwerfen Sie ein Tool `spy_screen` für den Server: Parameter, Rückgabe, Annotationen. Welche Leitplanke könnte der Server damit zusätzlich durchsetzen?

**5.** Schreiben Sie die Signatur und den Docstring. Die Implementierung darf ein Kommentar bleiben.

### Teil 3 · Vergleichen

**6.** Tragen Sie für jede Leitplanke aus Material C ein, wie sie mit dem eigenen Server und mit Squish MCP umgesetzt würde.

**7.** Welche Fähigkeit hat Squish MCP, die der eigene Server nicht hat? Welche davon braucht Ihr Workflow?

**8.** Formulieren Sie eine Empfehlung mit Bedingung: „Wir nehmen …, solange …“

---

## Hinweise zur Bearbeitung

- Den Server in Material A nicht vollständig nachbauen. Es geht um den Vertrag.
- Für Squish MCP nur verwenden, was Material B belegt.
- Wenn Sie unsicher sind, fragen Sie: **Welche Leitplanke steht im Werkzeug, welche nur in einer Anweisung?**
