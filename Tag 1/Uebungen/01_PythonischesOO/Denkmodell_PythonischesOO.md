# Denkmodell · Pythonisch entscheiden statt übertragen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Getter und Setter ohne eigene Logik | `getTimeout()` gibt nur `self.__timeout` zurück |
| Doppelte Unterstriche an allen Feldern | `self.__name`, `self.__tags` |
| Klassen, die nur `@staticmethod` enthalten | `StringUtils`, `DateHelper` |
| Klassen ohne Zustand mit genau einer Methode | `TimestampFormatter().format(...)` |
| Methoden mit Namen aus anderen Sprachen | `toString()`, `equals()`, `hashCode()`, `compareTo()` |
| Interfaces mit einer einzigen Methode | `Runnable`, `Callback`, `Handler` |

### Im Team und in der Testsuite

| Signal | Konkret |
|---|---|
| Begründung mit der Herkunft | „Das ist sauberes OO", „so macht man das" |
| Vorsorge für einen Fall, der nie eintrat | „damit wir später Validierung einbauen können" |
| Tests greifen auf umbenannte Namen zu | `obj._Klasse__feld` |
| Unlesbare Objekte in Protokollen | `<… object at 0x7f…>` |
| `==` verhält sich anders als erwartet | Duplikate werden nicht erkannt |

---

## Stufe 2 · Erkenntnisse

**1. Eine Struktur ist nicht deshalb gut, weil sie in einer anderen Sprache gut ist.**
Getter schützen in Java die Aufrufer vor einer späteren Umstellung. Python erreicht dasselbe mit einer Property, die erst eingeführt wird, wenn sie gebraucht wird.

**2. Kapselung ist in Python eine Vereinbarung.**
`_name` sagt: „Darauf baut fremder Code keinen Vertrag." Der doppelte Unterstrich verändert den Namen, um Kollisionen in Klassenhierarchien zu vermeiden. Einen Zugriffsschutz bietet keins von beiden.

**3. Python-Protokolle werden über Magic Methods bedient.**
`print()`, `==`, `in`, `len()`, `with` und Sets rufen bestimmte Methoden auf. Eigene Methoden mit anderen Namen erreichen diese Stellen nicht.

**4. Klassen, Funktionen und gebundene Methoden sind Objekte.**
Wo andere Sprachen ein Interface mit einer Methode verlangen, kann in Python die Funktion selbst übergeben werden.

**Was gesucht wird:** für jede Struktur die Absicht dahinter, und der Weg, wie Python diese Absicht ausdrückt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Öffentliches Attribut** | der Wert ohne Regel gelesen und gesetzt wird |
| **Property** | beim Lesen oder Setzen eine Regel gilt, der Zugriff aber billig und ohne Seiteneffekt bleibt |
| **Methode** | der Zugriff Parameter braucht, Zeit kostet, Seiteneffekte hat oder fehlschlagen kann |
| **Implementierungsdetail mit `_`** | der Wert intern gebraucht wird und kein Vertrag nach außen sein soll |
| **Magic Method** | das Objekt ein Python-Protokoll tatsächlich erfüllen soll (`__repr__`, `__eq__`, `__enter__` …) |
| **Funktion auf Modulebene** | es weder Zustand noch ein Objekt gibt, zu dem die Operation gehört |
| **Klasse** | Zustand und Verhalten zusammengehören |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es Zustand, zu dem das Verhalten gehört?

- **Nein** → eine Funktion auf Modulebene genügt. Eine Klasse nur als Namensraum übernimmt die Aufgabe, die in Python das Modul hat.
- **Ja** → eine Klasse ist angemessen. Weiter mit Frage 2 für jedes Attribut.

### Frage 2 — Gilt für dieses Attribut eine Regel?

- **Nein** → öffentliches Attribut.
- **Ja, und der Zugriff ist billig und ohne Seiteneffekt** → Property.
- **Ja, aber der Zugriff kostet, braucht Parameter oder kann fehlschlagen** → Methode mit sprechendem Namen.

Der Prüfstein: Würde jemand, der `obj.wert` liest, von dem überrascht, was dabei passiert?

### Frage 3 — Soll fremder Code sich auf das Attribut verlassen?

