"""3-7 · Minimaler MCP-Server um die vorhandenen Testskripte des Teams

Eine mögliche Richtung, akademisches Beispiel. Getestet gegen das offizielle Python-SDK
`mcp` in Version 2.2 (dort heißt die frühere Klasse FastMCP jetzt MCPServer).

Der Server kapselt zwei vorhandene Skripte als Tools:

- get_run_result  liest ein Protokoll über parse_run.py. Nur lesend.
- run_testcase    führt einen Testfall über run_testcase.sh aus. Verändert das Target:
                  exklusiv, Lizenzplatz, der Datensatz des Terminals wird ersetzt.

Was heute als Kommentar im Skript oder als Regel im Skill steht, steht hier im Vertrag:
Annotationen (lesend oder verändernd), typisierte Parameter, strukturierte Rückgabe,
unterscheidbare Fehler und eine Laufbegrenzung je Testfall. Die Rückfrage vor dem Lauf
übernimmt Claude Code: Ein MCP-Tool, das nicht ausdrücklich freigegeben ist, wird erst
nach Bestätigung aufgerufen.

Start in Claude Code, etwa:
    claude mcp add squish-tests -- python 3-7_MCP_Server_minimal.py
"""
import os
import re
import subprocess
import time
from pathlib import Path
from typing import Literal

from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations
from pydantic import BaseModel

SCRIPTS = Path(os.environ.get("TESTCASE_SCRIPTS", "scripts"))
RUN_CACHE = Path(os.environ["RUN_CACHE"])          # dasselbe Verzeichnis wie für run_testcase.sh
MAX_RUNS_PER_TESTCASE = 2
RUN_TIMEOUT_S = 30 * 60

server = MCPServer(
    name="squish-tests",
    instructions=(
        "Runs and evaluates single Squish test cases. Read a result before running again. "
        "A test case may be run at most twice per session; after that, report to the engineer."
    ),
)

_runs: dict[str, int] = {}


class RunResult(BaseModel):
    status: Literal["passed", "failed", "incomplete", "not_started", "refused", "timeout", "error"]
    testcase: str
    log_path: str | None = None
    summary: str
    runs_used: int


def _status_from(returncode: int, text: str) -> str:
    """parse_run.py: exit 0 = PASS, 1 = FAIL or INCOMPLETE, 2 = run did not start."""
    if returncode == 2:
        return "not_started"
    match = re.search(r"^verdict : (\w+)", text, re.MULTILINE)
    verdict = match.group(1) if match else ""
    return {"PASS": "passed", "FAIL": "failed", "INCOMPLETE": "incomplete"}.get(verdict, "error")


def _parse(log_path: Path) -> tuple[str, str]:
    completed = subprocess.run(
        ["python3", str(SCRIPTS / "parse_run.py"), str(log_path)],
        capture_output=True, text=True, timeout=60,
    )
    text = completed.stdout.strip() or completed.stderr.strip()
    return _status_from(completed.returncode, text), text


@server.tool(annotations=ToolAnnotations(read_only_hint=True))
def get_run_result(log_path: str) -> RunResult:
    """Summarise an existing squishrunner log: verdict, assertions in order, first failure."""
    path = Path(log_path)
    if not path.is_file() or RUN_CACHE not in path.resolve().parents:
        return RunResult(status="refused", testcase="", summary=f"no log in {RUN_CACHE}: {log_path}", runs_used=0)
    verdict, text = _parse(path)
    return RunResult(status=verdict, testcase=path.stem, log_path=str(path), summary=text, runs_used=0)


@server.tool(annotations=ToolAnnotations(read_only_hint=False, destructive_hint=True, idempotent_hint=False))
def run_testcase(target_ip: str, suite: str, testcase: str) -> RunResult:
    """Run one test case on a target. Takes the target exclusively and replaces its data set.

    Not for tests with physical steps, updater tests or tests that need a simulation setup.
    """
    key = f"{suite}/{testcase}"
    used = _runs.get(key, 0)
    if used >= MAX_RUNS_PER_TESTCASE:
        return RunResult(status="refused", testcase=key, runs_used=used,
                         summary=f"run limit of {MAX_RUNS_PER_TESTCASE} reached - hand back to the engineer")
    if not re.fullmatch(r"suite_\w+", suite) or not re.fullmatch(r"tst_\w+", testcase):
        return RunResult(status="refused", testcase=key, runs_used=used, summary="invalid suite or test case name")

    _runs[key] = used + 1
    started = time.time()
    try:
        completed = subprocess.run(
            [str(SCRIPTS / "run_testcase.sh"), target_ip, suite, testcase],
            capture_output=True, text=True, timeout=RUN_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return RunResult(status="timeout", testcase=key, runs_used=_runs[key],
                         summary=f"no result after {RUN_TIMEOUT_S} s")

    latest = RUN_CACHE / f"{suite}__{testcase}__latest.log"      # angelegt von run_testcase.sh
    if not latest.exists() or latest.resolve().stat().st_mtime < started:
        # Kein neues Protokoll: Vorbedingung nicht erfüllt (Testfall fehlt, keine Lizenz, Target
        # nicht erreichbar). run_testcase.sh bricht dann vor dem Lauf ab und sagt warum.
        # Ein älteres Protokoll desselben Testfalls wird bewusst nicht ausgewertet.
        return RunResult(status="not_started", testcase=key, runs_used=_runs[key],
                         summary=(completed.stdout + completed.stderr)[-2000:])
    log = latest.resolve()
    status, text = _parse(log)
    return RunResult(status=status, testcase=key, log_path=str(log), summary=text, runs_used=_runs[key])


if __name__ == "__main__":
    server.run()
