# 2-1 · Trainer-Ergänzungsmaterial: Vom strategischen zum taktischen Design

## Kernidee für den Trainer

Die Brückeneinheit. Sie hat zwei Aufgaben:

1. Tag 1 zusammenfassen und zeigen, worauf heute aufgebaut wird.
2. Die **Leitfrage des Tages** setzen — sie trägt bis 2-4.

> **Was muss zusammen gültig bleiben, und was darf auseinanderlaufen?**

Wer diese Frage im Kopf behält, versteht Aggregate und Domain Events als zwei Seiten derselben Entscheidung.

## Einstieg — der Rückblick

**Nicht dozieren, fragen.** Fünf Minuten:

> „Was war gestern die wichtigste Erkenntnis für Sie?"

Die Antworten anschreiben. Zwei Dinge sollten fallen: dass Bedeutungen berechtigt verschieden sind, und dass Grenzen dort verlaufen, wo die Bedeutung wechselt.

**Falls die Rückmeldefrage vom Vortag gestellt wurde** („Welchen Begriff würden Sie als Erstes überprüfen?"), hier darauf zurückkommen.

## Die Einordnung

Ein Bild, das trägt:

> Gestern haben wir die **Grundstücksgrenzen** gezogen. Heute bauen wir **innerhalb** eines Grundstücks.

Daraus folgt die wichtigste Vorbedingung, die ausgesprochen gehört:

**Taktisches Design ohne Kontextgrenze ist sinnlos.** Wer nicht weiß, für welchen Zweck er modelliert, kann nicht entscheiden, was zusammengehört.

**Trainerfrage:**

> „Warum kann man Aggregate nicht sinnvoll schneiden, bevor die Kontextgrenzen stehen?"

Antwort: Weil die Konsistenzregel vom Zweck abhängt. Was in der Anmietung zusammen gültig sein muss, ist in der Abrechnung gleichgültig.

## Die Bausteine im Überblick

Kurz halten — jeder bekommt später eine eigene Einheit. Hier nur die Landkarte:

| Baustein | Beantwortet |
|---|---|
| Entity | Hat es Identität über die Zeit? |
| Value Object | Ist es durch seine Werte bestimmt? |
| Aggregate | Was muss zusammen gültig bleiben? |
| Domain Event | Was ist geschehen, das andere angeht? |
| Repository | Woher kommt ein Aggregate? |
| Domain Service | Wohin mit Logik, die keinem Ding gehört? |

**Nicht mehr als fünf Minuten dafür.** Wer hier alles erklärt, nimmt den folgenden Einheiten die Spannung.

## Der Punkt, der oft fehlt

> **Es ist kein Baukasten, den man abarbeitet.**

Nicht jedes Modell braucht alle Bausteine. Ein Kontext mit drei Begriffen und einer Regel braucht kein Repository und keine Factory.

**Trainerfrage:**

> „Kennen Sie ein System, in dem jede Klasse ein Repository hat?"

Erfahrungsgemäß kommt Zustimmung — und damit die Gelegenheit zu sagen, dass Struktur ohne Anlass Kosten ohne Nutzen sind.

## Was Tag 1 vorgibt

Ausdrücklich betonen: **Die Sprache des Kontextes ist die Sprache des Modells.**

Wer heute neue Begriffe erfindet, weil sie technisch praktischer sind, hebt die Arbeit von gestern auf. Das ist der häufigste Rückfall zwischen Tag 1 und Tag 2.

## Konsistenz kostet — der Vorgriff

Ein Satz, der in 2-3 wieder auftaucht und hier vorbereitet wird:

> Was zusammen gültig bleiben muss, muss **zusammen geändert** werden.

Das begrenzt Nebenläufigkeit, Verteilbarkeit und Änderungstempo. Deshalb ist die Klammer eine Entscheidung mit Preis, keine Ordnungsübung.

## Typische Fragen

**„Brauchen wir das alles, wenn wir schon eine Architektur haben?"**
Die Bausteine sind unabhängig von der Architektur. Sie beantworten Modellfragen, keine Strukturfragen.

**„Ist das nicht einfach objektorientierter Entwurf?"**
Weitgehend ja. Neu ist die Betonung der Konsistenzgrenze und die Verbindung zur Fachsprache.

**„Geht das auch ohne Objektorientierung?"**
Ja. Die Fragen bleiben dieselben; die Umsetzung sieht anders aus.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Rückblick auf Tag 1, Rückmeldefrage | 10 |
| Einordnung, Vorbedingung | 8 |
| Bausteine im Überblick | 8 |
| Kein Baukasten, Leitfrage setzen | 8 |
| Ausblick auf den Tag | 5 |

Diese Einheit ist bewusst kürzer als 50 Minuten. Der Puffer geht an 2-3, die erfahrungsgemäß überzieht.

## Übergang

> „Bevor wir über Klammern reden, brauchen wir die Dinge, die geklammert werden. Fangen wir mit der einfachsten Frage an: Wann ist etwas dasselbe, und wann nur gleich?"