- **Ja** → ohne Unterstrich.
- **Nein** → einfacher Unterstrich.
- **Doppelter Unterstrich** nur, wenn eine Kollision mit Unterklassen konkret zu erwarten ist.

### Frage 4 — Soll das Objekt ein Python-Protokoll erfüllen?

- **Lesbare Darstellung** → `__repr__`, bei Bedarf `__str__`.
- **Gleichheit** → `__eq__`. Wenn das Objekt in Sets oder als Dict-Schlüssel dienen soll, auch `__hash__`, und zwar nur über unveränderliche Merkmale.
- **Kein Protokoll erkennbar** → keine Magic Method. Sie wird nicht eingebaut, weil sie pythonisch aussieht.

---

## Der Denkweg auf einen Blick

```
Eine Klasse wirkt formal, umständlich oder "wie Java"
        ↓
Hat sie Zustand?                      nein → Funktion auf Modulebene
        ↓ ja
Für jedes Attribut: gilt eine Regel?  nein → öffentliches Attribut
        ↓ ja
Ist der Zugriff billig, ohne Seiteneffekt?
        ↓ ja                          nein → Methode mit sprechendem Namen
     Property
        ↓
Soll fremder Code sich darauf verlassen?   nein → _name
        ↓
Erfüllt das Objekt ein Python-Protokoll?   ja → passende Magic Method
        ↓ nein
                 KEINE WEITERE STRUKTUR
```

---

## Die eine Prüffrage

> **Welches Problem löst diese Struktur in Python?**

Und die Gegenfrage für jede übernommene Konvention:

> **Wird sie mit ihrem Nutzen begründet – oder mit ihrer Herkunft?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Enthält ein Getter nur `return self.__x`? | Attribut genügt, Property erst bei Bedarf |
| Enthält eine Klasse nur `@staticmethod`? | Modul übernimmt die Aufgabe |
| Heißt eine Methode `toString`, `equals` oder `hashCode`? | Python ruft sie nicht auf |
| Greift ein Test auf `_Klasse__feld` zu? | die Kapselung ist nur scheinbar, der Test braucht einen offiziellen Weg |
| Löst eine Property Netzwerk- oder Dateizugriff aus? | Methode mit sprechendem Namen |
| Wurde `__eq__` ohne `__hash__` definiert? | Objekte sind nicht mehr hashbar, Sets schlagen fehl |

---

## Wenn die Entscheidung steht

**Aufrufstellen einmal umstellen, dann nie wieder.**
Der Wechsel von `getTimeout()` zu `timeout` betrifft alle Aufrufer. Jede spätere Regel kommt als Property dazu, ohne dass ein Aufrufer sich ändert.

**Validierung auch im Konstruktor.**
Wird im `__init__` über die Property zugewiesen (`self.timeout = timeout`), greift die Regel auch beim Erzeugen. Wer direkt `self._timeout` setzt, umgeht sie.

**`__repr__` zuerst.**
Für Testcode ist die Diagnosedarstellung meist wichtiger als die Anzeige. Ohne `__str__` verwendet `print()` die Ausgabe von `__repr__`.

**Gleichheit und Hash gemeinsam entscheiden.**
Wer `__eq__` definiert, setzt `__hash__` implizit auf `None`. Soll das Objekt in Sets bleiben, braucht es `__hash__` über dieselben Merkmale, und diese sollten sich nicht ändern.

**Nicht alles umbauen, was ungewohnt aussieht.**
Eine Klasse mit einer Methode kann berechtigt sein, wenn sie Konfiguration hält oder als austauschbarer Kollaborateur gedacht ist. Die Frage ist, ob sie Zustand oder eine Rolle hat.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| `__name` mit `private` | Name Mangling verhindert Kollisionen, keinen Zugriff |
| Property mit Getter | die Property ändert die Aufrufsyntax nicht, der Getter legt sie fest |
| `__str__` mit `__repr__` | `__repr__` dient der Diagnose, `__str__` der Anzeige |
| `__eq__` mit `is` | `==` vergleicht Wert, `is` vergleicht Identität |
| `@staticmethod` mit Modulfunktion | die statische Methode gehört zur Klasse, obwohl sie keine Instanz braucht |
| pythonisch mit kurz | eine verschachtelte Comprehension kann schlechter lesbar sein als eine Schleife |
