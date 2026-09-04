# Fallbeispiel · Die Regel, die niemand prüfen konnte

**Situationstyp:** Fachliche Regeln sind so mit Technik verwoben, dass man ein halbes System starten muss, um eine einzige Bedingung zu prüfen.

---

## Ausgangslage

Derselbe Autovermieter. Der Kontext **Anmietung** hat eine Regel, die seit Jahren gilt:

> Ein Mietvertrag darf nur einmal verlängert werden. Zweimal geht nicht — das muss dann eine neue Anmietung sein.

## Wie es gewachsen ist

Die Regel wurde 2016 eingeführt. Sie steht in einer Ablaufsteuerung, die bei einer Verlängerung durchlaufen wird:

1. Vorgang aus der Datenbank holen
2. Prüfen, ob schon verlängert wurde
3. Konditionen vom Vertragssystem abfragen
4. Neuen Zeitraum berechnen
5. Vorgang speichern
6. Bestätigung an den Mieter senden
7. Meldung an die Fakturierung

Die Regel steckt in Schritt 2 — eingebettet zwischen Datenbankzugriff, Fremdsystemabfrage und Versand.

## Der Vorfall

Ein Firmenkunde beschwerte sich, dass eine Verlängerung abgelehnt wurde, obwohl im Rahmenvertrag zwei Verlängerungen vereinbart sind.

Die Prüfung der Regel dauerte **drei Tage** — nicht wegen ihrer Kompliziertheit, sondern weil sie nicht isoliert prüfbar ist.

**Was nötig war, um die Regel einmal auszuführen:**

| Voraussetzung | Warum |
|---|---|
| Datenbank mit einem passenden Vorgang | Schritt 1 |
| Erreichbares Vertragssystem | Schritt 3 |
| Funktionierender Nachrichtenversand | Schritt 6 |
| Erreichbare Fakturierung | Schritt 7 |

**Der Entwickler baute sich einen Testfall.** Dafür brauchte er einen Datenbestand mit einem Vorgang im richtigen Zustand, Zugangsdaten für das Vertragssystem und eine Umgebung, in der keine echten Nachrichten hinausgehen.

**Am dritten Tag** stand fest: Die Regel prüft nur, ob bereits verlängert wurde. Die Sonderregelung aus dem Rahmenvertrag wird nicht berücksichtigt — sie war 2016 noch nicht vereinbart und wurde nie nachgezogen.

**Die Korrektur selbst dauerte zwei Stunden.**

## Was bei der Aufarbeitung auffiel

**Die Regel ist eine Zeile, ihre Umgebung ist ein halbes System.** Um zu prüfen, ob eine fachliche Bedingung stimmt, muss alles laufen, was drumherum steht.

**Es gibt keinen Ort für die Regel.** Sie steht in der Ablaufsteuerung, zwischen technischen Schritten. Wer sie sucht, muss den Ablauf lesen.

**Ähnliche Regeln stehen an anderen Stellen.** Eine Suche ergab: Die Frage „darf verlängert werden" wird an drei Stellen beantwortet — im Ablauf, in der Bedienoberfläche (zum Ausgrauen der Schaltfläche) und in der Partnerschnittstelle. Alle drei Fassungen unterscheiden sich.

**Fachvertreter können die Regel nicht prüfen.** Auf die Frage, ob die Regel richtig umgesetzt sei, gab es keine Antwort — man müsste den Ablauf lesen können.

**Die Ablaufsteuerung ist gewachsen.** 2016 hatte sie vier Schritte, heute sieben. Jeder neue Schritt liegt zwischen der Regel und dem Ergebnis.

## Was bisher versucht wurde

**Eine Testumgebung mit Datenbestand.** Verkürzt die Vorbereitung von drei Tagen auf einen halben. Löst nicht, dass ein halbes System laufen muss.

**Attrappen für die Fremdsysteme.** Wurden für zwei der drei gebaut. Der Nachrichtenversand hat keine.

## Diskussionsfragen

1. Die Regel ist eine Zeile. Warum dauerte ihre Prüfung drei Tage?
2. Warum gibt es drei Fassungen derselben Regel?
3. Was müsste anders sein, damit ein Fachvertreter die Regel prüfen kann?
4. Wo haben Sie so etwas?
