# Denkmodell · Zustand, Lebensdauer und Fehler als Teil des Objekts entwerfen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Paare wie `start`/`stop`, `open`/`close`, `connect`/`disconnect` im Aufrufer | `app.start()` … `app.stop()` |
| Cleanup-Code nach dem letzten Prüfschritt | läuft nur, wenn nichts fehlschlägt |
| Methoden, die in jedem Zustand „etwas" tun | `send()` vor `start()` sendet an `None` |
| Zweiphasige Initialisierung | `obj = X()` gefolgt von `obj.configure(...)` |
| Attribute, die mit `None` beginnen und später gesetzt werden | `self.database = None` |
| `except Exception: return False` | eine Antwort für verschiedene Ursachen |
| `except Exception: pass` oder nur `print` im Cleanup | der Cleanup-Fehler verschwindet |

### Im Testbetrieb

| Signal | Konkret |
|---|---|
| Kaskaden von Folgefehlern | ein echter Fehler, danach scheitern alle weiteren Tests |
| Tests bestehen einzeln, scheitern im Lauf | Reihenfolgeabhängigkeit durch verschmutzten Zustand |
| Die gemeldete Exception passt nicht zum Symptom | `ProcessLookupError` statt Absturz |
| Manuelle Aufräumschritte vor dem Lauf | Skript beendet übriggebliebene Prozesse |
| Dieselbe Meldung für verschiedene Ursachen | „Simulator nicht erreichbar" |

---

## Stufe 2 · Erkenntnisse

**1. Was ein Objekt öffnet, sollte es auch verlässlich schließen können.**
Liegt das Schließen beim Aufrufer, muss jeder Aufrufer den Fehlerpfad richtig behandeln. Einer, der es vergisst, genügt.

**2. Zustand bestimmt, was zulässig ist.**
Eine Operation, die in einem Zustand keinen Sinn hat, sollte dort laut scheitern. Ein stilles Weiterlaufen verschiebt den Fehler an eine Stelle, an der niemand ihn sucht.

**3. Ein Objekt sollte nach dem Konstruktor verwendbar sein.**
Jede zusätzliche Phase zwischen Erzeugen und Benutzen ist ein Zustand, in dem etwas vergessen werden kann.

**4. Exceptions sind Teil der Schnittstelle.**
Welche Fehler ein Objekt meldet, entscheidet darüber, was der Aufrufer tun kann. Wer alle Fehler zu `False` zusammenfasst, nimmt ihm die Wahl.

**5. Beim Aufräumen können zwei Fehler zusammentreffen.**
Dann stellt sich die Frage, welcher gemeldet wird. Python beantwortet sie standardmäßig mit „der letzte", und das ist für die Diagnose oft der falsche.

**Was gesucht wird:** für jede Ressource der Besitzer, der Weg zurück und die Frage, welcher Fehler den Aufrufer erreichen soll.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **`try/finally` beim Aufrufer** | es wenige Aufrufer gibt und der Lifecycle nicht wiederverwendet wird |
| **Context Manager als Klasse** (`__enter__`/`__exit__`) | das Objekt selbst eine begrenzte Lebensdauer hat |
| **Context Manager als Funktion** (`@contextmanager`) | eine vorhandene Klasse mit `open`/`close` unverändert bleiben soll |
| **`contextlib.ExitStack`** | die Zahl der Ressourcen erst zur Laufzeit feststeht |
| **Zustandsprüfung in der Methode** | ein Objekt mehrere Zustände hat und das nicht vermeidbar ist |
| **Getrennte Objekte je Zustand** | Operationen eines Zustands im anderen gar nicht existieren sollen |
| **Vollständige Initialisierung im Konstruktor** | alle Pflichtangaben beim Erzeugen bekannt sind |
| **Kleine eigene Exception-Hierarchie** | Aufrufer auf verschiedene Fehlerarten verschieden reagieren |
| **Übersetzen mit `raise … from …`** | technische Fehler an einer Schichtgrenze verständlich werden sollen |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es einen begrenzten Lebenszyklus?

- **Ja**, etwas wird geöffnet, gestartet oder gesperrt und muss wieder beendet werden → Context Manager prüfen.
- **Nein**, das Objekt hält nur Daten oder sammelt Ergebnisse → kein Context Manager. Er hätte keinen Austritt, den er garantieren müsste.

Der Prüfstein: Was bleibt übrig, wenn das Ende nicht erreicht wird?

### Frage 2 — Wer beendet den Zustand?

- **Der Aufrufer, jedes Mal von Hand** → fehleranfällig bei vielen Aufrufern.
- **Das Objekt über `__exit__`** → der Aufrufer kann das Ende nicht vergessen.
- **Ein übergeordnetes Objekt**, das mehrere Ressourcen besitzt → es schließt sie in umgekehrter Reihenfolge des Öffnens.

### Frage 3 — Welche Operationen sind in welchem Zustand zulässig?

Vier Richtungen, die sich kombinieren lassen:

1. Die Methode prüft den Zustand und wirft eine eindeutige Exception.
2. Der Konstruktor liefert nur verwendbare Objekte.
3. Jeder Zustand ist ein eigenes Objekt mit eigenen Methoden.
4. Ein Context Manager kapselt Aufbau und Abbau.

