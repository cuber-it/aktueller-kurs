# OOP-158 · Mengenprüfung ohne Prüfstand testbar machen

**Typ:** Story
**Komponente:** Testframework Workflows
**Priorität:** Hoch

---

## Story

**Als** Entwicklerin im Testautomatisierungsteam
**möchte ich** die Logik eines Workflows prüfen können, ohne Terminal, Testbackend und Netzwerkfreigabe bereitzustellen,
**damit** ein Fehler in einer Rechenregel nach Minuten auffällt und nicht nach dem nächsten Nachtlauf.

---

## Description

Die GUI-Testsuite für das Terminal umfasst **860 Tests**. Der Nachtlauf dauert 5 Stunden 20 Minuten auf zwei Prüfständen, auf denen Terminal und Testbackend installiert sind.

`ApplicationWorkflow` wird von **74 Tests** für Aufträge verwendet. Der Workflow beschafft seine Kollaborateure selbst:

| Kollaborateur | Wie beschafft |
|---|---|
| Terminal | `TerminalClient.connect(CONFIG["terminal_host"])` in `execute` |
| Aufwandmengen | `TaskService.instance()`, Singleton mit URL aus `CONFIG` |
| Reporter | `HtmlReporter(CONFIG["report_dir"])` in `execute` |
| Datum | `date.today()` |

**Befund:** Regeländerungen in `_expected_volume` sind lokal nicht prüfbar, nur im Nachtlauf auf dem Prüfstand. Die Mindestmenge von 5 l für kleine Aufträge war eine Änderung von drei Zeilen, prüfbar erst am nächsten Morgen.

**Die nächste Änderung ist angekündigt:** Ab 10 ha Auftragsfläche gilt ein Randabzug von 2 %. Sie soll vor dem Commit prüfbar sein.

**Befund zur Entstehung:** Der Workflow wurde als Ablauf auf dem Prüfstand geschrieben. Dass jemand Teile davon ohne Prüfstand ausführen möchte, war nicht vorgesehen.

**Nicht Gegenstand:** Die übrigen Workflows und die Struktur des Moduls `environment`.

## Randbedingungen

- Entwicklerrechner haben kein Terminal, keinen Zugang zum Testbackend und keine Verbindung zur Report-Freigabe.
- Ein Versuch mit `unittest.mock.patch` existiert: 43 Zeilen Vorbereitung für einen Test der Mengenregel. Er brach, als `environment` in ein Paket verschoben wurde.
- Eine Registry nach Material C wurde prototypisch gebaut, aber nicht übernommen.
- Neue Abhängigkeiten zu Bibliotheken sind nicht erwünscht.

## Akzeptanzkriterien

- **AK1** – Die Mengenregel ist ohne Terminal, Backend und Netzwerkfreigabe prüfbar. Die Tests dazu laufen in unter einer Sekunde.
- **AK2** – Alle wesentlichen Kollaborateure von `ApplicationWorkflow` sind am Konstruktor oder an der Signatur von `execute` erkennbar.
- **AK3** – `ApplicationWorkflow` greift weder auf `CONFIG` noch auf Singletons oder eine Registry zu.
- **AK4** – Tests für den Workflow kommen ohne `mock.patch` mit Modulpfaden aus.
- **AK5** – Der Workflow für den Prüfstand wird an einer Stelle zusammengesetzt.
- **AK6** – Für jede Abhängigkeit ist entschieden und begründet, ob sie übergeben wird oder konkret bleibt.
- **AK7** – Es wird kein DI-Framework eingeführt.

## Hinweise

Eine Registry erfüllt AK2 nicht. Die Abhängigkeit ist austauschbar, aber weiterhin erst in der Implementierung sichtbar.

`mock.patch` erfüllt AK4 nicht. Es ersetzt eine versteckte Abhängigkeit von außen, ohne sie sichtbar zu machen, und koppelt den Test an Modulpfade.

AK6 wird unbequem: Es ist damit zu rechnen, dass Vorschläge entstehen, auch Rundung, Mindestmenge und Randabzug zu injizieren.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Kann ich am Konstruktor oder an der öffentlichen API erkennen, was dieses Objekt zum Arbeiten braucht?**

---
---

# Addendum · Woran man versteckte Abhängigkeiten erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Konkrete Objekte werden in einer Methode erzeugt | `HtmlReporter(...)` in `execute` |
| Globale Konfiguration wird gelesen | `CONFIG["report_dir"]` |
| Singletons | `TaskService.instance()` |
| Service Locator | `Registry.get("tasks")` |
| Zeit und Zufall direkt aus der Standardbibliothek | `date.today()`, `random.choice(...)` |
| Konstruktor ohne Parameter bei einer Klasse mit vielen Kollaborateuren | `ApplicationWorkflow()` |

## In den Tests

| Signal | Konkret |
|---|---|
| Test braucht Prüfstand, Netzwerk oder Dateisystem für eine Rechenregel | Mengenregel nur im Nachtlauf prüfbar |
| Viele `mock.patch`-Zeilen mit Modulpfaden | 43 Zeilen Vorbereitung für drei Zeilen Logik |
| Tests brechen bei Verschiebung von Modulen | Patch-Ziel ist ein String |
| Mehr Mock-Konfiguration als fachliche Aussage | die Assertion ist die kürzeste Zeile im Test |

## Wie eine Abhängigkeit hereinkommen kann

| Form | Beispiel | Geeignet für |
|---|---|---|
| Konstruktor | `ApplicationWorkflow(form, rates, reporter)` | Kollaborateure, die das Objekt dauerhaft braucht |
| Methode | `execute(field_id, area_ha, product, rate)` | Werte oder Kontext eines einzelnen Aufrufs |
| Default-Parameter | `today=date.today` | Abhängigkeiten mit harmlosem Standard, die nur Tests ersetzen |
| Wert statt Dienst | `expected_volume(area_ha, rate)` | wenn nur ein Ergebnis des Dienstes gebraucht wird |

## Test Doubles

| Art | Was es tut | Beispiel |
|---|---|---|
| Stub | liefert vorbereitete Antworten | `FixedRates(Decimal("20"))` |
| Fake | vereinfachte, funktionierende Implementierung | Tabelle der Aufwandmengen im Speicher |
| Spy | zeichnet Aufrufe auf, die der Test danach prüft | `RecordingReporter` mit Liste der Ergebnisse |
| Mock | kennt erwartete Aufrufe und prüft sie selbst | `unittest.mock.Mock` mit `assert_called_once_with` |

Entscheidend ist nicht die Art, sondern ob die Abhängigkeit **kontrolliert ersetzt werden kann**.

## Wann nicht injiziert wird

- Werte und Funktionen ohne Seiteneffekt, die sich nicht unabhängig ändern: `Decimal`, `max`, Rundungsregeln
- stabile Implementierungsdetails der eigenen Klasse
- Varianten, die niemand benennen kann

Die Prüffrage lautet: **Welche Änderung oder welcher Test rechtfertigt die Übergabe von außen?** Wenn niemand eine nennen kann, ist die zusätzliche Abstraktion Architekturtheater.
