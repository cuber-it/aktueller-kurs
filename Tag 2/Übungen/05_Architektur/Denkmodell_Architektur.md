# Denkmodell · Fachlichkeit von Ablauf trennen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### In der Anwendung

| Signal | Konkret |
|---|---|
| Eine Regel ist nur mit laufender Umgebung prüfbar | Datenbank, Fremdsysteme, Versand müssen erreichbar sein |
| Dieselbe Frage wird an mehreren Stellen beantwortet | drei Fassungen, drei Ergebnisse |
| Attrappen werden gebaut, um Fachlogik zu prüfen | ein Symptom, keine Lösung |
| Eine Ablaufsteuerung wächst, die Regel bleibt darin | jeder neue Schritt liegt zwischen Regel und Ergebnis |
| Ein Zugang liefert Datenstrukturen statt Gegenstände | die Fachlogik liegt außerhalb |
| Ein Fachbaustein hat sehr viele Methoden | Sammelstelle für alles, was nirgends passte |

### Im Gespräch

| Signal | Deutet auf |
|---|---|
| „Ich kann nicht sagen, ob die Regel stimmt" | der Fachvertreter kann sie nicht lesen |
| „Da müsste man den Ablauf durchgehen" | die Regel hat keinen Ort |
| „Das prüfen wir an drei Stellen" | keine gemeinsame Antwort |
| Eine Analyse dauert länger als die Korrektur | die Regel ist eingebettet |

---

## Stufe 2 · Erkenntnisse

**1. Fachliche Regeln gelten unabhängig von Technik.**
Sie gälten auch auf Papier. Das Modell sollte so gebaut sein.

**2. Der Anteil des Fachlichen ist klein.**
In siebzehn Schritten waren vier fachlich. Genau deshalb verschwinden sie zwischen den technischen.

**3. Wo eine Regel keinen Ort hat, gibt es sie mehrfach.**
Drei Fassungen entstehen nicht durch Nachlässigkeit, sondern weil jede Stelle die Frage selbst beantworten muss.

**Was gesucht wird:** der eine Ort, an dem eine Regel steht — prüfbar ohne laufende Umgebung.

---

## Stufe 3 · Optionen

Wohin gehört eine fachliche Regel?

| Option | Käme in Frage, wenn |
|---|---|
| **Zum Gegenstand** | sie betrifft einen Gegenstand und dessen Zustand |
| **Zum Wert** | sie betrifft die Beschaffenheit eines Werts |
| **Eigener Fachbaustein** | sie braucht mehrere Gegenstände oder eine eigenständige Fachlichkeit |
| **Ablaufsteuerung** | **nie** — dort gehört keine Regel hin |

---

## Stufe 4 · Entscheidung

### Frage 1 — Ist der Schritt fachlich?

> **Würde der Fachbereich diese Regel kennen?**

- **Ja** → fachlich
- **Nein**, es geht um holen, speichern, senden → Ablauf
- **Beides** → trennen

### Frage 2 — Enthält der Schritt eine Entscheidung **und** einen Zugriff?

Dann ist er vermischt. Die Trennung:

| Teil | Wohin |
|---|---|
| Angaben beschaffen | Ablauf, **vorher** |
| Entscheiden | fachlich, mit den Angaben als Parameter |

**Achtung auf die Reihenfolge.** Wer trennt, aber die Reihenfolge belässt, hat denselben Fehler: Die Angabe kommt zu spät.

### Frage 3 — Zu welchem Gegenstand gehört die Regel?

- **Zu einem** → Methode an diesem Gegenstand
- **Zu keinem** → eigener Fachbaustein
- **Zu mehreren** → eigener Fachbaustein

**Der Prüfstein:** Kann einer der beteiligten Gegenstände die Frage allein beantworten, wenn er die nötigen Angaben bekommt? Dann gehört sie zu ihm.

### Frage 4 — Wird die Frage an mehreren Stellen gestellt?

