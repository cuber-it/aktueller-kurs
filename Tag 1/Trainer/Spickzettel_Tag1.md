# Spickzettel Tag 1

Eine Seite für den Trainer. Alles, was während der Durchführung griffbereit sein sollte.

---

## Die Prüffragen des Tages

Sie bauen aufeinander auf. Nebeneinander gelesen zeigen sie den roten Faden.

| Einheit | Prüffrage |
|---|---|
| **1-2** Modell | Kann ein Fachvertreter dieses Modell lesen und sagen, ob es stimmt? |
| **1-3** Sprache | Führt die Zusammenführung zu einem **Widerspruch** oder nur zu **mehr Feldern**? |
| **1-4** Glossar | Lässt sich jeder Eintrag eindeutig formulieren — ohne „je nach Kontext"? |
| **1-5** Kontext | Würde eine Änderung an dieser Aufgabe auch die **übrigen** Aufgaben betreffen? |
| **1-6** Subdomain | Wäre ein Wettbewerber mit gleicher Fähigkeit gefährlich — und **können es alle**? |
| **1-7** Beziehung | Wer muss **nachziehen**, und wie viel **Einfluss** hat er darauf? |

---

## Widerspruch oder Vereinigungsmenge

Der wichtigste Prüfstein des Tages. Kommt in 1-3, 1-4 und 1-5 vor.

| | Widerspruch | Vereinigungsmenge |
|---|---|---|
| Beispiel | ein Konzern ist 1 und ist 340 | einer braucht 5 Felder, einer 20 |
| Bedeutet | **Kontextgrenze** | dieselbe Sache, zwei Sichten |
| Konsequenz | trennen | **nicht** trennen |

Ohne diesen Prüfstein trennt die Gruppe zu viel.

---

## Die acht Beziehungsmuster

| Muster | Erkennungszeichen | Wer zieht nach |
|---|---|---|
| **Customer / Supplier** | „Wenn wir was brauchen, reden die mit uns" | Abnehmer, mit Vorlauf |
| **Conformist** | „Auf deren Format haben wir null Einfluss" | Abnehmer, vollständig |
| **Anticorruption Layer** | kein Einfluss, aber Übersetzung an der Grenze | nur die Übersetzung |
| **Open Host Service** | Lieferant bedient viele über eine Schnittstelle | Abnehmer |
| **Published Language** | öffentliche Spezifikation, Gremium | alle, koordiniert |
| **Shared Kernel** | „Wir arbeiten mit denselben Daten" | **beide, sofort** |
| **Partnership** | gemeinsame Planung und Releases | beide, koordiniert |
| **Separate Ways** | keine Verbindung — eine Entscheidung | niemand |

**Herleitung statt Auswendiglernen:**

1. Gegenseitig? → Shared Kernel / Partnership
2. Einfluss durch Absprache? → Customer/Supplier
3. Kein Einfluss, keine Übersetzung? → Conformist
4. Kein Einfluss, mit Übersetzung? → Anticorruption Layer

---

## Was kein Kriterium ist (Subdomains)

Jeder Punkt kommt in der Übung als Begründungsversuch vor:

| Scheinkriterium | Entgegnung |
|---|---|
| Umsatzanteil | die Buchhaltung verarbeitet 100 % des Umsatzes |
| Datenmenge | sagt nichts über Bedeutung |
| Bisheriger Aufwand | zirkulär |
| Nutzerzahl | die Zeiterfassung nutzen alle |
| Kompliziertheit | Kompliziertheit ist kein Wert |
| Gefühlte Wichtigkeit | jede Abteilung hält ihres für zentral |

---

## Die Warnzeichen im Code (1-2)

Sofort im eigenen Code auffindbar — der Teil, den Teilnehmer behalten:

- **Wahrheitswert für einen fachlichen Sachverhalt** — `fahrerlaubnisGeprueft` sagt nicht, ob das Ergebnis positiv war
- **Zahlencode für einen Zustand** — `statusCode = 2` bedeutet etwas, das nirgends steht
- **Technische Begriffe in Klassennamen** — `Kopf`, `Position`, `Historie`, `Zuordnung`
- **Klassen namens `…Service`, `…Manager`** — die Regeln liegen außerhalb
- **Setter für Zustände** — jede Regel ist umgehbar

---

## Problemraum und Lösungsraum

Wird dreimal gebraucht: 1-1, 1-5, 1-6.

| | Problemraum | Lösungsraum |
|---|---|---|
| Einheit | **Subdomain** | **Bounded Context** |
| Beschreibt | was das Unternehmen tut | wie die Software geschnitten ist |
| Bestimmt durch | das Geschäft | den Entwurf |

**Bild:** Der Problemraum ist die Landschaft, der Lösungsraum die Landkarte.

**Sie fallen nicht notwendig zusammen.** Deckungsgleichheit ist wünschenswert, nicht erzwingbar.

---

## Sätze, die im Kurs tragen

> Ein Modell ist eine **Auswahl**, kein Abbild.

> Wichtig und unterscheidend sind **zweierlei**.

> Ein Glossar ist nur **innerhalb** eines Kontextes möglich.

> Conformist ist eine **Wahl**, kein Versäumnis.

> Ein Kontext meldet, **wer es braucht, holt es sich**.

> Wenn ein Sonderfall einen ganzen Bereich in die Eigenentwicklung zieht, ist die **Grenze falsch gezogen**.

---

## Wenn Zeit übrig ist

In dieser Reihenfolge:

1. Diskussionsfragen aus dem ProContra-Papier (5 je Paket, ohne richtige Antwort)
2. „Wo haben Sie so etwas?" nach jedem Fallbeispiel
3. Der Preis-Abschnitt im ProContra
4. Das Beispiel-Dokument mitlesen
5. Die Ärgernisse aus 1-1 aufgreifen

---

## Wenn Zeit fehlt

Streichbar: 1-4 Übung · 1-2 Aufgaben 5–9 · 1-6 auf fünf Bereiche kürzen

**Nicht streichen:** 1-3 und 1-5 — sie tragen auch Tag 2.
