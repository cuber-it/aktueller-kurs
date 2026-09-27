# Denkmodell · Eine Schnittstelle festlegen, die andere benutzen können

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Fremder Code verwendet Namen mit Unterstrich | `collector._failed()` |
| Methoden geben interne Strukturen heraus | `get_results()` liefert das Dictionary, in dem gesammelt wird |
| Abgekürzte oder technische Namen | `add(n, s, d)`, `calc`, `proc`, `do_export` |
| Docstrings, die den Namen wiederholen | `"""Adds a result."""` |
| Daten als Dictionaries mit vereinbarten Schlüsseln | `result["status"]` |
| Module, deren Name eine Art statt einer Aufgabe nennt | `utils.py`, `helpers.py`, `common.py` |
| Ein Parameter wählt zwischen verschiedenen Verhalten | `export(fmt="html")` |

### Im Team

| Signal | Konkret |
|---|---|
| „Das war doch privat" | eine Änderung an `_name` bricht andere |
| Die API ist in einem Wiki beschrieben | und stimmt nicht mehr mit dem Code überein |
| Reviews drehen sich um Leerzeilen und Importe | Designfragen bleiben liegen |
| Nutzer wissen nicht, was eine Methode zusichert | sie probieren es aus oder lesen den Code |

---

## Stufe 2 · Erkenntnisse

**1. Die öffentliche Schnittstelle ist eine Entscheidung.**
Python verhindert keinen Zugriff. Was öffentlich ist, ergibt sich aus dem, was die Autoren zusichern, und daraus, dass Nutzer es erkennen können.

**2. Der Name gehört zum Vertrag.**
Ein Aufrufer liest `collector.record(result)` und weiß, was geschieht. `collector.add(n, s, d)` verlangt, den Code zu lesen.

**3. Ein Zugriff auf `_name` ist eine Information.**
Er zeigt ein Bedürfnis, das die öffentliche Schnittstelle nicht bedient. Das Bedürfnis kann berechtigt sein oder nicht. Es zu kennen ist die Voraussetzung, um darüber zu entscheiden.

**4. Stilfragen und Designfragen liegen auf verschiedenen Ebenen.**
Formatierung, Importe und Namenskonventionen kann ein Werkzeug entscheiden. Ob eine Methode öffentlich sein soll oder ein Modul die richtige Aufgabe hat, kann es nicht.

**Was gesucht wird:** eine Schnittstelle, die den richtigen Gebrauch einfach macht und alles andere als austauschbar kennzeichnet.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Name ohne Unterstrich** | fremder Code sich darauf verlassen soll |
| **`_name`** | es ein Implementierungsdetail ist, das sich ändern darf |
| **`__all__`** | ein Modul ausdrücklich festhalten soll, was es anbietet |
| **Type Hints** | Aufrufer und Werkzeuge wissen sollen, was hineingeht und herauskommt |
| **Docstring mit Vertrag** | der Name nicht alles sagt: Seiteneffekte, Exceptions, Randbedingungen |
| **`@dataclass(frozen=True)`** | ein Wert ohne Verhalten und ohne Lebenszyklus vorliegt, der sich nicht ändern soll |
| **`@dataclass`** | ein veränderlicher Datenträger mit wenig Verhalten gebraucht wird |
| **gewöhnliche Klasse** | Verhalten, Zustand und Regeln zusammengehören |
| **Property** | ein bisher öffentliches Attribut eine Regel bekommt, ohne dass Aufrufer sich ändern sollen |
| **Modul nach Verantwortung** | eine Gruppe von Funktionen eine gemeinsame Aufgabe hat |
| **Regel im Werkzeug** | eine Frage mechanisch entscheidbar ist |
| **Regel im Review** | eine Frage Designurteil braucht |

---

## Stufe 4 · Entscheidung

### Frage 1 — Soll sich fremder Code darauf verlassen dürfen?

- **Ja** → Name ohne Unterstrich, Type Hints, Docstring mit Vertrag, Eintrag in `__all__`.
- **Nein** → `_name`.
- **Unklar, weil es bereits jemand verwendet** → das Bedürfnis dahinter klären. Entweder eine öffentliche Funktion dafür anbieten oder begründen, warum es nicht bedient wird.

### Frage 2 — Sagt der Name, was passiert?

- **Ja** → bleibt.
- **Nein, er beschreibt die Technik** (`write_json`, `get_data`) → nach dem Ergebnis benennen, das der Aufrufer bekommt.
- **Nein, er ist abgekürzt** (`n`, `s`, `calc`) → ausschreiben.

Der Prüfstein: Versteht ein Aufrufer die Zeile, ohne die Implementierung zu öffnen?

### Frage 3 — Datenträger oder Verhaltensobjekt?

