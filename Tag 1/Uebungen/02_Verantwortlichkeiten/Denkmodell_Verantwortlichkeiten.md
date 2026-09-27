# Denkmodell · Verantwortung schneiden und Zustand schützen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Klassenname ohne Aufgabe | `ImplementTestHelper`, `Utils`, `Manager` |
| Methoden, die einander nicht brauchen | `unlock_service_menu` neben `write_html_report` |
| Eine Methode wird von vielen anderen benutzt, aus verschiedenen Gründen | `load_config()` für Anmeldung, Bericht und Datenbank |
| Öffentlicher Zustand ohne Regeln | `implement.status = "saved"` |
| Gespeicherte Werte, die sich ableiten lassen | `total` neben `items`, `status` neben `closed_at` |
| Aufrufer prüfen Zustand, bevor sie eine Methode aufrufen | `if terminal.state == "ready": terminal.switch_section(...)` |
| Methode nutzt fast nur Daten eines anderen Objekts | `ReportWriter.line_total(item)` |

### In der Zusammenarbeit

| Signal | Konkret |
|---|---|
| Viele Merge-Konflikte in derselben Datei | mehrere Teams, eine Klasse |
| Eine Änderung bricht Tests eines anderen Bereichs | Berichtskonfiguration bricht Anmeldung |
| Dieselbe Rechnung an mehreren Stellen | Positionsbetrag in Reporting, Buildern, Helper |
| Neue Zustände erzwingen Änderungen in vielen Tests | ein Zustand „gesperrt", 63 Tests angepasst |
| „Das ist nur Testcode" | Infrastruktur wird wie ein Einzeltest behandelt |

---

## Stufe 2 · Erkenntnisse

**1. Verantwortung zeigt sich an Änderungsgründen, nicht an Substantiven.**
Eine Klasse mit vielen Methoden ist in Ordnung, wenn dieselben Ereignisse sie ändern. Eine Klasse mit drei Methoden kann drei Verantwortungen tragen.

**2. Kapselung schützt Regeln, nicht Attribute.**
Der Unterstrich sagt, worauf fremder Code sich nicht verlassen soll. Welche Zustandsänderungen gültig sind, legen erst Methoden fest, die genau diese Änderungen anbieten.

**3. Wer die Daten hat, sollte in der Regel auch die Entscheidungen darüber treffen.**
Wenn Aufrufer Zustand auslesen, um zu entscheiden, wie sie das Objekt bedienen, ist das Wissen an der falschen Stelle.

**4. Testinfrastruktur ist langlebiger Code.**
Ein einzelner Test darf direkt und einfach sein. Was 400 Tests benutzen, lebt Jahre und verdient denselben Schnitt wie Produktivcode.

**Was gesucht wird:** für jede Klasse eine Verantwortung, die sich in einem Satz sagen lässt, und für jeden Zustand die Regeln, die ihn gültig halten.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Klasse nach Änderungsgründen aufteilen** | verschiedene Ereignisse verschiedene Teile der Klasse ändern |
| **Zustandsänderungen als Methoden anbieten** | Attribute zusammen gültig sein müssen |
| **Abgeleitete Werte berechnen statt speichern** | ein Wert sich vollständig aus anderen ergibt |
| **Entscheidung ins Objekt verlagern** | Aufrufer vor jedem Aufruf dieselbe Prüfung wiederholen |
| **Methode zu den Daten verschieben** | sie fast nur Daten eines anderen Objekts verwendet |
| **Funktionen in einem Modul sammeln** | sie dieselbe Art von Aufgabe erledigen und keinen Zustand teilen |
| **Beibehalten** | die Klasse zwar groß ist, aber nur einen Änderungsgrund hat |

---

## Stufe 4 · Entscheidung

### Frage 1 — Lässt sich die Verantwortung in einem Satz sagen?

- **Ja**, ohne „und" zwischen verschiedenen Aufgaben → weiter mit Frage 3.
- **Nein** → weiter mit Frage 2.

Der Prüfstein: Würden die Teams, die die Klasse benutzen, denselben Satz sagen?

### Frage 2 — Welche Ereignisse ändern die Klasse?

Für jede Methode fragen:

1. Welche Änderung im Produkt, in der Infrastruktur oder in der Organisation würde sie ändern?
2. Wer würde diese Änderung anstoßen?

Methoden mit denselben Antworten gehören zusammen. Methoden mit verschiedenen Antworten gehören in verschiedene Klassen oder Module.

### Frage 3 — Gibt es Zustandskombinationen, die fachlich ungültig sind?

