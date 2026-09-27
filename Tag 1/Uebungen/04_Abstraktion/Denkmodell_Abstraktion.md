# Denkmodell · Die passende Form von Abstraktion wählen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Methodenrümpfe mit `pass` oder `raise NotImplementedError` | eine Konsole, die `send_attachment` nicht kann |
| Ein Client ruft einen kleinen Teil des Vertrags auf | eine von fünf Methoden |
| Test-Doubles implementieren mehr, als der Test braucht | neun Methoden für zwei Aufrufe |
| Adapter, die nur Leermethoden ergänzen | fremde Klasse passt, erbt aber nicht |
| Abstraktion mit genau einer Implementierung | `ReportRenderer` mit `HtmlReportRenderer` |
| Eine Erweiterung bricht Klassen, die sie nicht nutzen | neue abstrakte Methode, Test-Doubles nicht mehr instanziierbar |
| Keine Abstraktion, aber viele `isinstance`-Abfragen | der Client unterscheidet Implementierungen selbst |

### Im Team

| Signal | Konkret |
|---|---|
| Eine Form wird zur Pflicht erhoben | „jede Komponente bekommt eine ABC" |
| Eine Form gilt als moderner und damit besser | „Protocols statt ABCs" |
| Annotationen gelten als Laufzeitschutz | „mit Type Hints kann nichts Falsches übergeben werden" |
| Niemand kann die zweite Implementierung nennen | „die kommt bestimmt noch" |

---

## Stufe 2 · Erkenntnisse

**1. Abstrahiert wird, was ein Client braucht.**
Ein Vertrag, der aus der Sicht der Implementierung entworfen wird, sammelt alles, was eine Implementierung kann. Ein Vertrag aus Sicht des Clients enthält, was er aufruft.

**2. Größe koppelt stärker als Form.**
Ein Protocol mit neun Methoden bindet einen Client ebenso an neun Methoden wie eine ABC mit neun Methoden. Wer eine ABC durch ein gleich großes Protocol ersetzt, ändert die Kopplung kaum.

**3. ABC und Protocol beantworten verschiedene Fragen.**
Die ABC fragt: „Gehört diese Klasse zur Familie?" Das Protocol fragt: „Kann dieses Objekt, was ich brauche?" Beide Fragen sind berechtigt.

**4. Type Hints sind ein Vertrag für Werkzeuge.**
Python prüft Annotationen zur Laufzeit nicht. Eine Absicherung entsteht erst, wenn ein Type Checker läuft.

**Was gesucht wird:** der kleinste Vertrag, der die Zusammenarbeit an dieser Grenze beschreibt, und die Form, die zu Implementierungen und Werkzeugen passt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Keine Abstraktion** | es eine Implementierung gibt, keine zweite absehbar ist und Tests keinen Ersatz brauchen |
| **Duck Typing** | die Grenze lokal ist, das benötigte Verhalten offensichtlich und statische Prüfung nicht wichtig |
| **Protocol** | die Grenze öffentlich ist, fremde oder unabhängig entstandene Klassen passen sollen, ein Type Checker helfen soll |
| **ABC** | eine bewusst modellierte Typfamilie existiert, gemeinsame Implementierung dazugehört oder die Vollständigkeit beim Instanziieren geprüft werden soll |
| **Mehrere kleine Verträge** | verschiedene Clients verschiedene Teile desselben Objekts brauchen |

---

## Stufe 4 · Entscheidung

### Frage 1 — Braucht diese Grenze überhaupt eine Abstraktion?

- **Ja**, wenn es mehrere Implementierungen gibt, eine zweite konkret absehbar ist, Tests einen Ersatz brauchen oder die Grenze Verantwortlichkeiten trennt.
- **Nein**, wenn keiner dieser Gründe zutrifft → konkrete Klasse direkt verwenden. Eine Abstraktion lässt sich später einführen, wenn der Grund entsteht.

Der Prüfstein: Kann jemand die zweite Implementierung oder den Test benennen, der sie braucht?

### Frage 2 — Was ruft der Client tatsächlich auf?

Die Liste dieser Operationen ist der Vertrag. Alles darüber hinaus gehört zu einem anderen Client oder zu keinem.

### Frage 3 — Woher kommen die Implementierungen?

- **Aus fremdem oder unabhängigem Code** → Protocol oder Duck Typing. Eine ABC erzwingt Adapter.
- **Aus einer eigenen, bewusst gebauten Familie** → weiter mit Frage 4.

