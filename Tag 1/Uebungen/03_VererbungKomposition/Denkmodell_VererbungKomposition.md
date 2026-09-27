# Denkmodell · Vererbung, Komposition oder Delegation wählen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Unterklassen nutzen nur wenige Methoden der Basisklasse | 7 von 46 |
| Geerbte Methoden werden stillgelegt | `raise NotImplementedError` in einer Unterklasse |
| Aufrufer prüfen auf konkrete Unterklassen | `if not isinstance(test, ServiceMenuTest)` |
| Mixins verwenden Attribute, die sie nicht selbst setzen | `self.driver`, `self.test_id` |
| Mehrere Basisklassen definieren dieselbe Methode | `log()` in Mixin und Basisklasse |
| Basisklassen heißen nach ihrer Position, nicht nach einem Begriff | `BaseTest`, `AbstractCommon` |
| Tiefe Hierarchien für Kombinationen von Fähigkeiten | `ServiceTest(DeviceTest(BaseTest))` |

### Im Team und in der Testsuite

| Signal | Konkret |
|---|---|
| Wiederverwendung als einziges Argument für eine Basisklasse | „dann haben es alle" |
| Änderungen an der Basisklasse treffen Tests an unerwarteter Stelle | Default-Timeout gesenkt, fremde Tests fallen um |
| Tests belegen Ressourcen, die sie nicht brauchen | Geräteverbindung für reine Dateiprüfungen |
| Diskussionen, auf welche Ebene einer Hierarchie eine Fähigkeit gehört | Screenshots in `DeviceTest` oder `BaseTest`? |

---

## Stufe 2 · Erkenntnisse

**1. Vererbung und Komposition drücken verschiedene Beziehungen aus.**
Vererbung sagt „ist ein", Komposition sagt „arbeitet zusammen mit". Beide ermöglichen Wiederverwendung. Welche passt, entscheidet die Beziehung, nicht die Menge des geteilten Codes.

**2. Eine Unterklasse übernimmt den Vertrag der Basisklasse vollständig.**
Wer eine Unterklasse erwartet, darf sich auf alles verlassen, was die Basisklasse zusagt. Eine Unterklasse, die eine geerbte Methode verweigert, bricht diesen Vertrag, und der Aufrufer muss Sonderfälle kennen.

**3. Fähigkeiten lassen sich nicht sinnvoll in einer Hierarchie ordnen.**
Screenshots, Logging, Geräteverbindung und Testdaten sind unabhängig voneinander. Eine Hierarchie zwingt sie in eine Reihenfolge, die es fachlich nicht gibt.

**4. Mixins sind Vererbung.**
Sie bringen dieselbe Kopplung mit: Sie greifen auf `self` zu und hängen von Attributen und Methoden ab, die andere Klassen bereitstellen. Welche Methode bei Namensgleichheit gilt, bestimmt die Reihenfolge der Basisklassen.

**Was gesucht wird:** für jede Beziehung die Aussage, die sie macht, und ob diese Aussage für jede beteiligte Klasse zutrifft.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Vererbung** | eine stabile Typbeziehung besteht und der Vertrag der Basisklasse für jede Unterklasse gilt |
| **Komposition** | ein Objekt Fähigkeiten anderer Objekte nutzt, ohne selbst eines davon zu sein |
| **Delegation** | Verhalten ergänzt werden soll, ohne die ursprüngliche Klasse und ihre Nutzer zu ändern |
| **Mixin** | eine kleine Fähigkeit ohne eigene Voraussetzungen an `self` mehreren Klassen einer Familie beigemischt werden soll |
| **Funktion auf Modulebene** | die Fähigkeit keinen Zustand braucht und von keinem Objekt besessen werden muss |

---

## Stufe 4 · Entscheidung

### Frage 1 — Kann die Unterklasse überall stehen, wo die Basisklasse erwartet wird?

- **Ja**, ohne Ausnahme und ohne Sonderbehandlung beim Aufrufer → Vererbung ist möglich. Weiter mit Frage 2.
- **Nein**, sie verweigert oder verändert zugesagtes Verhalten → keine Vererbung. Die Beziehung ist keine Typbeziehung.

Der Prüfstein: Muss irgendein Aufrufer wissen, welche Unterklasse er vor sich hat?

### Frage 2 — Nutzt die Unterklasse die Basisklasse als Typ oder als Werkzeugkiste?

- **Als Typ** → Aufrufer arbeiten mit der Basisklasse, die Unterklasse ersetzt oder ergänzt Verhalten. Vererbung trägt.
- **Als Werkzeugkiste** → die Unterklasse ruft vor allem geerbte Hilfsmethoden über `self` auf. Die Werkzeuge werden besser als Kollaborateure übergeben.

