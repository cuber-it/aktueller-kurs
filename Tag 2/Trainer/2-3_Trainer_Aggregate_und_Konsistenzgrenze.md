# 2-3 · Trainer-Ergänzungsmaterial: Aggregate und Konsistenzgrenze

## Kernidee für den Trainer

**Die schwierigste Einheit des Kurses.** Sie überzieht regelmäßig — der Puffer aus 2-1 ist dafür gedacht.

Der Kern in einem Satz:

> **Ein Aggregate ist keine Ordnungsübung, sondern eine Konsistenzentscheidung.**

Die Frage lautet nicht „was gehört sachlich zusammen", sondern:

> **Was muss im selben Moment stimmen?**

Wer nach Zugehörigkeit schneidet, baut Aggregate, die halbe Bestände sperren. Wer nach Regel schneidet, baut kleine.

## Einstieg

**Die Bestellfrage.** Ohne Vorrede:

> „Eine Bestellung hat Positionen und eine Gesamtsumme. Die Summe muss der Summe der Positionen entsprechen. Wo verläuft die Klammer?"

Um Bestellung und Positionen — die Regel verbindet sie.

> „Die Bestellung verweist auf einen Kunden. Gehört der Kunde in die Klammer?"

Nein. Es gibt keine Regel, die zwischen Bestellung und Kunde sofort gelten muss.

**Der Anschluss:** Die Regel zieht die Grenze, nicht die Zugehörigkeit. Der Kunde gehört zur Bestellung — aber nicht in dieselbe Klammer.

## Ohne Invariante kein Aggregate

Der Satz, der die meisten Fehlschnitte verhindert:

> **Wenn Sie keine Regel benennen können, die zwischen zwei Dingen sofort gelten muss, gehören sie nicht ins selbe Aggregate.**

**Trainerfrage** bei jedem Vorschlag aus der Gruppe:

> „Welche Regel verbindet die beiden?"

Wenn die Antwort lautet „das gehört doch zusammen", ist es kein Aggregate.

## Sofort oder später — die eigentliche Entscheidung

Die Frage an die Tafel:

| Muss es **sofort** stimmen? | Konsequenz |
|---|---|
| Ja | dasselbe Aggregate |
| Nein, darf kurz auseinanderlaufen | getrennte Aggregate, Nachziehen über ein Ereignis |

**Das ist keine technische, sondern eine fachliche Frage.** Sie gehört dem Fachbereich gestellt:

> „Was passiert, wenn das für fünf Minuten nicht zusammenpasst?"

Erfahrungsgemäß lautet die Antwort öfter „nichts", als Entwickler erwarten. Genau das erlaubt kleine Aggregate.

## Klein halten — und warum das schwerfällt

Der Reflex geht zu großen Aggregaten, weil sie bequem sind: alles zur Hand, keine Übersetzung nötig.

**Der Preis, den man aussprechen muss:**

- Ein großes Aggregate wird bei jeder Änderung als Ganzes gesperrt
- Zwei Leute können nicht gleichzeitig daran arbeiten
- Es lässt sich nicht verteilen
- Es wird langsam, weil viel geladen werden muss

**Trainerfrage:**

> „Wenn zwei Sachbearbeiter gleichzeitig an derselben Bestellung arbeiten — was passiert?"

## Verweise statt Verschachtelung

Ein Aggregate verweist auf ein anderes über dessen Identität, statt es zu enthalten.

**Fachlich formuliert für gemischte Gruppen:**

> Die Bestellung merkt sich, **welcher** Kunde es war — nicht alles über ihn.

Das ist auch außerhalb der Software eine vertraute Vorstellung: Auf dem Lieferschein steht die Kundennummer, nicht die Lebensgeschichte des Kunden.

## Eine Änderung, ein Aggregate

Die Faustregel, die im Alltag am meisten trägt:

> Wer in einem Vorgang mehrere Aggregate ändert, hat entweder falsch geschnitten oder braucht ein Domain Event.

Das ist zugleich die Brücke zu 2-4.

## Die Übung

Erfahrungsgemäß:

- **Die ersten Vorschläge sind zu groß.** Fast immer landet alles in einer Klammer. Gegenmittel: bei jedem Vorschlag nach der Regel fragen.
- **„Gehört dazu" wird als Begründung genannt.** Nicht durchgehen lassen.
- **Die Frage „was passiert, wenn es kurz nicht stimmt" löst den Knoten.** Wenn die Gruppe feststeckt, diese Frage stellen.
- **Streitfälle sind gewollt.** Bei manchen Grenzen gibt es zwei vertretbare Antworten; die Begründung entscheidet.

**Wenn die Gruppe schnell fertig ist:** Nach dem Preis fragen — was kostet der gewählte Schnitt, wenn zwei Leute gleichzeitig arbeiten?

## Der häufigste Fehlschluss

> „Wir schneiden nach den Tabellen, die zusammengehören."

Dann folgt das Aggregate der Speicherung statt der Fachlichkeit — derselbe Fehler wie bei einem Modell, das aus dem Datenbankschema abgeleitet wird.

**Gegenfrage:** „Welche fachliche Regel verbindet sie?"

## Zum Umgang mit gemischten Gruppen

Das Thema ist abstrakt und hat trotzdem einen guten fachlichen Zugang: **Was muss zusammen stimmen?** ist eine Frage, die jeder PO und jede Führungskraft beantworten kann.

**Zurückstellen, wenn es kommt:**

| Frage | Antwort |
|---|---|
| „Wie sperrt man das?" | Umsetzungsdetail — die fachliche Grenze zuerst |
| „Was ist mit Transaktionen?" | Später; die Regel bestimmt die Transaktion, nicht umgekehrt |
| „Wie sieht das in der Datenbank aus?" | Zwei Fragen — Modell und Ablage |

## Typische Fragen

**„Wie groß darf ein Aggregate sein?"**
Kein Zahlenwert. Der Prüfstein ist die Invariante: Was die Regel nicht braucht, gehört nicht hinein.

**„Was, wenn zwei Regeln über Kreuz gehen?"**
Dann sind es Kandidaten für ein größeres Aggregate — oder eine der Regeln muss nicht sofort gelten. Meist das Zweite.

**„Können Aggregate sich überlappen?"**
Nein. Ein Ding gehört zu genau einem Aggregate.

**„Und wenn wirklich alles zusammen stimmen muss?"**
Dann nachfragen: wirklich sofort? Oder nur bis zum Tagesabschluss? Der Unterschied ist entscheidend.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Bestellfrage, Invariante | 10 |
| Fallbeispiel lesen lassen | 10 |
| Sofort oder später, klein halten | 10 |
| Übung | 15 |
| Auswertung | 12 |

**Rechnen Sie mit Überziehung.** Der Puffer aus 2-1 ist dafür da.

## Übergang

> „Wir haben eben festgestellt: Was nicht sofort stimmen muss, gehört in getrennte Klammern. Aber irgendwie muss es ja doch zusammenkommen. Genau dafür gibt es den nächsten Baustein."
