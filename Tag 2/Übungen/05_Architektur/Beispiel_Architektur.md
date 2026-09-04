# Beispiel · Fachlichkeit und Ablauf in klein

Ein Ablauf mit fünf Schritten, vollständig zerlegt.

---

## Der Ablauf

Eine Bibliothek. Ein Benutzer leiht ein Buch aus.

| # | Schritt |
|---|---|
| 1 | Benutzerkonto holen |
| 2 | Prüfen, ob der Benutzer ausleihen darf |
| 3 | Exemplar holen |
| 4 | Exemplar als ausgeliehen kennzeichnen und Frist setzen |
| 5 | Quittung drucken |

## Was der Fachbereich sagt

**Zur Ausleihberechtigung:** „Wer überzogene Medien hat, darf nicht ausleihen. Wer mehr als zwanzig hat, auch nicht. Bei Kindern sind es zehn."

**Zur Frist:** „Vier Wochen. Bei Präsenzbeständen zwei. Bei vorgemerkten Titeln auch zwei, damit der Nächste schneller drankommt."

---

## Schritt 1 · Die Zuordnung

| # | Schritt | Einordnung |
|---|---|---|
| 1 | Benutzerkonto holen | **Ablauf** |
| 2 | Prüfen, ob ausleihen erlaubt ist | **fachlich** |
| 3 | Exemplar holen | **Ablauf** |
| 4 | Kennzeichnen und Frist setzen | **beides vermischt** |
| 5 | Quittung drucken | **Ablauf** |

## Schritt 2 · Den vermischten Schritt trennen

**Schritt 4 enthält zwei Dinge:**

| Teil | Art |
|---|---|
| Frist berechnen | **fachlich** — vier Wochen, zwei bei Präsenz oder Vormerkung |
| Exemplar kennzeichnen | fachlich — der Zustandswechsel |

Beides ist fachlich, aber es sind zwei Regeln. Die Fristberechnung braucht eine Angabe, die im Exemplar nicht steht: ob der Titel vorgemerkt ist.

**Die Trennung:**

| Schritt | Neu |
|---|---|
| 3a | Exemplar holen (Ablauf) |
| 3b | Vormerkstand des Titels beschaffen (Ablauf) |
| 4a | Frist berechnen (fachlich, braucht Bestandsart und Vormerkstand) |
| 4b | Exemplar als ausgeliehen kennzeichnen (fachlich, beim Exemplar) |

**Die Reihenfolge ist entscheidend:** 3b muss vor 4a stehen. Wer die Vormerkung erst danach abfragt, berechnet eine falsche Frist.

**Das ist derselbe Fehler wie im großen Fall** — dort standen die Konditionen hinter der Prüfung.

## Schritt 3 · Wohin die Regeln gehören

### „Darf der Benutzer ausleihen?"

**Betrifft:** das Benutzerkonto — Zahl der überzogenen, Zahl der laufenden Ausleihen, Altersgruppe.

**Alles beim Konto vorhanden.** Die Regel gehört als Methode dorthin.

> „Darf ich ausleihen?" → ja/nein mit Begründung

### „Wie lang ist die Frist?"

**Braucht:** Bestandsart (vom Exemplar) und Vormerkstand (vom Titel).

**Zwei Gegenstände.** Keiner kann die Frage allein beantworten.

**Einordnung: eigener Fachbaustein** — die Fristberechnung.

**Gegenprobe:** Könnte das Exemplar es? Es kennt den Vormerkstand des Titels nicht. Könnte der Titel es? Er kennt die Bestandsart des einzelnen Exemplars nicht. Ein eigener Baustein ist richtig.

## Schritt 4 · Die Prüfung

**Was muss laufen, um „darf ausleihen" zu prüfen?**

| Vorher | Nachher |
|---|---|
| Datenbank mit Benutzerkonto | nichts |
| Exemplarbestand | nichts |
| Drucker oder Attrappe | nichts |

**Die Prüfung besteht aus:** ein Konto mit bestimmten Werten erzeugen, fragen, Antwort ansehen.

**Was man dem Fachbereich zeigen kann:**

| Fall | Erwartung |
|---|---|
| 19 Ausleihen, keine überzogen | darf |
| 20 Ausleihen, keine überzogen | darf nicht |
| 5 Ausleihen, eine überzogen | darf nicht |
| Kind, 9 Ausleihen | darf |
| Kind, 10 Ausleihen | darf nicht |

Die Bibliothekarin liest die Liste und sagt „stimmt" — oder „bei Lehrkräften gelten andere Grenzen".

---

## Was dieses Beispiel zeigt

**Von fünf Schritten sind zwei fachlich**, einer vermischt. Das übliche Verhältnis.

**Der vermischte Schritt enthielt eine versteckte Abhängigkeit.** Die Vormerkung wurde gebraucht, aber nirgends beschafft — das fiel erst beim Trennen auf.

**Die Reihenfolge ist ein eigener Fehler.** Wer trennt, aber die Beschaffung hinten lässt, hat nichts gewonnen.

**Zwei Regeln, zwei Orte.** Die eine gehört zum Konto, die andere in einen eigenen Baustein — weil sie zwei Gegenstände braucht.

**Die Prüfbarkeit ist das Ergebnis.** Aus „Datenbank, Bestand und Drucker" wird „nichts". Und der Fachbereich kann mitlesen.

---

## Zum Vergleich: alles im Ablauf

Angenommen, beide Regeln stehen in der Ablaufsteuerung.

| Frage | Antwort |
|---|---|
| Wo steht die Ausleihgrenze? | in Schritt 2 des Ausleihablaufs |
| Wo steht sie noch? | in der Oberfläche, zum Ausgrauen der Schaltfläche |
| Und noch? | in der Selbstverbuchung am Automaten |
| Sind alle drei gleich? | vermutlich nicht |

**Drei Stellen, drei Gelegenheiten für Abweichung** — genau der Befund aus dem großen Fall.
