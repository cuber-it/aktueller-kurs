# Lösungsvorschlag · Was ist fachlich, was ist Ablauf?

---

## 1 · Die Zuordnung

### Ablauf „Verlängerung"

| # | Schritt | Einordnung |
|---|---|---|
| 1 | Vorgang aus der Datenbank holen | **Ablauf** |
| 2 | Prüfen, ob schon verlängert wurde | **beides vermischt** |
| 3 | Konditionen vom Vertragssystem abfragen | **Ablauf** |
| 4 | Neuen Zeitraum berechnen | **fachlich** |
| 5 | Vorgang speichern | **Ablauf** |
| 6 | Bestätigung an den Mieter senden | **Ablauf** |
| 7 | Meldung an die Fakturierung | **Ablauf** |

### Ablauf „Rückgabe"

| # | Schritt | Einordnung |
|---|---|---|
| 1 | Vorgang holen | **Ablauf** |
| 2 | Kilometerstand entgegennehmen | **Ablauf** |
| 3 | Plausibilität des Kilometerstands prüfen | **fachlich** |
| 4 | Fahrzeugzustand erfassen | **Ablauf** |
| 5 | Entscheiden, ob ein Schaden vorliegt | **fachlich** |
| 6 | Prüfen, ob Freikilometer überschritten sind | **beides vermischt** |
| 7 | Vorgang auf „zurückgenommen" setzen | **fachlich** |
| 8 | Fahrzeug als verfügbar melden | **Ablauf** |
| 9 | Vorgang speichern | **Ablauf** |
| 10 | Meldung erzeugen | **Ablauf** |

**Vier fachliche Schritte in siebzehn.** Das ist das übliche Verhältnis — und der Grund, warum die Fachlichkeit in der Technik verschwindet.

---

## 2 · Die vermischten Schritte

### A2 · „Prüfen, ob schon verlängert wurde"

**Was daran vermischt ist:** Die Prüfung braucht eine Angabe aus dem Rahmenvertrag (wie viele Verlängerungen erlaubt sind) — die muss geholt werden. Das Holen ist Ablauf, die Prüfung ist fachlich.

**Die Trennung:**

| Teil | Wohin |
|---|---|
| Zulässige Verlängerungszahl beschaffen | Ablauf, vor der Prüfung |
| Vergleich mit der bisherigen Zahl | fachlich, beim Vorgang |

**In der Reihenfolge bedeutet das:** Schritt 3 (Konditionen abfragen) muss **vor** Schritt 2 stehen. Die heutige Reihenfolge ist der Grund, warum die Sonderregelung nie berücksichtigt wurde — zum Zeitpunkt der Prüfung war sie noch nicht da.

**Das ist der eigentliche Fund der Übung:** Der Fehler aus AV-3594 steckt in der Schrittreihenfolge, nicht in der Regel.

### B6 · „Prüfen, ob Freikilometer überschritten sind"

**Vermischt:** Die Freikilometer stehen im Rahmenvertrag. Das Holen ist Ablauf, der Vergleich fachlich.

**Die Trennung:** Freikilometer als Angabe beschaffen (Ablauf), dann vergleichen (fachlich, beim Vorgang oder beim Zeitraum).

---

## 3 · Die vollständige Regel

Aus Material D: „Ob verlängert werden darf, hängt vom Rahmenvertrag ab. Standard ist einmal, manche Firmenkunden haben zwei."

**Vollständig formuliert:**

> Ein Mietvorgang darf verlängert werden, wenn die Zahl der bisherigen Verlängerungen kleiner ist als die im Rahmenvertrag vereinbarte Höchstzahl. Ist kein Rahmenvertrag vorhanden oder keine Zahl vereinbart, gilt eins.

**Was der ursprüngliche Schritt nicht abbildete:**

| Aspekt | Im Schritt | Vollständig |
|---|---|---|
| Höchstzahl | fest auf 1 | aus dem Rahmenvertrag |
| Kein Rahmenvertrag | nicht bedacht | Standardwert 1 |
| Vereinbart, aber ohne Zahl | nicht bedacht | Standardwert 1 |

---

## 4 · Wo die Regel hingehört

**Zum Vorgang.**