Dann eine Methode, die alle aufrufen — mit Begründung im Ergebnis, damit die Oberfläche etwas anzeigen kann.

**Zweistufig:**

| Stufe | Zweck |
|---|---|
| Frage | für Anzeige und Vorabprüfung |
| Durchführung | prüft erneut und verweigert bei Verstoß |

**Warum zweimal:** Zwischen Anzeige und Durchführung können Minuten liegen. Die Anzeige ist eine Auskunft, die Durchführung eine Zusicherung.

---

## Der Denkweg auf einen Blick

```
Ein Ablauf soll zerlegt werden
        ↓
Je Schritt: Wuerde der Fachbereich die Regel kennen?
        ↓ nein → Ablauf
        ↓ ja
Enthaelt der Schritt auch einen Zugriff?
        ↓ ja → trennen: beschaffen (vorher), entscheiden (fachlich)
        ↓ nein
Zu welchem Gegenstand gehoert die Regel?
        ↓ zu einem → Methode dort
        ↓ zu keinem oder mehreren → eigener Fachbaustein
        ↓
Wird die Frage mehrfach gestellt?   ja → eine Methode, alle rufen sie
```

---

## Die eine Prüffrage

> **Würde der Fachbereich diese Regel kennen?**

Und die praktische Probe:

> **Was muss laufen, damit ich diese Regel einmal ausführen kann?**

Wenn die Antwort mehr als „nichts" lautet, steckt die Regel in der Technik.

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Hat der Ablauf gar keine Regel? | keine Trennung nötig |
| Ist die Regel trivial? | eine Zeile im Ablauf ist vertretbar |
| Hat der Fachbaustein sehr viele Methoden? | Sammelstelle — das Modell ist wieder ohne Verhalten |
| Liefert der Zugang Datenstrukturen? | die Fachlogik ist wieder draußen |
| Wird nur gelesen und angezeigt? | dann braucht es kein geschütztes Modell |

---

## Wenn die Entscheidung steht

**Die Ablaufsteuerung enthält keine Regel.**
Sie holt, ruft, speichert, meldet. Wer dort rechnet oder entscheidet, hat das Modell umgangen.

**Die Reihenfolge gehört geprüft.**
Eine Angabe, die nach der Entscheidung beschafft wird, geht nicht in sie ein. Das ist eine eigene Fehlerquelle, unabhängig von der Trennung.

**Regeln liefern Begründungen, nicht nur ja/nein.**
Die Oberfläche will einen Hinweis anzeigen, die Partnerschnittstelle einen Ablehnungsgrund melden. Ein Wahrheitswert reicht dafür nicht.

**Die Grenze nach außen übersetzt.**
Was aus einem Fremdsystem kommt, kommt in dessen Begriffen. Wer sie unverändert übernimmt, holt fremde Modelle ins eigene — das Thema der Ablösung.

**Der Fachbaustein ist kein Sammelbecken.**
Wenn dort alles landet, was nicht in einen Gegenstand passte, ist das Modell wieder leer. Bei jeder neuen Methode prüfen: Gehört sie wirklich zu keinem Gegenstand?

**Bei einfachen Abläufen ist die Trennung Überbau.**
Drei technische Schritte ohne Regel brauchen keine Struktur. Der Aufwand lohnt, wo Regeln gelten und geprüft werden müssen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Schichtenarchitektur | eine Bauform; hier geht es um die Frage, wo eine Regel steht |
| Datenzugriffsschicht | ein Zugang liefert Gegenstände, nicht Datensätze |
| Hilfsklasse | ein Fachbaustein trägt Regeln, kein Werkzeug |
| Ablaufsteuerung mit Prüfungen | Prüfungen sind Regeln und gehören nicht dorthin |
| Eingabevalidierung | „Feld ausgefüllt" ist Eingabe, „Betrag nicht negativ" ist fachlich |