- **Nein** → öffentliche Attribute genügen.
- **Ja, weil ein Wert sich aus anderen ergibt** → ableiten statt speichern.
- **Ja, weil mehrere Werte gemeinsam wechseln** → eine Methode für den Übergang, Attribute als Implementierungsdetail.

### Frage 4 — Wer trifft die Entscheidung?

- **Aufrufer prüfen Zustand, um das Objekt korrekt zu bedienen** → die Prüfung gehört ins Objekt.
- **Aufrufer fragen Zustand ab, um selbst etwas zu tun** → legitime Abfrage, etwa in einer Assertion oder für eine Anzeige.
- **Eine Methode rechnet fast nur mit Daten eines anderen Objekts** → prüfen, ob sie dorthin gehört. Sie bleibt, wo sie ist, wenn sie Wissen braucht, das das andere Objekt nicht hat.

---

## Der Denkweg auf einen Blick

```
Eine Klasse ist groß, oder eine Änderung trifft Unbeteiligte
        ↓
Verantwortung in einem Satz sagbar?        ja → weiter unten
        ↓ nein
Welche Ereignisse ändern welche Methoden?
        ↓
Nach Änderungsgrund gruppieren  →  je Gruppe eine Klasse oder ein Modul
        ↓
Gibt es ungültige Zustandskombinationen?   nein → Attribute genügen
        ↓ ja
Wert ableitbar?                            ja → berechnen statt speichern
        ↓ nein
Übergang als Methode, Attribute mit _
        ↓
Prüfen Aufrufer Zustand vor dem Aufruf?    ja → Prüfung ins Objekt
        ↓ nein
                 SCHNITT STEHT
```

---

## Die eine Prüffrage

> **Wofür ist dieses Objekt verantwortlich – und welche Änderung sollte genau hier stattfinden?**

Und die Gegenfrage für jeden Zustand:

> **Gibt es genau einen Weg, ihn gültig zu ändern?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Heißt die Klasse `Helper`, `Utils`, `Manager`, `Common`? | Verantwortung ausdrücklich benennen lassen |
| Ändern mehrere Teams die Klasse aus verschiedenen Gründen? | mehr als eine Verantwortung |
| Kann ein Aufrufer zwei zusammengehörige Attribute einzeln setzen? | Invariante ungeschützt |
| Wird ein Wert gespeichert, der sich berechnen lässt? | Widerspruch möglich |
| Steht vor jedem Aufruf dieselbe `if`-Prüfung? | Entscheidung liegt beim falschen Objekt |
| Steht dieselbe Rechnung an mehreren Stellen? | der Rechnung fehlt ihr Ort |
| Wurde die Klasse nach Zeilen aufgeteilt? | Aufteilung ohne neuen Schnitt |

---

## Wenn die Entscheidung steht

**Erst den Schnitt, dann die Zusammenarbeit.**
Welche Klassen es gibt und wofür sie zuständig sind, ist die erste Entscheidung. Wie sie sich gegenseitig finden, ob über Vererbung, Komposition oder Übergabe, ist Thema von 1-3 und 1-5.

**Invarianten beim Entstehen schützen, nicht beim Export prüfen.**
Eine Validierung am Ende findet ungültige Objekte, sagt aber nicht, wo sie entstanden sind. Eine Methode, die nur gültige Übergänge zulässt, verhindert sie.

**Abfragen bleiben erlaubt.**
Tell, don't ask richtet sich gegen Aufrufer, die Zustand auslesen, um das Objekt korrekt zu bedienen. Eine Assertion, eine Anzeige oder ein Bericht fragt legitim nach Zustand.

**Nicht jede Methode zu den Daten verschieben.**
Feature Envy ist ein Hinweis, keine Regel. Braucht die Berechnung Wissen, das das Datenobjekt nicht hat, bleibt sie beim Aufrufer.

**Große Klassen mit einem Änderungsgrund dürfen groß bleiben.**
Ein Bildschirmobjekt mit vierzig Methoden für vierzig Bedienelemente ist kohäsiv, wenn sich alle mit demselben Bildschirm ändern.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Single Responsibility mit „eine Methode je Klasse" | Verantwortung bemisst sich an Änderungsgründen, nicht an der Zahl der Methoden |
| Kapselung mit Unterstrichen | der Unterstrich markiert, die Methode schützt |
| Kohäsion mit „liegt in derselben Datei" | Kohäsion heißt: ändert sich gemeinsam |
| Tell, don't ask mit „nie Zustand abfragen" | Abfragen zur Anzeige oder für Assertions sind legitim |
| Feature Envy mit falscher Zuordnung | ein Hinweis, der geprüft werden muss |
| Aufteilen mit Verbessern | vier Dateien mit Mixins ändern den Schnitt nicht |
