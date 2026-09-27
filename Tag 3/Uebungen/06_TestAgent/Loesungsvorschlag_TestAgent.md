# Lösungsvorschlag · Welche Werkzeuge, mit welchen Grenzen?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **jede Wirkung eine passende Freigabe** hat und **Regeln im Tool** stehen, wo es möglich ist.

---

## 1 · Tools

| Skript | wird |
|---|---|
| `run_testcase.sh` | Tool `run_testcase` |
| `parse_run.py` | Tool `get_run_result` |
| `spy_dump.sh` + `find_object.py` | Tool `spy_screen` (Dump und Abfrage in einem) |
| `fetch_testcase.py` | Tool `get_testcase` oder bleibt Bash (lesend) |
| `check_test.py`, `assertion_guard.py` | bleiben Bash (lesend, lokal) |

---

## 2 · Wirkung

| Tool | Wirkung |
|---|---|
| `get_testcase`, `get_run_result` | lesend |
| `spy_screen` | belegt Target, verändert es nicht |
| `run_testcase` | zerstörend (Datensatz) |

---

## 3 · Vertrag `run_testcase`

| Teil | Inhalt |
|---|---|
| Parameter | `target_ip: str`, `suite: str` (Muster `suite_\w+`), `testcase: str` (Muster `tst_\w+`) |
| Rückgabe | `status`, `testcase`, `log_path`, `summary`, `runs_used` |
| `status` | `passed`, `failed`, `incomplete`, `not_started`, `refused`, `timeout`, `error` |
| Annotationen | `destructive_hint: true`, `idempotent_hint: false` |

`not_started`: `parse_run.py` Exit 2 oder kein neues Protokoll (Vorbedingung nicht erfüllt). `refused`: Laufgrenze oder ungültiger Name.

---

## 4 · Regeln im Tool

| Regel | im Tool? |
|---|---|
| vorher fragen | über Freigabe `ask` |
| keine physischen/Updater-Tests | ja, wenn der Testfall eine Kennzeichnung trägt (etwa Suite-Name `suite_Updater`) |
| höchstens 2 Läufe | ja, Zähler im Server |
| erlaubte Korrekturen | nein, Urteil |
| Selector nur nach Spy | teilweise: Server kann merken, ob `spy_screen` vor einem Lauf mit geändertem Selector aufgerufen wurde |

---

## 5 · Vertrag `spy_screen`

| Teil | Inhalt |
|---|---|
| Parameter | `target_ip`, `app` (Anwendung), `query` (Eigenschaften des gesuchten Objekts) |
| Rückgabe | Liste passender Objekte mit Real Name und Typ, höchstens 20 |
| Wirkung | belegt das Target für die Dauer |

Der Dump selbst bleibt im Server; der Agent bekommt nur das Abfrageergebnis, wie heute mit `find_object.py`.

---

## 6 · Freigaben

```json
{
  "permissions": {
    "allow": ["mcp__squish-tests__get_run_result", "mcp__squish-tests__get_testcase"],
    "ask":   ["mcp__squish-tests__run_testcase", "mcp__squish-tests__spy_screen"],
    "deny":  ["Bash(*run_testcase.sh*)", "Bash(*spy_dump.sh*)"]
  }
}
```

---

## 7 · Warum `deny`

Sonst bleibt der alte Weg offen: Mit pauschaler Bash-Freigabe ruft der Agent das Skript direkt, ohne Rückfrage und ohne Zähler.

---

## Diskussionsanschluss

Wer entwickelt die Skripte weiter, und wie geht das mit `deny` für Bash?
