# 2-6 · Trainer-Ergänzungsmaterial: Architektur und Implementierung

## Kernidee für den Trainer

Die Einheit mit dem größten Gefälle in gemischten Gruppen: Devs wollen Details, PO und Management steigen aus.

**Der Ausweg:** Ein Gedanke trägt alles, und er ist nicht technisch.

> **Das Modell hängt von nichts ab. Alles andere hängt von ihm ab.**

Hexagonal, Onion, Clean Architecture sind drei Namen dafür. Wer den Gedanken hat, braucht die Namen nicht.

## Einstieg

**Die Prüfbarkeitsfrage.** Ohne Vorrede:

> „Wenn Sie prüfen wollen, ob die Regel ,verlängern nur einmal' stimmt — was müssen Sie dafür starten?"

Erfahrungsgemäß: Datenbank, Anwendung, vielleicht die Oberfläche.

> „Und wenn die Regel in einem Modell steht, das nichts davon kennt?"

Nichts. Man ruft sie auf und sieht nach.

**Das ist der ganze Punkt.** Alles Weitere ist Ausgestaltung.

## Die vier Bausteine

Kurz und mit Abgrenzung. Die Abgrenzungen sind das Wertvolle, nicht die Definitionen.

### Repository oder Factory

| | Repository | Factory |
|---|---|---|
| Antwort auf | „Hol mir das Aggregate mit dieser Kennung" | „Erzeuge ein neues, gültiges Aggregate" |
| Liefert | was es gibt | was es noch nicht gab |

**Fachliche Formulierung:** Holen oder erzeugen.

**Wichtig:** Ein Repository je **Aggregate**, nicht je Entity. Was innen liegt, kommt über die Wurzel.

### Domain Service oder Application Service

| | Domain Service | Application Service |
|---|---|---|
| Enthält | Fachlogik | Ablaufsteuerung |
| Beispiel | Umbuchung zwischen zwei Konten | Aggregate holen, Methode rufen, speichern, melden |
| Fachvertreter erkennt es | ja | nein |

**Der Prüfstein:**

> Würde der Fachbereich diese Regel kennen?

Ja → Domain Service. Nein → Application Service.

**Der häufigste Fehler:** Im Application Service wird gerechnet. Dann ist das Modell umgangen, und die Regeln liegen wieder außen.

## Schichten — fachlich erklärt

Für gemischte Gruppen ohne Architekturdiagramm:

> Die Fachlichkeit steht in der Mitte. Datenbank, Oberfläche und Fremdsysteme stehen außen. Innen weiß man nichts von außen.

**Das Bild, das trägt:** Die Fachregeln eines Unternehmens gelten unabhängig davon, ob sie in einem System, auf Papier oder im Kopf einer Sachbearbeiterin liegen. Genau so sollte das Modell gebaut sein.

**Trainerhinweis:** Die drei Namen (Hexagonal, Onion, Clean) nennen und als Varianten desselben Gedankens abtun. Wer sie vergleicht, verliert zwanzig Minuten und gewinnt nichts.

## Die zwei Fehler

**Das Repository gibt Datenstrukturen zurück.** Dann liegt die Fachlogik wieder außerhalb, und das Aggregate ist eine Datenablage.

**Domain Services als Sammelstelle.** Wenn dort alles landet, was nicht in eine Entity passte, ist das Modell wieder anämisch — nur mit anderem Namen.

**Trainerfrage:**

> „Wenn Ihr Domain Service dreißig Methoden hat — was ist dann passiert?"

## Der Preis

Ausdrücklich nennen:

- Mehr Struktur, mehr Übersetzung zwischen den Schichten
- Bei einfachen Anwendungen Aufwand ohne Gegenwert
- Wer keine Regeln hat, braucht kein Modell zu schützen

**Trainerfrage:**

> „Wo in Ihrem Haus wäre diese Trennung Überbau?"

## Zum Umgang mit gemischten Gruppen

Diese Einheit **kürzen**, wenn PO und Management überwiegen. Was dann bleibt:

- Die Prüfbarkeitsfrage vom Einstieg
- Domain Service gegen Application Service (das ist eine fachliche Unterscheidung)
- Der Grundgedanke „Fachlichkeit innen, Technik außen"

**Was dann entfällt:** Schichtenvarianten, Repository-Details, Umsetzungsfragen.

**Bei überwiegend Devs** umgekehrt: Der Teil kann tiefer gehen, und die Diskussion über Repository-Zuschnitt lohnt sich.

## Typische Fragen

**„Ist ein Repository nicht einfach eine Datenzugriffsschicht?"**
Ähnlich, aber der Zuschnitt unterscheidet sich: je Aggregate, nicht je Tabelle. Und es gibt Aggregate zurück, keine Datensätze.

**„Brauchen wir für jedes Aggregate ein Repository?"**
Für jedes, das von außen geholt wird. Innenliegende Teile nicht.

**„Was ist mit Auswertungen?"**
Gute Frage, und der Punkt, an dem viele scheitern. Auswertungen über Aggregate zu bauen ist mühsam; dafür gibt es getrennte Lesemodelle. Das ist die Brücke zu CQRS — kurz nennen, nicht vertiefen.

**„Wo liegt die Validierung?"**
Fachliche Regeln im Modell, Eingabeprüfungen außen. Ein Betrag darf nicht negativ sein — das ist fachlich. Ein Feld muss ausgefüllt sein — das ist Eingabe.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Prüfbarkeitsfrage | 6 |
| Repository, Factory, die Abgrenzung | 10 |
| Domain gegen Application Service | 10 |
| Schichten, fachlich erklärt | 8 |
| Übung | 12 |
| Auswertung, der Preis | 6 |

## Übergang

> „Wir haben jetzt ein Modell, das geschützt ist. Nur: Die wenigsten von Ihnen fangen bei null an. Wie kommt man dorthin, wenn schon fünfzehn Jahre Software da sind?"
