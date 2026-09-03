# AV-2104 · Modelle an ihrem Zweck ausrichten

**Typ:** Story
**Komponente:** Fachliche Architektur
**Priorität:** Hoch
**Verweist auf:** AV-2091 (Auswertung „Ausmusterungskandidaten", nach 11 Wochen geliefert, wird nicht genutzt)

---

## Story

**Als** Leiterin der Werkstattdisposition
**möchte ich**, dass das System die Fragen beantworten kann, die ich täglich entscheide,
**damit** ich nicht aus dem Kopf arbeiten muss, während 61 Merkmale je Fahrzeug gespeichert werden.

---

## Description

Der Fahrzeugbegriff im System umfasst **61 Merkmale**. Bei einem beliebigen Fahrzeug sind im Mittel **19** gefüllt.

**Vorfall AV-2091:** Die Werkstattdisposition beantragte eine Auswertung „Welche Fahrzeuge sollten wir ausmustern statt weiter zu reparieren?". Die Lieferung dauerte elf Wochen und wird nicht genutzt.

**Die Analyse ergab, dass das Modell die Frage nicht beantworten kann**, obwohl alle Daten vorhanden sind:

| Was fehlt | Warum es fehlt |
|---|---|
| Bezug zwischen Reparaturen | sie sind Einzelvorgänge mit Datum und Betrag; dass drei dasselbe Bauteil betrafen, steht nirgends |
| Ein Zustand „grenzwertig" | es gibt nur verfügbar, vermietet, in Werkstatt |
| Der Begriff „lohnt nicht mehr" | eine Bewertung — Bewertungen kommen im Modell nicht vor |

**Die Fachvertreterin entscheidet dies täglich.** Sie sagt: „Bei manchen sehe ich nach dem dritten Getriebeschaden, dass sich Reparieren nicht mehr lohnt."

**Befund zur Entstehung:** Das Modell wurde 2009 aus einer Bestandserhebung gebaut — erhoben wurde, welche Daten geführt werden, nicht welche Entscheidungen zu treffen sind. Ein Zweck wurde nie benannt; der Auftrag lautete „Fahrzeuge und Vermietungen verwalten".

**Nicht Gegenstand:** Ein Umbau des Gesamtsystems. Es geht um Erhebung und einen Vorschlag für den Bereich Werkstattdisposition.

## Randbedingungen

- 8.400 Fahrzeuge, 61 Merkmale je Fahrzeug
- Ein Feld „Ausmusterungsempfehlung" wurde nachträglich angelegt; bei 40 Fahrzeugen gefüllt
- Eine Auswertungsdatenbank spiegelt alle Daten; die Frage bleibt unbeantwortbar
- Die Fachvertreterin ist verfügbar und auskunftsbereit
- Vier weitere Bereiche nutzen denselben Fahrzeugbegriff

## Akzeptanzkriterien

- **AK1** – Für den Bereich Werkstattdisposition ist ein Zweck in **einem Satz** formuliert, der ein fachliches Ergebnis nennt.
- **AK2** – Es ist erhoben, welche Entscheidungen in diesem Bereich getroffen werden und welche Angaben sie erfordern.
- **AK3** – Für jede erhobene Entscheidung ist festgestellt, ob das heutige Modell sie stützt.
- **AK4** – Begriffe, die die Fachvertreterin verwendet und die im Modell fehlen, sind benannt.
- **AK5** – Fachliche Regeln sind als Teil des Modells erfasst, nicht als Zusatz.
- **AK6** – Für jedes Merkmal des heutigen Fahrzeugbegriffs ist angegeben, für welchen Zweck es gebraucht wird. Merkmale ohne Zweck sind ausgewiesen.
- **AK7** – Es ist begründet, ob ein eigenes Modell für die Werkstattdisposition sinnvoll ist oder das gemeinsame ausreicht.
- **AK8** – Für die Aussage „manche Fahrzeuge werden härter rangenommen" ist geklärt, ob sie modellierbar ist und woran sie sich festmacht.

## Hinweise

Weitere Merkmale zu ergänzen erfüllt AK3 nicht. Das Feld „Ausmusterungsempfehlung" ist der Beleg: Ein Feld ohne fachliche Herleitung wird nicht gepflegt.

Eine Auswertungsdatenbank erfüllt AK3 ebenfalls nicht. Wenn die Information nicht im Modell steckt, ist sie auch nicht abfragbar — nur schneller nicht abfragbar.

AK6 wird unbequem: Bei 61 Merkmalen ist damit zu rechnen, dass einige keinen Zweck mehr haben.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Wozu ist dieses Modell da — und beantwortet es die Fragen, die dazu gehören?**

---
---

# Addendum · Woran erkennt man ein Modell ohne Zweck

## Im Gespräch mit dem Fachbereich

| Signal | Beispiel |
|---|---|
| Eine tägliche Entscheidung ist im System nicht abbildbar | „Das mache ich aus dem Kopf" |
| Der Fachbereich verwendet Begriffe, die im System fehlen | „grenzwertig", „lohnt nicht mehr" |
| Eine Auswertung wird geliefert und nicht benutzt | sie beantwortet eine andere Frage |
| „Alle Daten sind doch da" | Daten sind nicht dasselbe wie Modell |
| Der Auftrag lautete „X verwalten" | eine Zuständigkeit, kein Zweck |

## Im System

| Signal | Konkret |
|---|---|
| Viele Merkmale, wenige gefüllt | 61 gespeichert, 19 belegt |
| Merkmale, die niemand mehr braucht | „Innenraumfarbe" |
| Vorgänge ohne Bezug zueinander | drei Reparaturen am selben Bauteil sind drei unabhängige Einträge |
| Zustände, die nur technische Abläufe abbilden | verfügbar, vermietet, in Werkstatt — aber nicht „grenzwertig" |
| Nachträglich angelegte Bewertungsfelder | werden nicht gepflegt, weil ihre Herleitung fehlt |
| Eine Auswertungsdatenbank als Antwort auf fachliche Lücken | verlagert das Problem |

## Die drei Fragen, mit denen ein Modell entsteht

Nicht: „Welche Daten haben Sie?"

Sondern:

1. **Welche Entscheidungen treffen Sie?**
2. **Woran machen Sie sie fest?**
3. **Was passiert, wenn Sie falsch entscheiden?**

Die dritte Frage deckt Regeln auf, die niemand für erwähnenswert hält, weil sie selbstverständlich sind.

## Warum „vollständig" kein Ziel ist

Ein Modell mit 61 Merkmalen wirkt gründlich. Es ist aber nicht mehr wert als eines mit acht, wenn die acht die Fragen beantworten und die 61 nicht.

**Was weggelassen wird, ist eine Entscheidung.** In beiden Gesprächen der Übung ist der aufschlussreichste Satz der, der mit „Was mich nicht interessiert …" beginnt.

## Wann ein Modell falsch ist

Ein Modell ist nicht wahr oder unwahr, sondern **brauchbar oder unbrauchbar für seinen Zweck**.

Es ist falsch, wenn:

- es die Fragen seines Zwecks nicht beantwortet
- es Begriffe führt, die im Fachbereich nicht vorkommen
- es Begriffe des Fachbereichs nicht kennt, die Entscheidungen tragen
- es mehrere Zwecke bedienen soll und für jeden schlechter geworden ist

Der letzte Punkt führt zur Frage nach Modellgrenzen.