Je mehr Zustände es gibt, desto eher lohnt Richtung 3. Bei zwei Zuständen genügt oft Richtung 1 zusammen mit 4.

### Frage 4 — Wer kann auf den Fehler sinnvoll reagieren?

- **Der direkte Aufrufer** → eine eigene Exception, die er fangen kann.
- **Erst eine höhere Ebene** → weiterreichen, gegebenenfalls übersetzen.
- **Niemand, es ist ein Programmierfehler** → nicht fangen.

Übersetzt wird mit `raise NeueException(...) from error`, damit die Ursache erhalten bleibt.

### Frage 5 — Was geschieht, wenn das Aufräumen selbst scheitert?

- **Es lief kein anderer Fehler** → den Cleanup-Fehler normal werfen.
- **Es lief bereits ein Fehler** → den ursprünglichen Fehler weiterreichen und den Cleanup-Fehler anhängen, etwa mit `add_note()` (ab Python 3.11) oder über das Logging.

In beiden Fällen gilt: Der Cleanup-Fehler darf nicht verschwinden, denn er bedeutet, dass die Umgebung möglicherweise nicht sauber ist.

---

## Der Denkweg auf einen Blick

```
Ein Objekt öffnet, startet oder sperrt etwas
        ↓
Gibt es ein Ende, das garantiert werden muss?   nein → kein Context Manager
        ↓ ja
Wer beendet es heute?                  jeder Aufrufer → Context Manager
        ↓
Gibt es Operationen, die nur in einem Zustand gelten?
        ↓ ja                            nein → fertig
Zustand prüfen · Konstruktor vervollständigen · getrennte Objekte
        ↓
Welche Fehler können auftreten, wer reagiert darauf?
        ↓
Übersetzen an der Grenze, Ursache mit "from" erhalten
        ↓
Kann das Aufräumen selbst scheitern?    ja → Originalfehler behalten,
        ↓ nein                                Cleanup-Fehler anhängen
                 LIFECYCLE IST TEIL DES OBJEKTS
```

---

## Die eine Prüffrage

> **Wer beendet diesen Zustand – und was passiert, wenn zwischen Start und Ende ein Fehler auftritt?**

Und die Gegenfrage für jede gefangene Exception:

> **Welche Information hat der Aufrufer danach noch?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Steht `stop()` oder `close()` nach dem letzten Prüfschritt ohne `finally`? | läuft nur im Erfolgsfall |
| Kann ein Objekt nach dem Konstruktor noch nicht benutzt werden? | ein Zustand mehr, in dem etwas vergessen wird |
| Liefert eine Methode im falschen Zustand ein Ergebnis? | der Fehler zeigt sich später und woanders |
| Endet ein `except` mit `return False` oder `pass`? | die Ursache ist verloren |
| Kann im `finally` oder in `__exit__` eine Exception entstehen? | sie ersetzt die ursprüngliche |
| Gibt `__exit__` etwas anderes als `False` oder `None` zurück? | Exceptions werden unterdrückt |
| Hat ein Context Manager nichts, was er schließen müsste? | zusätzliche Struktur ohne Aussage |

---

## Wenn die Entscheidung steht

**`__exit__` gibt `False` zurück, außer die Unterdrückung ist gewollt.**
Ein versehentliches `return True` lässt fehlgeschlagene Tests bestehen. Wer nichts zurückgibt, gibt `None` zurück, und das unterdrückt ebenfalls nichts.

**`__enter__` räumt selbst auf, wenn es scheitert.**
`__exit__` wird dann nicht aufgerufen. Was `__enter__` bis zum Fehler geöffnet hat, muss es vor dem Weiterwerfen wieder schließen.

**Beim `@contextmanager` gehört `yield` in ein `try/finally`.**
Sonst läuft der Code nach `yield` bei einer Exception im Block nicht.

**Mehrere Ressourcen werden in umgekehrter Reihenfolge geschlossen.**
`with database, app:` schließt erst `app`, dann `database`. Das entspricht der Abhängigkeit: Die Anwendung braucht die Datenbank, nicht umgekehrt.

**Eigene Exceptions sparsam.**
Eine Basisklasse und so viele Unterklassen, wie Aufrufer tatsächlich unterscheiden. Eine Hierarchie für jede denkbare Ursache erzeugt Klassen, die niemand fängt.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Context Manager mit `try/finally` | der Context Manager legt den Austritt einmal im Objekt fest, `try/finally` in jedem Aufrufer |
| Context Manager mit „jede Klasse mit Ressource" | er drückt eine begrenzte Lebensdauer aus; ein Ergebnisobjekt hat keine |
| `__del__` mit Cleanup | wann `__del__` läuft, ist nicht garantiert |
| Fehler übersetzen mit Fehler verbergen | `raise … from error` behält die Ursache, `return False` verwirft sie |
| robust mit still | eine Funktion, die nie wirft, meldet auch nie, was schiefging |
| Invariante mit Validierung | die Invariante gilt für die ganze Lebensdauer, die Validierung prüft einen Zeitpunkt |
