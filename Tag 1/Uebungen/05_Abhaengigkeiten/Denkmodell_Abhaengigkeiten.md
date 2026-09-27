# Denkmodell · Abhängigkeiten sichtbar und kontrollierbar machen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Konkrete Kollaborateure werden in Methoden erzeugt | `reporter = HtmlReporter(...)` in `execute` |
| Globale Konfiguration wird tief im Code gelesen | `CONFIG["report_dir"]` |
| Singletons | `TaskService.instance()` |
| Service Locator | `Registry.get("tasks")` |
| Zeit, Zufall oder Umgebung direkt abgefragt | `date.today()`, `os.environ[...]` |
| Konstruktor ohne Parameter bei vielen Kollaborateuren | `ApplicationWorkflow()` |
| Eine Regel ist private Methode eines Ablaufs mit Seiteneffekten | `_expected_volume` in einem Workflow, der das Terminal verbindet |

### In Tests und im Alltag

| Signal | Konkret |
|---|---|
| Eine Rechenregel ist nur in der Gesamtumgebung prüfbar | Mengenregel nur im Nachtlauf |
| Viel `mock.patch` mit Modulpfaden | Tests brechen beim Verschieben eines Moduls |
| Tests beeinflussen sich gegenseitig | ein Singleton wurde überschrieben und nicht zurückgesetzt |
| Mehr Vorbereitung als Aussage | 43 Zeilen Setup, eine Assertion |
| „Auf meinem Rechner geht das nicht" | Abhängigkeit von Prüfstand, Freigabe, Netzwerk |

---

## Stufe 2 · Erkenntnisse

**1. Eine Abhängigkeit verschwindet nicht, wenn man sie versteckt.**
Ein Workflow, der seinen Reporter selbst erzeugt, hängt genauso vom Reporter ab wie einer, der ihn übergeben bekommt. Der Unterschied ist, dass man es nicht sieht und nicht steuern kann.

**2. Sichtbarkeit ist das Ziel, Testbarkeit die Folge.**
Wer die Kollaborateure am Konstruktor aufführt, macht die Zusammenarbeit lesbar. Dass Tests dadurch Ersatzobjekte übergeben können, folgt daraus. Umgekehrt führt „wir injizieren, damit man mocken kann" leicht zu Abstraktionen ohne fachlichen Grund.

**3. Nicht jede Abhängigkeit ist wesentlich.**
`Decimal`, `max` oder eine feste Rundungsregel sind Abhängigkeiten, aber keine Kollaborateure. Sie ändern sich nicht unabhängig und haben keine Seiteneffekte.

**4. In Python genügt ein Parameter.**
Dependency Injection heißt: Das Objekt bekommt seine Kollaborateure von außen. Dafür ist kein Framework nötig.

**Was gesucht wird:** die Kollaborateure, die ein Objekt wirklich braucht, und die Stelle, an der sie ausgewählt werden.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Constructor Injection** | das Objekt den Kollaborateur über seine ganze Lebensdauer braucht |
| **Method Injection** | der Kollaborateur oder Wert nur für einen Aufruf gilt |
| **Wert statt Dienst übergeben** | nur ein Ergebnis gebraucht wird, etwa ein Kurs statt des Kursdienstes |
| **Default-Parameter** | der Standard harmlos ist (keine Ein-/Ausgabe, kein Netz) und nur Tests ihn ersetzen |
| **Konkret lassen** | es keine Variante und keinen Testbedarf gibt |
| **Regel herauslösen** | eine fachliche Regel in einem Ablauf mit Seiteneffekten steckt |
| **Kleiner Vertrag (Protocol)** | ein höherliegender Ablauf nur wenige Operationen eines technischen Details braucht |

Nicht in der Liste: Singleton, Service Locator, `mock.patch` als Dauerlösung. Sie machen austauschbar, aber nicht sichtbar.

---

## Stufe 4 · Entscheidung

### Frage 1 — Steckt eine Regel in einem Ablauf mit Seiteneffekten?

- **Ja** → Regel als Funktion oder eigene Klasse herauslösen, mit Werten als Eingabe. Sie braucht dann oft gar keine Injektion mehr.
- **Nein** → weiter.

### Frage 2 — Ist die Abhängigkeit ein Kollaborateur mit eigenem Verhalten?

- **Nein**, ein Wert oder eine reine Funktion ohne Seiteneffekt → konkret lassen oder als Wert übergeben.
- **Ja**, mit Ein-/Ausgabe, Zustand oder Seiteneffekten → weiter.

### Frage 3 — Braucht das Objekt den Dienst oder nur ein Ergebnis davon?