### Frage 4 — Teilen die Implementierungen Code oder einen Ablauf?

- **Ja** → ABC. Sie kann gemeinsame Implementierung tragen und fehlende Methoden beim Instanziieren melden.
- **Nein** → Protocol oder Duck Typing genügt.

### Frage 5 — Wer soll den Vertrag prüfen?

- **Ein Type Checker** → Protocol oder ABC mit Annotationen.
- **Leser und Dokumentation genügen** → Duck Typing mit Docstring.
- **Der Code zur Laufzeit** → ABC mit `isinstance`, oder Protocol mit `@runtime_checkable`. Letzteres prüft nur, ob die Methoden vorhanden sind, nicht ihre Signaturen.

---

## Der Denkweg auf einen Blick

```
Ein Objekt arbeitet mit einem Gegenüber zusammen
        ↓
Gibt es Varianten, Testersatz oder eine Grenze?   nein → konkrete Klasse
        ↓ ja
Was ruft der Client auf?  → das ist der Vertrag
        ↓
Kommen Implementierungen von außen?        ja → Protocol oder Duck Typing
        ↓ nein
Teilen sie Code oder Ablauf?               ja → ABC
        ↓ nein
Soll ein Type Checker prüfen?              ja → Protocol
        ↓ nein
                   DUCK TYPING MIT DOCSTRING
```

---

## Die eine Prüffrage

> **Welche Operationen ruft dieser Client auf – und wer muss das wissen?**

Und die Gegenfrage für jede bestehende Abstraktion:

> **Welche zweite Implementierung oder welcher Test rechtfertigt sie?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Enthalten Implementierungen leere Rümpfe? | der Vertrag ist größer als der Bedarf |
| Ruft kein Client eine Methode des Vertrags auf? | sie gehört nicht in diesen Vertrag |
| Braucht eine passende fremde Klasse einen Adapter ohne Verhalten? | nominaler Vertrag an einer strukturellen Grenze |
| Existiert genau eine Implementierung seit Jahren? | Abstraktion auf Vorrat |
| Wurde eine ABC durch ein gleich großes Protocol ersetzt? | Form geändert, Kopplung nicht |
| Stehen Type Hints im Code, aber kein Type Checker in der CI? | die Hints dokumentieren, sie sichern nicht ab |

---

## Wenn die Entscheidung steht

**Der Vertrag steht beim Client.**
Ein Protocol für `ServiceUnlockFlow` gehört in die Nähe von `ServiceUnlockFlow`, nicht in die Nähe der Treiberimplementierung. Es beschreibt, was dieser Client braucht.

**Große Implementierungen bleiben unverändert.**
Ein vollständiger Treiber erfüllt jeden kleinen Vertrag, dessen Methoden er besitzt. Kleine Protocols erfordern keinen Umbau auf der Implementierungsseite.

**`register` ist keine Prüfung.**
`Basisklasse.register(Klasse)` lässt `isinstance` zustimmen, ohne eine Methode zu prüfen. Type Checker wie mypy berücksichtigen die Registrierung nicht.

**Neue abstrakte Methoden treffen alle Unterklassen.**
Wer eine ABC erweitert, sollte wissen, wo ihre Unterklassen liegen, auch in fremden Testmodulen.

**Eine entfernte Abstraktion lässt sich wieder einführen.**
Wenn die zweite Implementierung kommt, ist der Vertrag aus dem Client ablesbar. Vorsorglich angelegt, muss er meist korrigiert werden, sobald der tatsächliche Bedarf bekannt ist.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Protocol mit „moderner ABC" | das Protocol verlangt keine Vererbung und trägt in der Regel keine Implementierung |
| Type Hint mit Laufzeitprüfung | `ServiceUnlockFlow("text")` läuft, bis die erste Methode fehlt |
| `@runtime_checkable` mit vollständiger Prüfung | nur Vorhandensein der Attribute, keine Signaturen |
| `ABC.register` mit Implementierung | `isinstance` stimmt zu, keine Methode wird geprüft |
| „gegen Interfaces programmieren" mit „für jede Klasse ein Interface" | der Grundsatz betrifft die Sicht des Clients, nicht die Zahl der Interfaces |
| kleiner Vertrag mit unvollständigem Vertrag | klein heißt: alles, was der Client braucht, und nicht mehr |
