# Beispiel · Zwei Modelle in klein

Derselbe Sachverhalt, zwei Entwürfe. Kürzer als die Übung, zum Nachvollziehen des Vorgehens.

---

## Der Sachverhalt

Eine Bibliothek. Eine Ausleihe.

**Wie die Bibliothekarin spricht:**

> „Ausleihen darf, wer keine überzogenen Medien hat. Vier Wochen, einmal verlängerbar — außer das Buch ist vorgemerkt, dann geht keine Verlängerung."

---

## Modell 1

```
Klasse AusleiheDatensatz
    id
    benutzerId
    exemplarId
    ausleihDatum
    faelligkeitsDatum
    verlaengerungsZaehler
    rueckgabeDatum          (leer, solange nicht zurück)
```

Getter und Setter für alles. Die Regeln liegen in `AusleiheService`.

---

## Modell 2

```
Klasse Ausleihe
    exemplar
    entleiher
    frist

    verlaengern()           -> nur einmal, nicht bei Vormerkung
    zurueckgeben()
    istUeberzogen()

Klasse Frist
    faelligAm
    wurdeVerlaengert

    verlaengernUm(wochen)
    istVerstrichen()
```

---

## Schritt 1 · Welche Begriffe fehlen in Modell 1?

| Begriff der Bibliothekarin | Modell 1 |
|---|---|
| überzogen | nur errechenbar aus `faelligkeitsDatum` und heute |
| verlängern | als Zähler, nicht als Vorgang |
| vorgemerkt | **fehlt vollständig** |
| Frist | als Datumsfeld |

**Der auffälligste Befund:** „Vorgemerkt" kommt nicht vor, obwohl es eine Regel bestimmt. Die Regel kann Modell 1 gar nicht prüfen — die Information fehlt.

## Schritt 2 · Wo steht die Regel?

**„Einmal verlängerbar, außer vorgemerkt"**

| | |
|---|---|
| Modell 1 | in `AusleiheService`, der `verlaengerungsZaehler` prüft und die Vormerkung woanders herholt |
| Modell 2 | in `verlaengern()` |

**Der Unterschied im Betrieb:** In Modell 1 kann jeder `setVerlaengerungsZaehler(0)` aufrufen und die Regel umgehen. In Modell 2 gibt es keinen Setter.

## Schritt 3 · Welche ungültigen Zustände sind konstruierbar?

In Modell 1:

| Zustand | Fachlich möglich? |
|---|---|
| `rueckgabeDatum` gesetzt, `verlaengerungsZaehler` wird erhöht | nein — zurückgegebene Medien verlängert man nicht |
| `faelligkeitsDatum` vor `ausleihDatum` | nein |
| `verlaengerungsZaehler = 5` | nein — nur eine Verlängerung |

Alle drei sind in Modell 1 anlegbar. In Modell 2 gibt es keinen Weg dorthin.

## Schritt 4 · Der Lesbarkeitstest

Die Bibliothekarin liest Modell 2:

> „Ausleihe, Exemplar, Entleiher, Frist, verlängern, zurückgeben, überzogen."

Sie kann sagen: „Stimmt — aber Vormerkung fehlt bei euch als eigene Sache."

Bei Modell 1 müsste jemand übersetzen: „`verlaengerungsZaehler` ist die Zahl der Verlängerungen." Danach prüft sie die Übersetzung.

---

## Was dieses Beispiel zeigt

**Ein fehlender Begriff macht eine Regel unprüfbar.** „Vorgemerkt" fehlt in Modell 1, also kann die Regel dort nicht stehen — sie muss aus einem anderen System geholt werden.

**Ein Zähler ist selten die richtige Abbildung.** `verlaengerungsZaehler` speichert, wie oft etwas geschah, aber nicht, ob es noch zulässig ist. Das ist eine andere Frage.

**Setter sind Löcher.** Jedes setzbare Feld ist ein Weg, die Regeln zu umgehen. Wo Regeln gelten sollen, gehören sie geschlossen.

**Beide Modelle speichern dieselben Daten.** Der Unterschied liegt darin, welche Fragen sie beantworten und welche Zustände sie zulassen.

---

## Zum Vergleich: wann Modell 1 richtig wäre

Angenommen, es geht um eine **Auswertung** der Ausleihen der letzten zehn Jahre — Häufigkeiten, Fristüberschreitungen, Nutzungsmuster.

Dann sind die Regeln gegenstandslos. Die Daten sind historisch, es wird nichts entschieden, nur gelesen. `AusleiheDatensatz` mit offenen Feldern ist genau richtig.

**Der Unterschied liegt nicht in der Sache, sondern im Zweck.** Ein Modell zum Entscheiden und eines zum Auswerten dürfen verschieden sein — und sind es meistens.
