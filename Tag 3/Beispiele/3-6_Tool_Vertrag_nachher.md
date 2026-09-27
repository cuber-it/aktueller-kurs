# 3-6 · nachher · Dasselbe Werkzeug als MCP-Tool mit Vertrag

Eine mögliche Richtung. Der Vertrag entspricht dem Beispielserver `3-7_MCP_Server_minimal.py`.

## Tool-Vertrag `run_testcase`

| Teil | Inhalt |
|---|---|
| Name | `run_testcase` |
| Beschreibung | Run one test case on a target. Takes the target exclusively and replaces its data set. Not for tests with physical steps, updater tests or tests that need a simulation setup. |
| Annotationen | `read_only_hint: false`, `destructive_hint: true`, `idempotent_hint: false` |
| Parameter | `target_ip: str`, `suite: str` (muss `suite_…` sein), `testcase: str` (muss `tst_…` sein) |
| Rückgabe | `status`, `testcase`, `log_path`, `summary`, `runs_used` |
| `status` | `passed` · `failed` · `incomplete` · `not_started` · `refused` · `timeout` · `error` |
| Laufgrenze | 2 Läufe je Testfall, danach `refused` |

Die Status-Werte folgen der Ausgabe von `parse_run.py`: `PASS`, `FAIL` (auch „baselines missing only“), `INCOMPLETE`; Exit-Code 2 heißt, der Lauf hat nicht begonnen. `not_started` meldet auch Vorbedingungen, an denen `run_testcase.sh` vor dem Lauf abbricht.

## Tool-Vertrag `get_run_result`

| Teil | Inhalt |
|---|---|
| Annotationen | `read_only_hint: true` |
| Parameter | `log_path: str`, nur innerhalb von `RUN_CACHE` |
| Rückgabe | wie oben, `runs_used: 0` |

## Freigaben in Claude Code (`.claude/settings.json` im Repository)

```json
{
  "permissions": {
    "allow": ["mcp__squish-tests__get_run_result"],
    "ask":   ["mcp__squish-tests__run_testcase"],
    "deny":  ["Bash(*run_testcase.sh*)"]
  }
}
```

- Lesen des Ergebnisses ohne Rückfrage.
- Jeder Lauf fragt nach, auch wenn andere Werkzeuge freigegeben sind.
- Das Skript direkt über Bash ist gesperrt; der Weg führt nur über das Tool mit Vertrag.

## Was sich gegenüber vorher ändert

| Regel | vorher | nachher |
|---|---|---|
| Rückfrage vor dem Lauf | Modell befolgt Regel | Claude Code fragt (`ask`) |
| höchstens 2 Läufe | Modell befolgt Regel | Server verweigert den dritten |
| Ergebnis | Text | Struktur mit festem `status` |
| Fehlerarten | Meldungstext | `not_started`, `timeout`, `refused`, … |
| Umgehung über Bash | möglich | `deny` |
| keine physischen/Updater-Tests | Modell befolgt Regel | weiterhin Regel; im Server prüfbar, wenn der Testfall eine Kennzeichnung trägt |
