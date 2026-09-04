# Übung · Was ist fachlich, was ist Ablauf?

Sie zerlegen vier Abläufe und ordnen jeden Schritt zu.

**Es wird kein Code geschrieben.**

---

## Material A · Die Ablaufsteuerung „Verlängerung"

| # | Schritt |
|---|---|
| 1 | Vorgang aus der Datenbank holen |
| 2 | Prüfen, ob schon verlängert wurde |
| 3 | Konditionen vom Vertragssystem abfragen |
| 4 | Neuen Zeitraum berechnen |
| 5 | Vorgang speichern |
| 6 | Bestätigung an den Mieter senden |
| 7 | Meldung an die Fakturierung |

## Material B · Die Ablaufsteuerung „Rückgabe"

| # | Schritt |
|---|---|
| 1 | Vorgang holen |
| 2 | Kilometerstand entgegennehmen |
| 3 | Prüfen, ob der Kilometerstand plausibel ist (nicht kleiner als bei Ausgabe) |
| 4 | Fahrzeugzustand erfassen |
| 5 | Entscheiden, ob ein Schaden vorliegt |
| 6 | Prüfen, ob Freikilometer überschritten sind |
| 7 | Vorgang auf „zurückgenommen" setzen |
| 8 | Fahrzeug in der Flotte als verfügbar melden |
| 9 | Vorgang speichern |
| 10 | Meldung erzeugen |

## Material C · Weitere Bausteine im System

| Baustein | Was er tut |
|---|---|
| `VorgangZugang` | holt und speichert Mietvorgänge |
| `KonditionenAbfrage` | fragt beim Vertragssystem an |
| `Preisrechner` | berechnet den Mietpreis aus Zeitraum, Kategorie und Konditionen |
| `Nachrichtenversand` | verschickt E-Mails und Kurznachrichten |
| `VorgangErzeuger` | legt neue Mietvorgänge an |
| `SchadensBewertung` | entscheidet, ob ein Befund ein Schaden ist |
| `MeldungsVersand` | veröffentlicht Meldungen |

## Material D · Aussagen aus dem Fachbereich

**Zur Verlängerung:** „Ob verlängert werden darf, hängt vom Rahmenvertrag ab. Standard ist einmal, manche Firmenkunden haben zwei."

**Zum Kilometerstand:** „Wenn der Stand kleiner ist als bei der Ausgabe, hat sich jemand vertippt. Das prüfe ich immer."

**Zum Schaden:** „Ob eine Schramme ein Schaden ist oder normale Abnutzung, entscheidet die Werkstatt nach einer Tabelle. Kratzer unter fünf Zentimetern zählen nicht."

**Zu den Freikilometern:** „Was drüber ist, wird berechnet. Der Satz steht im Rahmenvertrag."

---

## Aufgabe

### Teil 1 · Zuordnen

**1.** Ordnen Sie jeden Schritt aus Material A und B zu:

- **fachlich** — eine Regel oder Entscheidung, die der Fachbereich kennt
- **Ablauf** — holen, speichern, senden, melden
- **beides vermischt** — der Schritt enthält Fachliches und Technisches

**2.** Welche Schritte fallen in die dritte Kategorie? Wie würden Sie sie trennen?

### Teil 2 · Die Regel finden

**3.** Nehmen Sie Schritt A2 („Prüfen, ob schon verlängert wurde"). Nach Material D ist die Regel komplizierter als der Schritt vermuten lässt. Formulieren Sie die Regel vollständig.

**4.** Wo gehört diese Regel hin — zum Vorgang, zum Rahmenvertrag, oder in einen eigenen Baustein? Begründen Sie.

**5.** Die Frage „darf verlängert werden" wird an drei Stellen beantwortet: im Ablauf, in der Bedienoberfläche und in der Partnerschnittstelle. Wie stellen Sie sicher, dass es künftig eine Antwort gibt — und wie kommt die Bedienoberfläche an sie heran?

### Teil 3 · Die Bausteine einordnen

**6.** Ordnen Sie die sieben Bausteine aus Material C ein:

- **Zugang** — holt und speichert
- **Erzeuger** — bringt Neues hervor
- **Fachlogik** — enthält Regeln
- **Ablaufsteuerung** — koordiniert
- **Technik** — verschickt, überträgt

**7.** Bei welchem Baustein waren Sie unsicher? Woran lag es?

**8.** `Preisrechner` und `SchadensBewertung` enthalten beide Regeln. Gehören sie zu einem Gegenstand oder stehen sie daneben? Begründen Sie je Baustein.

### Teil 4 · Die Folgen

**9.** Prüfen Sie Ihren Vorschlag: Welche Voraussetzungen braucht es jetzt, um die Regel „darf verlängert werden" einmal auszuführen?

**10.** Ein Fachvertreter soll prüfen, ob die Schadensregel richtig umgesetzt ist. Was zeigen Sie ihm?

**11.** Was ist der Preis Ihres Vorschlags? Nennen Sie mindestens zwei Nachteile.

---

## Hinweise zur Bearbeitung

- Der Prüfstein für „fachlich": **Würde der Fachbereich diese Regel kennen?**
- Bei Aufgabe 2 sind mehrere Schritte betroffen. Suchen Sie nach Schritten, die eine Entscheidung **und** einen Zugriff enthalten.
- Bei Aufgabe 8 gibt es keine eindeutige Antwort. Die Begründung zählt.
