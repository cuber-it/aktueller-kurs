# Fallbeispiel · Das Modell, das die Datenbank abbildete

**Situationstyp:** Die Struktur der Software folgt der Datenhaltung statt der Fachlichkeit — jede fachliche Frage wird zur Abfrage über mehrere Tabellen.

---

## Ausgangslage

Ein Autovermieter mit 140 Stationen. Die Software wird seit 2009 im Haus entwickelt.

Am Anfang stand eine Datenbank. Ein externer Berater entwarf das Schema: 34 Tabellen, normalisiert bis zur dritten Normalform, mit sauberen Fremdschlüsseln. Das Schema war fachlich korrekt und technisch sauber.

Die Anwendung entstand darauf. Für jede Tabelle eine Klasse, für jede Spalte ein Feld, für jeden Fremdschlüssel eine Referenz.

## Wie es gewachsen ist

Das Vorgehen war effizient. Neue Anforderungen bedeuteten: Tabelle ergänzen, Klasse ergänzen, fertig.

Nach fünfzehn Jahren umfasst das Modell 61 Klassen. Jede entspricht einer Tabelle. Klassennamen wie `MietvertragPosition`, `FahrzeugStatusHistorie` und `KundeKontaktZuordnung` beschreiben, wo Daten liegen.

Fachliche Vorgänge sind über mehrere Klassen verteilt. Eine Fahrzeugausgabe berührt sieben davon.

## Der Vorfall

Die Fachabteilung meldete einen Fehler: Bei Verlängerungen wurde in bestimmten Fällen der falsche Tagessatz berechnet.

Die Analyse dauerte elf Tage. Der Grund lag nicht in der Berechnung — die war korrekt. Der Grund lag darin, dass **niemand sagen konnte, wo eine Verlängerung im Code stattfindet.**

Sie besteht aus:

- einem neuen Satz in `MietvertragPosition`
- einer Änderung in `MietvertragKopf`
- einem Eintrag in `PreisHistorie`
- einer Statusänderung in `FahrzeugStatusHistorie`
- einer Neuberechnung in `AbrechnungVorschau`

**Der Begriff „Verlängerung" kommt im Code nicht vor.** Er existiert im Fachbereich, in der Bedienoberfläche und in den Anforderungen — nicht im Modell.

Bei der Suche stellte sich heraus, dass es **drei Stellen** gibt, an denen eine Verlängerung durchgeführt wird: über die Bedienoberfläche, über die Partnerschnittstelle und über einen Nachtlauf für automatische Verlängerungen. Die drei taten fachlich Verschiedenes, ohne dass das jemandem aufgefallen war.

**Die Korrektur betraf zwei der drei Stellen.** Die dritte wurde übersehen und fiel vier Monate später auf.

## Was bei der Aufarbeitung auffiel

**Fachliche Fragen sind nur über Abfragen zu beantworten.** „Ist dieser Vorgang abgeschlossen?" ergibt sich aus dem Zusammenspiel von vier Feldern in drei Tabellen. Die Regel dafür steht an sechs Stellen im Code, in vier Varianten.

**Das Modell kennt keine Regeln, nur Daten.** Ob eine Verlängerung zulässig ist, entscheidet Code außerhalb der Klassen. Die Klassen haben Getter und Setter.

**Die Sprache des Fachbereichs kommt im Code nicht vor.** Ein Entwickler, der die Anforderung „Verlängerung darf nur einmal erfolgen" umsetzen soll, findet keinen Ort dafür.

**Neue Entwickler brauchen lange.** Sie lernen zuerst das Datenmodell und danach, welcher fachliche Vorgang aus welchen Tabellen besteht. Das steht nirgends.

## Was bisher versucht wurde

**Ein Datenmodell-Diagramm.** Wurde erstellt, hängt aus, ist aktuell. Es zeigt 61 Tabellen mit ihren Beziehungen und beantwortet keine fachliche Frage.

**Eine Namenskonvention.** Klassen sollten sprechender benannt werden. Nach der Umbenennung von `MVP` zu `MietvertragPosition` war es lesbarer, aber nicht fachlicher.

## Diskussionsfragen

1. Das Datenbankschema war fachlich korrekt. Warum ist das Modell trotzdem unbrauchbar?
2. Warum hat die Umbenennung nichts gebracht?
3. Was müsste anders sein, damit die Frage „wo findet eine Verlängerung statt" beantwortbar ist?
4. Wo haben Sie so etwas?
