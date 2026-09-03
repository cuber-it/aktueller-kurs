# 2-2 · Trainer-Ergänzungsmaterial: Entity und Value Object

## Kernidee für den Trainer

Eine Frage trägt die Einheit:

> **Interessiert es, ob es dasselbe ist — oder nur, ob es gleich ist?**

Die zweite Botschaft ist die didaktisch wichtigere und wird meist übersehen:

> **Die Antwort hängt vom Kontext ab, nicht vom Ding.**

Ein Geldschein ist für die Kasse ein Betrag, für die Zentralbank ein Einzelstück mit Seriennummer. Wer das verstanden hat, verwendet Tag 1 weiter, statt ihn abzuhaken.

## Einstieg

**Die Geldscheinfrage.** Ohne Vorrede:

> „Ich leihe Ihnen zwanzig Euro. Sie geben mir einen anderen Zwanziger zurück. Ist das in Ordnung?"

Ja. Beim Geld interessiert nur der Wert.

> „Ich leihe Ihnen mein Fahrrad. Sie geben mir ein baugleiches zurück. Ist das in Ordnung?"

Nein. Beim Fahrrad interessiert, ob es **dasselbe** ist.

Zwei Minuten, und der Unterschied sitzt.

**Der Anschluss:** Geld ist ein Wert, das Fahrrad ist ein Ding mit Identität. Das ist die ganze Unterscheidung.

## Der Kontextbezug — der Punkt, der oft fehlt

Sofort nachschieben, bevor sich „Geld ist immer ein Wert" festsetzt:

> „Und wenn die Zentralbank einen Schein sucht, weil er als gestohlen gemeldet ist?"

Dann ist derselbe Schein eine Entity mit Seriennummer.

**Die Regel daraus:**

> Nicht das Ding entscheidet, sondern der Kontext.

**Trainerfrage:**

> „Nennen Sie etwas aus Ihrem System, das in einem Bereich ein Wert und im anderen ein Ding mit Geschichte ist."

Erfahrungsgemäß kommen: Adresse, Artikel, Termin, Dokument.

## Unveränderlichkeit

Der Teil, bei dem Devs zustimmen und PO/Management aussteigen, wenn man ihn technisch erklärt. **Fachlich formulieren:**

> Ein Betrag von 50 Euro wird nicht zu 60 Euro. Es ist dann ein **anderer** Betrag.

Das leuchtet allen ein. Erst danach, und nur wenn die Gruppe es braucht, die Konsequenz für die Umsetzung.

**Warum das lohnt:** Werte, die sich nicht ändern, kann man gefahrlos weitergeben, vergleichen und kopieren. Kein Lebenszyklus, keine Identitätsverwaltung.

## Value Objects tragen Regeln

Der praktisch wertvollste Punkt und der am seltensten genutzte:

> Ein Zeitraum weiß, dass sein Ende nach seinem Beginn liegt.

Solche Regeln gehören zum Wert, nicht in jeden Aufrufer. Ein „Betrag" ohne Währung und Rundungsregel ist eine Zahl, kein Wert.

**Trainerfrage:**

> „Wie oft steht in Ihrem System die Prüfung ,Ende nach Beginn'?"

Die Antwort ist meist: an mehreren Stellen, in mehreren Fassungen.

## Die zwei häufigen Fehler

**Alles zur Entity machen.** Anschrift, Zeitraum, Betrag, Kennzeichen — meist Werte. Der Reflex kommt daher, dass alles gespeichert werden muss und Speicherung nach Identität verlangt. Das ist eine Frage der Ablage, keine des Modells.

**Werte als bloße Zahlen führen.** Ein Betrag als Kommazahl, ein Kennzeichen als Zeichenkette. Dann gibt es keinen Ort für die Regeln, die dazugehören.

## Die Übung

Erfahrungsgemäß:

- Die klaren Fälle gehen schnell.
- **Streit gibt es bei „Adresse".** Das ist gewollt: Für den Versand ein Wert, für die Bestandspflege eventuell ein Ding mit Historie. Beide Antworten sind vertretbar — die Begründung zählt.
- **Der Kontextbezug wird vergessen.** Wenn die Gruppe „X ist eine Entity" sagt, nachfragen: „In welchem Kontext?"

**Wenn die Gruppe schnell fertig ist:** Nach Regeln fragen, die zu den Werten gehören. Das führt direkt zu 2-3.

## Zum Umgang mit gemischten Gruppen

Diese Einheit funktioniert bei PO und Management gut, wenn man bei den Beispielen bleibt (Geld, Fahrrad, Adresse) und die Umsetzungsfragen zurückstellt.

**Zurückstellen, wenn es kommt:**

| Frage | Antwort |
|---|---|
| „Wie speichert man Value Objects?" | Später. Erst die fachliche Entscheidung. |
| „Was ist mit Gleichheit und Hashwerten?" | Umsetzungsdetail, hängt von der Sprache ab. |
| „Brauchen Entities immer eine technische Kennung?" | Nein — eine fachliche Identität ist besser, wenn es eine gibt. |

## Typische Fragen

**„Ist eine Entity nicht einfach eine Tabelle?"**
Nein. Speicherung und Modell sind zwei Fragen. Ein Value Object kann in derselben Tabelle liegen wie seine Entity.

**„Woran erkenne ich eine Entity sicher?"**
Wenn es sinnvoll ist, ihre Geschichte zu erzählen, sie zu suchen oder zu verfolgen. Bei einem Wert wäre das sinnlos.

**„Kann eine Entity zum Value Object werden?"**
Nicht dieselbe im selben Kontext. Aber dasselbe Ding kann in zwei Kontexten verschieden eingeordnet sein — genau das ist der Punkt.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Geldschein- und Fahrradfrage | 8 |
| Kontextbezug, Unveränderlichkeit | 10 |
| Fallbeispiel lesen lassen | 10 |
| Übung | 12 |
| Auswertung, Regeln in Werten | 10 |

## Übergang

> „Jetzt haben wir die Dinge und die Werte. Was fehlt, ist die Frage, welche davon **zusammen** gültig bleiben müssen — und das ist die schwierigste Entscheidung des taktischen Designs."