**Begründung:** Die Regel betrifft einen einzelnen Vorgang und dessen Zustand („wie oft wurde bereits verlängert"). Sie braucht eine Angabe von außen (die Höchstzahl), aber die Entscheidung selbst trifft der Vorgang.

**Die Form:** Der Vorgang bekommt eine Methode, die die Höchstzahl als Parameter entgegennimmt und antwortet.

> „Darf ich bei einer Höchstzahl von N verlängert werden?"

**Warum nicht zum Rahmenvertrag:** Der Rahmenvertrag weiß nichts über den einzelnen Vorgang. Er liefert eine Zahl, mehr nicht.

**Warum nicht in einen eigenen Baustein:** Ein eigener Baustein wäre gerechtfertigt, wenn die Regel mehrere Gegenstände bräuchte. Hier braucht sie einen Vorgang und eine Zahl — das reicht für eine Methode am Vorgang.

**Der Prüfstein aus dem Denkmodell:** Fachlogik gehört in einen eigenen Baustein, wenn sie zu **keinem** Gegenstand gehört. Diese hier gehört eindeutig zum Vorgang.

---

## 5 · Eine Antwort statt drei

**Der Kern:** Die Bedienoberfläche und die Partnerschnittstelle brauchen dieselbe Antwort wie der Ablauf — sie stellen die Frage nur früher.

**Der Vorschlag:**

| Wer fragt | Wozu | Wie |
|---|---|---|
| Bedienoberfläche | Schaltfläche ausgrauen | fragt den Vorgang: „Darf verlängert werden?" |
| Partnerschnittstelle | Anfrage annehmen oder ablehnen | dieselbe Frage |
| Ablaufsteuerung | vor der Durchführung | dieselbe Frage, dann durchführen |

**Alle drei rufen dieselbe Methode auf.** Sie liefert nicht nur ja/nein, sondern eine Begründung — damit die Oberfläche einen Hinweis anzeigen kann.

**Zweistufig:**

| Schritt | Zweck |
|---|---|
| Frage: darf verlängert werden? | für Anzeige und Vorabprüfung |
| Durchführung: verlängere bis Datum X | prüft erneut und verweigert bei Verstoß |

**Warum zweimal geprüft wird:** Zwischen Anzeige und Durchführung können Minuten liegen. Die Anzeige ist eine Auskunft, die Durchführung eine Zusicherung.

---

## 6 · Die Bausteine

| Baustein | Einordnung | Begründung |
|---|---|---|
| `VorgangZugang` | **Zugang** | holt und speichert Vorgänge |
| `KonditionenAbfrage` | **Technik** | fragt bei einem Fremdsystem an |
| `Preisrechner` | **Fachlogik** | siehe Aufgabe 8 |
| `Nachrichtenversand` | **Technik** | verschickt |
| `VorgangErzeuger` | **Erzeuger** | legt neue Vorgänge an |
| `SchadensBewertung` | **Fachlogik** | siehe Aufgabe 8 |
| `MeldungsVersand` | **Technik** | veröffentlicht |

**Keine Ablaufsteuerung in der Liste.** Sie fehlt — die sieben Bausteine sind alle Zugriff, Erzeugung, Fachlogik oder Technik. Die Ablaufsteuerung ist der Ablauf selbst, der sie zusammenruft.

---

## 7 · Der unsichere Fall

**`KonditionenAbfrage`.**

Sie fragt bei einem Fremdsystem an — das ist Technik. Aber sie liefert eine fachliche Angabe (Konditionen), und man könnte argumentieren, sie sei eine Art Zugang.

**Was den Ausschlag gibt:** Ein Zugang liefert Gegenstände des eigenen Modells. Die `KonditionenAbfrage` liefert Angaben aus einem fremden Modell — sie ist die Grenze nach außen.

**Konsequenz:** Sie sollte übersetzen. Was aus dem Vertragssystem kommt, kommt in dessen Begriffen; was die Anmietung bekommt, sollte in ihren Begriffen sein. Das ist die Aufgabe eines Anticorruption Layer — das Thema von morgen.

---

## 8 · Preisrechner und Schadensbewertung

### `Preisrechner`

**Gehört er zu einem Gegenstand?**

Er braucht Zeitraum, Kategorie und Konditionen — drei Dinge aus verschiedenen Quellen. Keines davon ist „der" Gegenstand der Berechnung.

**Einordnung: eigener Baustein.** Das ist der klassische Fall für Fachlogik, die zu keinem einzelnen Gegenstand gehört.

**Gegenprobe:** Könnte der Zeitraum den Preis berechnen? Er kennt die Kategorie nicht. Könnte der Vorgang es? Er müsste die Konditionen kennen — die kommen von außen. Ein eigener Baustein ist richtig.

### `SchadensBewertung`

**Gehört sie zu einem Gegenstand?**

Aus Material D: „Ob eine Schramme ein Schaden ist, entscheidet die Werkstatt nach einer Tabelle. Kratzer unter fünf Zentimetern zählen nicht."

Die Regel braucht einen Befund (Art, Größe) und eine Tabelle. Der Befund ist ein Gegenstand, die Tabelle eine Angabe.

**Zwei vertretbare Antworten:**

| Antwort | Begründung |
|---|---|
| **Beim Befund** | Der Befund kennt seine Merkmale und kann sich selbst bewerten, wenn er die Tabelle bekommt |
| **Eigener Baustein** | Die Bewertungstabelle ist eine eigene Fachlichkeit, die sich unabhängig ändert |

**Der Vorschlag wählt den eigenen Baustein**, weil die Tabelle fachlich eigenständig ist: Sie wird von der Werkstatt gepflegt, ändert sich unabhängig vom Befund und gilt für alle Befunde gleichermaßen.

**Aber:** Wer sie beim Befund ansiedelt, hat ebenfalls recht — solange die Tabelle als Angabe hereingereicht wird und nicht als Abhängigkeit fest verdrahtet ist.

---

## 9 · Voraussetzungen für die Regelprüfung

**Nach dem Vorschlag:**

| Voraussetzung | Nötig? |
|---|---|
| Datenbank | **nein** — ein Vorgang wird direkt erzeugt |
| Vertragssystem | **nein** — die Höchstzahl wird als Zahl übergeben |
| Nachrichtenversand | **nein** |
| Fakturierung | **nein** |

**Die Prüfung besteht aus:** einen Vorgang mit einer bestimmten Zahl bisheriger Verlängerungen erzeugen, die Frage stellen, die Antwort ansehen.

**Aus drei Tagen werden Minuten.**

**Der Vergleich mit AV-3594:** Der Entwickler brauchte drei Tage, um die Regel einmal auszuführen. Die Korrektur dauerte zwei Stunden. Nach dem Vorschlag wäre das Verhältnis umgekehrt.

---

## 10 · Was man dem Fachvertreter zeigt

**Die Schadensbewertung als eigener Baustein** hat eine Methode:

> „Ist dieser Befund ein Schaden?"

**Was man zeigen kann:**

| Was | Wie |
|---|---|
| Eine Liste von Befunden mit Bewertung | Kratzer 3 cm → kein Schaden. Kratzer 8 cm → Schaden |
| Die Grenzfälle | genau 5 cm — was gilt? |
| Die Tabelle selbst | in lesbarer Form, nicht im Code |

**Der Fachvertreter kann sagen:** „Stimmt" oder „Nein, bei Glasschäden gilt die Grenze nicht."

**Was man ihm nicht zeigen kann:** die Ablaufsteuerung. Sie ist technisch und für ihn ohne Aussage.

**Das ist der Prüfstein aus AK6:** Wenn die fachlichen Bausteine benannt sind und für sich stehen, kann ein Fachvertreter sie prüfen. Steckt die Regel im Ablauf, kann er es nicht.

---

## 11 · Der Preis

**Erstens: Mehr Bausteine.**
Aus einer Ablaufsteuerung mit sieben Schritten werden eine Ablaufsteuerung, zwei bis drei Fachbausteine und die vorhandenen Zugänge. Wer nur den Ablauf lesen will, muss jetzt mehr Stellen ansehen.

**Zweitens: Die Übergabe von Angaben wird sichtbar.**
Die Höchstzahl aus dem Rahmenvertrag muss geholt und übergeben werden. Vorher stand die Abfrage einfach im Ablauf. Jetzt ist die Abhängigkeit sichtbar — was gut ist und mehr Schreibarbeit bedeutet.

**Drittens: Die Reihenfolge muss stimmen.**
Der Fund aus Aufgabe 2 — Konditionen vor Prüfung — ist keine automatische Folge der Trennung. Wer trennt, aber die Reihenfolge belässt, hat denselben Fehler.

**Viertens: Bei einfachen Abläufen ist es Überbau.**
Eine Ablaufsteuerung mit drei technischen Schritten und keiner Regel braucht keine Trennung.

**Fünftens: Die Umstellung betrifft vier Abläufe.**
Verlängerung, Ausgabe, Rückgabe, Stornierung. AK9 verlangt Übertragbarkeit — das ist vierfacher Aufwand.

---

## Diskussionsanschluss

Der Fund aus Aufgabe 2 — Konditionen abfragen vor der Prüfung — hätte den Vorfall verhindert. Er hat mit der Trennung von Fachlichkeit und Ablauf nur mittelbar zu tun. Was sagt das über die Fehlerursache?
