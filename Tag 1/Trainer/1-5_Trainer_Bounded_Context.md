# 1-5 · Trainer-Ergänzungsmaterial: Bounded Context

## Kernidee für den Trainer

Der Bounded Context ist der zentrale Begriff des strategischen Designs. In den Einheiten 1-3 und 1-4 wurde bereits mit ihm gearbeitet, ohne ihn sauber einzuführen — das geschieht jetzt.

Zwei Botschaften:

**Erstens:** Die Grenze verläuft dort, wo die Bedeutung wechselt. Das ist aus 1-3 bekannt.

**Zweitens, und das ist neu:** Die schwierigere Frage ist nicht *wo verläuft die Grenze*, sondern **was gehört hinein**. Ein Kontext ohne Abgrenzung wächst, weil im Zweifel er zuständig ist.

## Warum ein Modell für alles nicht trägt

Das anschaulichste Argument ist die Tabelle mit 47 Spalten, von denen die meisten für die meisten Sätze leer sind.

**Trainerfrage:**

> „Wie viele Spalten hat Ihre größte Tabelle — und wie viele davon sind bei einem beliebigen Satz gefüllt?"

Die Antworten sind erfahrungsgemäß eindrucksvoll und kommen aus dem eigenen Haus.

## Der Zwecksatz — der schwierigste Teil

Ein Kontext braucht einen Zweck in **einem Satz**, mit einem fachlichen Ergebnis, ohne „und", ohne Ortsangabe.

Die Beispiele aus dem Material vorführen:

| Vorschlag | Warum nicht |
|---|---|
| „Alles, was am Tresen passiert" | Ort statt Fachlichkeit; schließt die Webseite fälschlich aus |
| „Fahrzeuge ausgeben und zurücknehmen" | zu eng, lässt Reservierung weg |
| „Die Kundenbeziehung während der Miete" | zu weit, überschneidet |
| „Vorgänge verwalten **und** Fahrzeuge disponieren" | zwei Klammern |
| **„Verantwortet den Mietvorgang von der Reservierung bis zum Abschluss"** | trägt |

**Die Regel für die Gruppe:** Wenn Sie „und" brauchen, haben Sie zwei Kontexte.

**Der zweite Prüfstein:** Ein Zwecksatz muss **ausschließen** können. „Alles rund um den Mietvorgang" schließt nichts aus und hilft deshalb nicht.

## Die Prüffrage für Zugehörigkeit

> **Würde eine Änderung an dieser Aufgabe auch die übrigen Aufgaben des Kontextes betreffen?**

Diese Frage entscheidet die sechs strittigen Aufgaben der Übung. Sie ist präzise genug für den Kursgebrauch und stößt bei einem Fall an ihre Grenze — der Verfügbarkeitsanzeige, die an zwei Kontexten hängt. Das ist kein Mangel, sondern ehrlich: Manche Fälle bleiben offen.

## Die vier Kriterien und ihre Rangfolge

Der Workshop im Fallbeispiel scheiterte, weil vier Kriterien vermischt wurden. Die Rangfolge ausdrücklich an die Tafel:

| Kriterium | Gewicht |
|---|---|
| Was gehört fachlich zusammen? | **entscheidend** |
| Teilen sich die Aufgaben eine Sprache? | starkes Indiz |
| Wer braucht das Ergebnis? | schwach |
| Wo passiert es? | schwach |
| Wer hat es gebaut? | **kein Kriterium** |

**Trainerfrage:**

> „,Wir haben das damals gebaut, weil wir Kapazität hatten' — ist das ein Grund, dass es dort bleibt?"

## Festlegen oder anwenden

Eine Unterscheidung, die in der Übung zweimal trägt und im eigenen Code sofort anwendbar ist:

- Der Kontext **wendet an**, was ein anderer festlegt → gehört dazu
- Der Kontext **legt fest**, was er braucht → prüfen, ob das eine eigene Verantwortung ist

Beispiel: Firmenkonditionen *anwenden* gehört zur Anmietung. Preise *festlegen* gehört zur Vertragsverwaltung.

## Empfänger kennen

Der subtilste Punkt der Einheit, und der mit dem größten praktischen Wert:

> Ein Kontext meldet, dass etwas geschehen ist. Wer es braucht, holt es sich.

Ein Kontext, der seine Empfänger kennt, muss bei jedem neuen Empfänger geändert werden.

**In der Übung:** Aufgabe 10 (Schadensfotos weiterleiten) wird aufgeteilt — speichern bleibt, weiterleiten geht an die Empfänger.

**Trainerfrage:**

> „Was passiert, wenn ein vierter Empfänger dazukommt?"

## Das Canvas

Acht Felder. Das wichtigste ist das letzte und steht nicht im ursprünglichen Canvas der DDD Crew:

> **Nicht zuständig für …**

Ausdrücklich betonen: Ohne dieses Feld wächst jeder Kontext. Es ist der einzige Mechanismus, der Wachstum durch Zweifel verhindert.

## Die Übung

Vierzehn Aufgaben, sechs strittig. Erfahrungsgemäß:

- Der Zwecksatz braucht mehrere Anläufe. Zeit dafür lassen — er ist der Kern.
- Die Aufteilung von Aufgabe 10 wird selten von allein gefunden. Wenn nicht, gezielt fragen: „Gehören ,speichern' und ,weiterleiten' wirklich zusammen?"
- Die Verfügbarkeitsanzeige spaltet die Gruppe. Das ist gewollt — die richtige Antwort ist, sie als offen auszuweisen, mit einem Kriterium für später.

**Der Abschlusstest (Aufgabe 7):** Die Frage nach der Zusatzleistungs-Auswertung. Wenn die Gruppe sie anhand ihres Canvas in zwei Sätzen beantwortet, hat die Einheit funktioniert.

## Typische Fragen

**„Ist ein Bounded Context dasselbe wie ein Microservice?"**
Nein. Ein Kontext kann in einem Monolithen liegen. Wenn ein Service geschnitten wird, ist der Kontext allerdings eine gute Schnittlinie.

**„Wie groß darf ein Kontext sein?"**
Kein Zahlenwert. Der Prüfstein ist der Zwecksatz: Passt er in einen Satz ohne „und"?

**„Was ist mit einem Kontext für eine einzige Aufgabe?"**
Zulässig, wenn die Fähigkeit eigenständig ist und von mehreren genutzt wird. Der Aufwand ist die Grenze, nicht die Größe. In der Lösung wird das kritisch diskutiert.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Begriff, warum ein Modell nicht trägt | 8 |
| Fallbeispiel lesen lassen | 10 |
| Zwecksatz, Kriterien, Rangfolge | 12 |
| Übung: Canvas ausfüllen | 15 |
| Auswertung | 10 |

## Übergang

> „Sie haben eben ,Core Domain' ins Canvas geschrieben und es mit ,da findet das Kerngeschäft statt' begründet. Das ist keine Begründung. Jetzt sehen wir uns an, was eine Core Domain wirklich ausmacht."