- **Nur ein Ergebnis** → Wert übergeben.
- **Den Dienst** → weiter.

### Frage 4 — Dauerhaft oder für einen Aufruf?

- **Dauerhaft** → Konstruktor.
- **Für einen Aufruf** → Methode.

### Frage 5 — Gibt es einen harmlosen Standard?

- **Ja**, und er hat keine Ein-/Ausgabe → Default-Parameter ist vertretbar, etwa `now=datetime.now`.
- **Nein**, der Standard öffnet Dateien, Netz oder GUI → kein Default. Sonst ist die Abhängigkeit wieder im Objekt verankert.

Der Prüfstein für jede Übergabe: **Welche Änderung oder welcher Test rechtfertigt sie?**

---

## Der Denkweg auf einen Blick

```
Ein Objekt ist nur in der Gesamtumgebung prüfbar
        ↓
Steckt eine Regel in einem Ablauf?        ja → Regel herauslösen, Werte übergeben
        ↓ nein
Kollaborateur mit Verhalten/Seiteneffekt? nein → konkret lassen
        ↓ ja
Nur ein Ergebnis gebraucht?               ja → Wert übergeben
        ↓ nein
Dauerhaft gebraucht?                      ja → Konstruktor
        ↓ nein
     Methode
        ↓
Harmloser Standard vorhanden?             ja → Default-Parameter vertretbar
        ↓ nein
                 ZUSAMMENSETZEN AN EINER STELLE
```

---

## Die eine Prüffrage

> **Kann ich am Konstruktor oder an der öffentlichen API erkennen, was dieses Objekt zum Arbeiten braucht?**

Und die Gegenfrage für jeden neuen Parameter:

> **Welche Änderung oder welcher Test rechtfertigt ihn?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wird in einer Methode ein technischer Kollaborateur erzeugt? | versteckte Abhängigkeit |
| Holt das Objekt etwas aus einer Registry? | austauschbar, aber nicht sichtbar |
| Braucht ein Test `mock.patch` mit Modulpfad? | die Abhängigkeit ist versteckt, der Test koppelt an die Modulstruktur |
| Heißt der Default `reporter or HtmlReporter(...)`? | jedes falsy Objekt wird ersetzt, auch ein leerer Test-Reporter mit `__len__`; `is None` prüfen |
| Ist der Default ein veränderliches Objekt wie `events=[]`? | es wird einmal erzeugt und von allen Aufrufen geteilt |
| Hat ein Parameter nur eine denkbare Implementierung? | vermutlich Architekturtheater |
| Enthält der Test mehr Double-Konfiguration als Aussage? | der Schnitt der Abhängigkeiten ist zu grob |

---

## Wenn die Entscheidung steht

**Zusammensetzen an einer Stelle.**
Die konkreten Objekte für den Prüfstand werden in einer Funktion oder einem Modul erzeugt und übergeben. Dort, und nur dort, darf `CONFIG` gelesen werden.

**Der Vertrag gehört dem Verwender.**
Der Workflow beschreibt, was er vom Terminal-Client braucht. Der Terminal-Client erfüllt es. So hängt der Workflow nicht von allen Fähigkeiten des Terminal-Clients ab, und ein Test-Double muss nur drei Methoden haben.

**Default-Parameter mit `is None` prüfen.**
`reporter or Default()` ersetzt jedes Objekt, das als falsch gilt. Ein Test-Reporter mit `__len__`, der noch nichts aufgezeichnet hat, wird dadurch still ausgetauscht.

**Test Doubles einfach halten.**
Ein Stub oder Spy als kleine Klasse ist oft lesbarer als ein konfiguriertes `Mock`. `unittest.mock` bleibt nützlich, wo ein Protokoll groß ist oder Aufrufe genau geprüft werden sollen.

**Nicht alles injizieren.**
Jeder Parameter ist ein Teil der öffentlichen API. Wer Rundung und Mindestmenge injiziert, verteilt eine fachliche Regel auf den Aufrufer.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Dependency Injection mit DI-Container | DI ist das Übergeben; ein Container ist ein Werkzeug dafür, in Python selten nötig |
| Dependency Injection mit Dependency Inversion | Injection regelt, wer auswählt; Inversion regelt, wer den Vertrag bestimmt |
| Service Locator mit Injection | beim Locator holt sich das Objekt seine Kollaborateure selbst |
| Test Double mit Mock | Mock ist eine Art Test Double, Stub, Fake und Spy sind andere |
| `mock.patch` mit Testbarkeit | Patch ersetzt eine versteckte Abhängigkeit, ohne sie sichtbar zu machen |
| explizit mit viel | explizit heißt sichtbar, nicht möglichst viele Parameter |