### Frage 3 — Soll Verhalten ergänzt werden, ohne Klasse und Nutzer zu ändern?

- **Ja** → Delegation: ein Objekt mit derselben Schnittstelle, das ergänzt und weiterreicht.
- **Nein** → keine zusätzliche Schicht.

### Frage 4 — Wenn ein Mixin im Spiel ist: Sind seine Voraussetzungen sichtbar?

- **Es braucht nichts von `self`** außer seinen eigenen Methoden → ein Mixin kann tragen.
- **Es braucht Attribute oder Methoden anderer Klassen** → die Voraussetzung ist unsichtbar. Das Mixin sollte ein Kollaborateur werden, der das Benötigte übergeben bekommt.

---

## Der Denkweg auf einen Blick

```
Eine Klasse erbt von einer Basisklasse
        ↓
Kann sie überall anstelle der Basisklasse stehen?   nein → keine Vererbung
        ↓ ja
Nutzen Aufrufer die Basisklasse als Typ?            nein → Werkzeuge als Kollaborateure
        ↓ ja
              VERERBUNG TRÄGT
        ↓
Soll Verhalten ergänzt werden, ohne Klassen zu ändern?
        ↓ ja
              DELEGATION
        ↓
Mixins beteiligt?  Voraussetzungen an self?          ja → Kollaborateur statt Mixin
```

---

## Die eine Prüffrage

> **Ist diese Klasse eine spezielle Form ihrer Basisklasse – oder möchte sie nur deren Werkzeuge benutzen?**

Und die Gegenfrage für jede Komposition:

> **Welche Änderung wird leichter, weil dieser Kollaborateur getrennt ist?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wirft eine Unterklasse `NotImplementedError` für eine geerbte Methode? | die Typbeziehung stimmt nicht |
| Prüft ein Aufrufer mit `isinstance` auf eine konkrete Unterklasse? | der Vertrag der Basisklasse reicht nicht aus |
| Nutzt eine Unterklasse weniger als ein Viertel der Basisklasse? | wahrscheinlich eine Werkzeugkiste |
| Greift ein Mixin auf Attribute zu, die es nicht setzt? | versteckte Voraussetzung |
| Reicht ein Wrapper jeden Aufruf unverändert weiter? | die Delegation ergänzt nichts und kann entfallen |
| Gibt es genau eine Implementierung eines Kollaborateurs und keine erkennbare Änderung? | die Trennung kostet mehr, als sie bringt |

---

## Wenn die Entscheidung steht

**Vererbung für Typfamilien behalten.**
Ergebnisklassen, Zonen einer Heizung, Varianten eines Protokolls: Wo Aufrufer mit dem Basistyp arbeiten, ist Vererbung die klarste Form. Komposition an dieser Stelle erzeugt Delegationscode ohne Gewinn.

**Werkzeuge einzeln übergeben.**
Jede Fähigkeit, die ein Test braucht, wird ein eigenes Objekt. Am Konstruktor steht dann, was der Test benutzt, und eine Änderung an einer Fähigkeit trifft nur Tests, die sie erhalten haben.

**Defaults an den Kollaborateur binden.**
Ein Timeout gehört zu dem Objekt, das wartet. Zwei Gruppen von Tests können zwei Warteobjekte mit verschiedenen Timeouts erhalten.

**Delegation vollständig oder bewusst unvollständig.**
Ein Wrapper, der nur einen Teil der Methoden weiterreicht, bricht bei der ersten nicht weitergereichten Methode mit `AttributeError`. Das kann gewollt sein, sollte aber entschieden werden.

**Schrittweise umstellen.**
Eine neue Testklasse kann Kollaborateure erhalten, während alte Tests weiter von der Basisklasse erben. Die Basisklasse kann dieselben Kollaborateure intern verwenden, damit beide Wege dasselbe Verhalten haben.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Vererbung mit Wiederverwendung | Wiederverwendung entsteht bei beiden, die Beziehung unterscheidet sie |
| „Composition over Inheritance" mit „keine Vererbung" | der Grundsatz betrifft Wiederverwendung, nicht Typfamilien |
| Mixin mit Komposition | ein Mixin wird geerbt und teilt `self`, ein Kollaborateur nicht |
| Delegation mit Weiterreichen | Delegation ergänzt etwas, reines Weiterreichen ist eine überflüssige Schicht |
| `super()` mit „Aufruf der Basisklasse" | `super()` folgt der Method Resolution Order, bei Mehrfachvererbung ist das nicht zwingend die direkte Basisklasse |
| abstrakte Methode in der Basisklasse mit stillgelegter Methode in der Unterklasse | die erste fordert Verhalten, die zweite verweigert es |