- **Nur Daten, keine eigenen Regeln** → `@dataclass`, bei Werten, die sich nicht ändern sollen, `frozen=True`.
- **Daten mit einer einfachen Prüfung** → Dataclass mit Prüfung in `__post_init__`.
- **Zustand, Verhalten, Lebenszyklus** → gewöhnliche Klasse. Eine Dataclass würde Konstruktor, Gleichheit und Darstellung aus allen Feldern erzeugen, auch aus internen.

### Frage 4 — Kann ein Werkzeug die Regel prüfen?

- **Ja** → in Formatter, Linter oder Type Checker und in der CI. Nicht im Review.
- **Nein** → ins Review, mit einer Frage, die der Reviewer stellen kann.

### Frage 5 — Wie verbindlich soll die Regel sein?

- **Ohne Ausnahme sinnvoll und prüfbar** → MUST.
- **Standard mit legitimen Ausnahmen** → SHOULD.
- **Erlaubt, aber nicht verlangt** → MAY.
- **Bewusst zu vermeiden** → DON'T.

---

## Der Denkweg auf einen Blick

```
Ein Name, eine Klasse oder ein Modul wird von anderen verwendet
        ↓
Sollen andere sich darauf verlassen?        nein → _name
        ↓ ja                                 (wird es trotzdem verwendet?
        ↓                                     → Bedürfnis klären)
Sagt der Name, was passiert?                 nein → umbenennen
        ↓ ja
Type Hints und Docstring mit Vertrag
        ↓
Reiner Datenträger?                          ja → dataclass, ggf. frozen
        ↓ nein
Gewöhnliche Klasse
        ↓
Liegt es im Modul seiner Verantwortung?      nein → verschieben
        ↓ ja
In __all__ aufnehmen
        ↓
Welche Regel steckt dahinter, und wer prüft sie?
```

---

## Die eine Prüffrage

> **Worauf darf sich fremder Code verlassen – und woran erkennt er das?**

Und die Gegenfrage für jede Teamregel:

> **Wer prüft sie – ein Werkzeug oder ein Mensch?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Greift fremder Code auf `_name` zu? | es fehlt ein öffentliches Angebot, oder das Bedürfnis ist nicht gewollt |
| Gibt eine Methode eine interne Sammlung heraus? | Aufrufer können den Zustand verändern |
| Lässt sich der Docstring aus dem Namen ableiten? | er trägt nichts bei |
| Wählt ein String-Parameter das Verhalten? | zwei Methoden mit sprechenden Namen prüfen |
| Heißt ein Modul `utils` oder `common`? | seine Verantwortung ist nicht benannt |
| Diskutiert das Review eine Leerzeile? | die Regel gehört in ein Werkzeug |
| Gibt es eine MUST-Regel, die niemand prüft? | sie wird in der Praxis zu MAY |

---

## Wenn die Entscheidung steht

**Die Schnittstelle im Code festhalten, nicht daneben.**
`__all__`, Namen ohne Unterstrich, Type Hints und Docstrings stehen dort, wo sich der Code ändert. Eine Wiki-Seite veraltet, weil nichts sie mit dem Code verbindet.

**Interne Sammlungen nicht herausgeben.**
Eine Methode, die das interne Dictionary zurückgibt, macht jeden Aufrufer zum Mitbesitzer. Eine Kopie oder ein unveränderlicher Typ hält den Zustand beim Objekt.

**Eine Property, wenn ein öffentliches Attribut eine Regel bekommt.**
Wird `collector.results` heute gelesen, kann daraus eine Property werden, die eine unveränderliche Sicht liefert. Lesende Aufrufer merken nichts, schreibende scheitern sichtbar.

**Veraltete Namen nicht sofort entfernen.**
Wenn andere Teams eine Methode verwenden, kann sie für eine Übergangszeit auf die neue verweisen und eine `DeprecationWarning` auslösen.

**Werkzeugregeln zuerst.**
Formatter und Linter in der CI entlasten jedes Review ab dem ersten Tag. Designregeln brauchen Diskussion und kommen danach.

**Nicht jede Methode braucht einen Docstring.**
`failed` als Property über die fehlgeschlagenen Ergebnisse erklärt sich selbst. Ein Docstring, der das wiederholt, wird beim nächsten Umbau nicht angepasst und stimmt dann nicht mehr.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Style Guide mit Architekturstandard | der Style Guide regelt Form, der Standard regelt Struktur und Verantwortung |
| `__all__` mit Zugriffsschutz | `__all__` steuert `import *` und dokumentiert; direkte Importe bleiben möglich |
| `_name` mit „wird nicht verwendet" | der Unterstrich sagt, was intern sein soll, nicht, wer es verwendet |
| Docstring mit Kommentar | der Docstring beschreibt den Vertrag nach außen, der Kommentar erklärt eine Stelle im Code |
| `dataclass` mit „Klasse mit Attributen" | eine Dataclass erzeugt Gleichheit und Darstellung aus allen Feldern |
| Type Hints mit Laufzeitprüfung | Python prüft Annotationen zur Laufzeit nicht |
