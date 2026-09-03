# 1-2 · Trainer-Ergänzungsmaterial: Domäne und Modell

## Kernidee für den Trainer

Ein Satz trägt die ganze Einheit:

> **Ein Modell ist eine Auswahl, kein Abbild.**

Alles Weitere folgt daraus. Wer das verstanden hat, versteht auch, warum es mehrere richtige Modelle derselben Domäne geben kann — und das ist die Voraussetzung für Bounded Contexts in 1-5.

**Diese Einheit kommt ohne Code aus.** Modelliert wird mit Begriffen, Merkmalen und Regeln. Wer hier Klassen zeichnet, nimmt Tag 2 vorweg und lenkt vom Kern ab.

## Einstieg

**Die Landkartenfrage.** Zwei Karten derselben Stadt zeigen — eine U-Bahn-Karte, eine Wanderkarte.

> „Welche ist richtig?"

Beide. Sie treffen verschiedene Auswahlen für verschiedene Zwecke. Die U-Bahn-Karte verzerrt Entfernungen und lässt Straßen weg — und ist deshalb brauchbar.

**Der Anschluss:** Was eine Karte weglässt, gehört zur Karte. Dasselbe gilt für Modelle.

Diese zwei Minuten ersparen später viel Diskussion darüber, ob ein Modell „vollständig" sein muss.

## Der Zweck ist die erste Frage

Der Kern der Einheit und der Punkt, an dem die meisten Systeme gescheitert sind:

> **Ohne benannten Zweck lässt sich nicht entscheiden, was ins Modell gehört.**

Im Fallbeispiel lautete der Auftrag 2009: „ein System, das unsere Fahrzeuge und Vermietungen verwaltet". Das ist eine **Zuständigkeit**, kein Zweck. Ergebnis: 61 Merkmale, von denen 19 gefüllt sind, und eine fachliche Frage, die niemand beantworten kann.

**Trainerfrage:**

> „Was war der Zweck Ihres letzten Systems — in einem Satz?"

Wenn die Antwort mit „verwalten" endet, ist der Punkt gemacht.

**Der Prüfstein:** Ein Zweck muss etwas **ausschließen** können.

## Die drei Fragen, mit denen ein Modell entsteht

Der praktisch nützlichste Teil der Einheit. An die Tafel:

Nicht fragen: *„Welche Daten haben Sie?"*

Sondern:

1. **Welche Entscheidungen treffen Sie?**
2. **Woran machen Sie sie fest?**
3. **Was passiert, wenn Sie falsch entscheiden?**

Die dritte deckt Regeln auf, die niemand für erwähnenswert hält, weil sie selbstverständlich sind.

**Warum die erste Frage nicht funktioniert:** Ein Berater, der nach Daten fragt, bekommt Formulare und Listen. Daraus entsteht ein Datenbestand, kein Modell — genau der Fehler von 2009.

## Der aufschlussreichste Satz jedes Fachgesprächs

> **„Was mich nicht interessiert …"**

In beiden Gesprächsauszügen der Übung kommt er vor. Er zieht die Grenze des Modells — und wird beim Zuhören regelmäßig überhört, weil er wie eine Nebenbemerkung klingt.

**Ansage vor der Übung:** „Achten Sie besonders auf die Sätze, die mit ,was mich nicht interessiert' beginnen."

## Regeln gehören ins Modell

Der zweite Punkt, der oft fehlt. Ein Modell besteht nicht nur aus Begriffen und Merkmalen, sondern auch aus dem, was zwischen ihnen gilt.

Beispiel aus der Übung:

> „Wenn es hier ist, gehört es mir. Die Station kann es nicht mehr vermieten."

| | |
|---|---|
| Als Merkmal | „Zustand: in der Werkstatt" |
| Als Regel | „In diesem Zustand ist Vermieten ausgeschlossen" |

Ein Merkmal beschreibt, eine Regel schließt aus. Wer nur das Merkmal führt, muss die Ausschlusslogik an jeder Stelle wiederholen.

## Die Übung

Zwei Fachgespräche, zwei Zwecke, zwei Modelle. Erfahrungsgemäß:

