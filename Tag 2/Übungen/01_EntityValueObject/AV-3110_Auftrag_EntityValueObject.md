# AV-3110 · Werte von Dingen mit Identität unterscheiden

**Typ:** Story
**Komponente:** Fakturierung
**Priorität:** Hoch
**Verweist auf:** AV-3098 (Rechnung an abgemeldete Anschrift, Kundenbeschwerde)

---

## Story

**Als** Sachbearbeiterin in der Abrechnung
**möchte ich**, dass auf einer Rechnung die Anschrift steht, die zum Zeitpunkt der Rechnung galt,
**damit** eine Adressänderung nicht rückwirkend alte Rechnungen verfälscht — und keine Rechnung an eine abgemeldete Anschrift geht.

---

## Description

Die Rechnungsanschrift wurde über die Jahre von fünf auf zwölf Angaben erweitert. Hinzugekommen sind: eine Kennung, Anlagedatum, Änderungsdatum, Bearbeitervermerk, Gültigkeitszeitraum, Unzustellbarkeitsmerkmal und ein Vermerk dazu.

**Vorfall AV-3098:** Eine Rechnung ging an eine Anschrift, die der Kunde vor zwei Jahren abgemeldet hatte. Die Rechnung verweist auf die **Kennung** der Anschrift; beim Erstellen wurde die Kennung aufgelöst, ohne die Gültigkeit zu prüfen.

**Weitere Befunde aus der Nachrecherche:**

| Befund | Anzahl |
|---|---|
| Anschriften mit identischen Werten und verschiedenen Kennungen | 14 |
| Kunden mit der Anschrift eines anderen Kunden verknüpft | 3 |
| Gültigkeitszeiträume, die in der Zukunft beginnen | 80 |

**Kernbefund:** Die Anschrift wird behandelt, als hätte sie eine eigene Geschichte. Der Gegenstand mit Geschichte ist aber die **Zuordnung** — welcher Kunde welche Anschrift wann verwendet —, nicht die Anschrift selbst.

**Nicht Gegenstand:** Die Bereinigung der Bestandsdaten. Es geht um die Modellentscheidung.

## Randbedingungen

- Rund 4.200 gespeicherte Anschriften bei 1.240 Firmenkunden
- Firmenkunden können mehrere Rechnungsanschriften haben, je Landesgesellschaft eine
- Rechnungen müssen zehn Jahre unverändert nachweisbar bleiben
- Eine Dublettenprüfung beim Anlegen ist vorhanden und verhindert neue Doppelte
- Ein Pflegewerkzeug zum Zusammenführen existiert und wurde dreimal benutzt

## Akzeptanzkriterien

- **AK1** – Für die Anschrift ist entschieden und begründet, ob sie eine eigene Identität braucht oder durch ihre Werte bestimmt ist.
- **AK2** – Eine Rechnung zeigt die Anschrift, die zum Zeitpunkt ihrer Erstellung galt. Eine spätere Änderung wirkt nicht zurück.
- **AK3** – Es ist benannt, welcher Gegenstand die Geschichte trägt — die Anschrift oder die Zuordnung zwischen Kunde und Anschrift.
- **AK4** – Zwei Anschriften mit gleichen Werten sind nicht unterscheidbar. Doppelte können nicht entstehen.
- **AK5** – Regeln, die zur Anschrift gehören (etwa: Postleitzahl passt zum Land), sind Teil der Anschrift und nicht auf Aufrufer verteilt.
- **AK6** – Für jede der zwölf heutigen Angaben ist festgestellt, ob sie zur Anschrift gehört oder zu etwas anderem.
- **AK7** – Für die Angaben, die nicht zur Anschrift gehören, ist benannt, wohin sie gehören.
- **AK8** – Das Unzustellbarkeitsmerkmal ist eingeordnet: Eigenschaft der Anschrift, der Zuordnung oder eines Zustellversuchs?

## Hinweise