- **Die Modelle geraten zu groß.** Teilnehmer nehmen auf, was vorkommt, statt was gebraucht wird. Eingreifen mit: „Trägt dieser Begriff eine Entscheidung?"
- **Regeln werden vergessen.** Die meisten schreiben Begriffe und Merkmale, aber nicht die Regeln. Gezielt danach fragen.
- **Aufgabe 4 (Fahrzeug in beiden Modellen) ist der Kern.** 8.400 Einzelobjekte gegen acht Kategorien — das ist kein Detailunterschied, sondern zwei Sachen mit einem Namen. Hier entsteht der Übergang zu 1-3 und 1-5.
- **Aufgabe 7 (gemeinsames Modell) führt zum Aha.** Wer es aufschreibt, merkt selbst, dass „Fahrzeug" beides zugleich sein müsste.

**Wenn die Gruppe schnell fertig ist:** Aufgabe 9 und 10 vertiefen — die Erfahrung „manche werden härter rangenommen". Das ist eine echte Modellierungsfrage ohne eindeutige Antwort.

## Erfahrung modellieren

Aufgabe 9 und 10 sind der anspruchsvollste Teil und lohnen Zeit.

**Der Punkt:** Ein Modell kann kein Bauchgefühl abbilden. Es kann abbilden, **woran** sich das Bauchgefühl festmacht — sobald das benannt ist.

**Die gute Frage an den Fachbereich:**

> „Woran sehen Sie, dass ein Fahrzeug härter rangenommen wurde?"

**Die schlechte:**

> „Können Sie Ihre Erfahrung formalisieren?"

Diesen Unterschied vorführen. Er ist übertragbar auf jede Anforderungserhebung.

**Die zweite gute Frage:** „Bei welchen Fahrzeugen lagen Sie zuletzt daneben?" — Fehler sind oft aufschlussreicher als Regeln.

## Was nicht in diese Einheit gehört

Ausdrücklich zurückstellen, wenn es aus der Gruppe kommt:

| Thema | Gehört zu |
|---|---|
| Anämisches Modell, Rich Domain Model | Tag 2, Aggregates |
| Entity gegen Value Object | Tag 2 |
| Repository, Factory | Tag 2 |
| Wie wird das gespeichert? | Tag 2, Architektur |
| Klassen und Vererbung | Tag 2 |

**Die Antwort auf solche Fragen:** „Guter Punkt — den heben wir uns für morgen auf. Heute geht es darum, **was** modelliert wird, nicht wie es gebaut ist."

## Typische Fragen

**„Wir haben ein Datenmodell — reicht das nicht?"**
Ein Datenmodell beschreibt, was gespeichert wird. Ein fachliches Modell beschreibt, was entschieden wird. Beide können gleichzeitig richtig sein und verschieden aussehen.

**„Ist ein Modell ohne Vollständigkeit nicht lückenhaft?"**
Vollständigkeit gemessen woran? Ein Modell ist vollständig, wenn es die Fragen seines Zwecks beantwortet. Das Fallbeispiel hat 61 Merkmale und beantwortet die Frage nicht.

**„Wer entscheidet, was ins Modell gehört?"**
Fachbereich und Entwicklung gemeinsam. Der Fachbereich kennt die Entscheidungen, die Entwicklung kennt die Konsequenzen der Modellierung.

**„Was ist mit Daten, die wir aufbewahren müssen, aber nicht brauchen?"**
Die werden gespeichert. Speichern und modellieren sind zwei Fragen — was aufbewahrt werden muss, gehört nicht automatisch ins Modell.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Landkartenfrage, Modellbegriff, Zweck | 12 |
| Fallbeispiel lesen lassen | 10 |
| Kurz andiskutieren, die drei Fragen | 8 |
| Übung: zwei Modelle | 15 |
| Auswertung, besonders Aufgabe 4 und 7 | 10 |

## Übergang

> „Beim Fahrzeug haben wir festgestellt: Zwei Bereiche verwenden dasselbe Wort und meinen Verschiedenes. Das war kein Einzelfall. Sehen wir uns an, was passiert, wenn das durch ein ganzes Unternehmen geht."