Eine Dublettenprüfung erfüllt AK4 nicht. Sie verhindert Doppelte durch Kontrolle; gesucht ist ein Modell, in dem sie nicht entstehen können.

AK3 ist der Kern. Solange die Anschrift die Geschichte trägt, sind Gültigkeitszeiträume an ihr — und damit ist sie ein Ding mit Lebenslauf.

AK8 hat keine offensichtliche Antwort. Alle drei Zuordnungen sind vertretbar; die Begründung entscheidet.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Interessiert es, ob es dasselbe ist — oder nur, ob es gleich ist?**

---
---

# Addendum · Woran man Werte von Dingen unterscheidet

## Die eine Frage

> **Interessiert es, ob es dasselbe ist — oder nur, ob es gleich ist?**

| Antwort | Einordnung |
|---|---|
| Es muss **dasselbe** sein | Entity — es hat Identität über die Zeit |
| Es genügt, dass es **gleich** ist | Value Object — es ist durch seine Werte bestimmt |

**Die Probe:** Wenn ich es gegen ein identisches austausche — merkt jemand den Unterschied, und stört es?

- Zwanzig Euro gegen einen anderen Zwanziger: niemand stört sich daran → Wert
- Mein Fahrrad gegen ein baugleiches: stört sehr → Ding mit Identität

## Es hängt vom Kontext ab

Nicht das Ding entscheidet, sondern der Zweck:

| Gegenstand | In einem Kontext | Im anderen |
|---|---|---|
| Geldschein | Betrag (Wert) | Einzelstück mit Seriennummer (Entity) |
| Sitzplatz | Kategorie (Wert) | konkreter Platz mit Reihe und Nummer (Entity) |
| Artikel | Position auf der Rechnung (Wert) | Einzelstück im Lager (Entity) |
| Anschrift | Zieladresse (Wert) | Objekt in der Bestandspflege (Entity) |

## Signale für einen Wert

| Signal | Beispiel |
|---|---|
| Es beschreibt etwas, statt etwas zu sein | Betrag, Zeitraum, Anschrift, Kennzeichen |
| Zwei mit gleichen Werten sind austauschbar | zwei Beträge von 50 Euro |
| Es ändert sich nicht — es wird ersetzt | aus 50 werden nicht 60; es ist ein anderer Betrag |
| Es hat keine sinnvolle Geschichte | „was ist mit diesem Betrag im letzten Jahr passiert" ergibt keinen Sinn |
| Man kann es nicht suchen | „finde mir den Zeitraum" — welchen? |

## Signale für eine Entity

| Signal | Beispiel |
|---|---|
| Es bleibt dasselbe, auch wenn sich alles ändert | ein Fahrzeug mit neuem Kennzeichen und Halter |
| Man kann seine Geschichte erzählen | „dieses Fahrzeug war dreimal in der Werkstatt" |
| Man kann es suchen und verfolgen | „wo ist Fahrzeug X gerade" |
| Es hat einen Lebenszyklus | angelegt, in Betrieb, ausgemustert |

## Die zwei häufigen Fehler

**Alles zur Entity machen.**
Der Reflex kommt daher, dass alles gespeichert werden muss und Speicherung nach Kennungen verlangt. Das ist eine Frage der Ablage, keine des Modells.

**Werte als bloße Zahlen und Zeichenketten führen.**
Ein Betrag ohne Währung, ein Zeitraum als zwei getrennte Daten, ein Kennzeichen als freier Text. Dann gibt es keinen Ort für die Regeln, die dazugehören — und sie stehen bei jedem Aufrufer.

## Wenn ein Wert eine Geschichte zu brauchen scheint

Dann trägt meist nicht der Wert die Geschichte, sondern die **Zuordnung**.

Nicht: „Die Anschrift gilt von–bis."
Sondern: „Dieser Kunde verwendet diese Anschrift von–bis."

Die Zuordnung ist der Gegenstand mit Lebenslauf. Der Wert bleibt ein Wert.
