# Lösungsvorschlag · Ding oder Wert?

**Vorbemerkung:** Ein Vorschlag. Bei mehreren Gegenständen sind beide Einordnungen vertretbar — bewertet wird die Begründung.

---

## 1 · Die Einordnung

| # | Gegenstand | Einordnung | Begründung |
|---|---|---|---|
| 1 | Fahrzeug | **Ding** | Bleibt dasselbe trotz neuem Kennzeichen und Lack — die Fahrgestellnummer trägt es |
| 2 | Fahrzeugkategorie | **Wert** | „Kompakt" ist „Kompakt"; welche Kategorie-Instanz gemeint ist, fragt niemand |
| 3 | Mietzeitraum | **Wert** | Zwei Zeiträume mit gleichen Grenzen sind derselbe Zeitraum |
| 4 | Kaution | **Wert** | Zweihundert Euro sind zweihundert Euro |
| 5 | Mietvorgang | **Ding** | Hat einen Verlauf: reserviert, laufend, abgeschlossen |
| 6 | Kilometerstand | **Wert** | 41.230 km ist eine Angabe, kein Gegenstand |
| 7 | Station | **Ding** | München-Ost bleibt München-Ost, auch nach Umbau und Umzug |
| 8 | Rechnungsanschrift | **Wert** | siehe Teil 3 — der Kern der Übung |
| 9 | Schadensbefund | **Ding** | Wird verfolgt, bewertet, an die Versicherung gemeldet |
| 10 | Rahmenvertrag | **Ding** | Nummer, Laufzeit, Nachträge — wird über Jahre verfolgt |
| 11 | Fahrerlaubnisklasse | **Wert** | „B" ist „B"; es gibt kein einzelnes B, das man suchen könnte |
| 12 | Prüfbericht | **Ding** | „Gehört zu genau diesem Termin an diesem Fahrzeug", Jahre später auffindbar |

**Fünf Dinge, sieben Werte.** Das Verhältnis ist typisch — in den meisten Modellen überwiegen die Werte, obwohl in der Praxis fast alles als Ding modelliert wird.

---

## 2 · Die uneindeutigen Fälle

### Kaution (4)

Als **Wert** eingeordnet: Der Betrag zählt.

**Gegenargument:** Eine Kaution wird gesperrt, teilweise verrechnet, freigegeben. Das klingt nach Verlauf.

**Auflösung:** Nicht die Kaution hat den Verlauf, sondern die **Kautionssperrung**. Der Betrag ist ein Wert; die Sperrung ist der Vorgang mit Zustand. Dasselbe Muster wie bei der Anschrift.

### Schadensbefund (9)

Als **Ding** eingeordnet, weil er bewertet und gemeldet wird.

**Gegenargument:** Ein Befund ist eine Feststellung zu einem Zeitpunkt — das klingt nach Wert.

**Was den Ausschlag gibt:** Er wird nach der Aufnahme **weiterbearbeitet** — bewertet, weitergeleitet, reguliert. Etwas, das seinen Zustand ändert und dabei dasselbe bleibt, ist ein Ding.

### Station (7)

Als **Ding** eingeordnet.

**Gegenargument:** Für die Anmietung ist die Station vielleicht nur ein Ort — dann wäre sie ein Wert.

**Was den Ausschlag gibt:** Sie hat einen Lebenszyklus (eröffnet, umgebaut, geschlossen) und man verfolgt sie über die Zeit.

---

## 3 · Kontextabhängige Einordnung

Mehrere Gegenstände wechseln je nach Zweck. Zwei deutliche Fälle:

### Fahrzeugkategorie

| Kontext | Einordnung | Begründung |
|---|---|---|
| Anmietung | **Wert** | „Kompakt" ist eine Einteilung |
| Produktverwaltung | **Ding** | Kategorien werden angelegt, umbenannt, zusammengelegt, mit Preisen versehen — sie haben einen Lebenszyklus |

### Kilometerstand

| Kontext | Einordnung | Begründung |
|---|---|---|
| Anmietung | **Wert** | eine Ablesung, eine Zahl |
| Werkstatt | **Wert**, aber als Teil eines Dings | Die **Ablesung** ist ein Ding: Zeitpunkt, Ableser, Anlass. Der Stand selbst bleibt ein Wert |

Der zweite Fall zeigt ein wiederkehrendes Muster: Nicht der Wert wird zum Ding, sondern der **Vorgang um ihn herum**.

---

## 4 · Regeln in Werten

| Wert | Regeln, die dazugehören |
|---|---|
| **Mietzeitraum** | Ende liegt nach Beginn · Mindestdauer eine Stunde · maximale Dauer laut Vertrag |
| **Kaution** | nicht negativ · Währung gehört dazu · Rundung auf zwei Stellen |
| **Kilometerstand** | nicht negativ · bei Rückgabe nicht kleiner als bei Ausgabe |
| **Fahrzeugkategorie** | nur aus dem gültigen Katalog |
| **Fahrerlaubnisklasse** | nur aus dem amtlichen Katalog · bestimmt zulässige Fahrzeugkategorien |
| **Rechnungsanschrift** | Postleitzahl passt zum Land · Pflichtangaben je Land verschieden |

**Der Kilometerstand ist bemerkenswert:** Die Regel „bei Rückgabe nicht kleiner als bei Ausgabe" gehört nicht zum einzelnen Stand, sondern zum **Paar**. Das ist ein Hinweis darauf, dass ein Wert „Laufleistung während der Anmietung" fehlt.

---

## 5 · Wenn Werte nur Zahlen sind

**Wo die Regeln dann stehen:** bei jedem Aufrufer.

Ein Zeitraum als zwei getrennte Datumsangaben bedeutet: Jede Stelle, die einen Zeitraum entgegennimmt, muss selbst prüfen, dass das Ende nach dem Beginn liegt.

**Was daraus folgt:**

| Folge | Warum |
|---|---|
| Die Regel steht mehrfach | so oft, wie es Stellen gibt |
| Sie steht in Varianten | jede Stelle prüft etwas anders |
| Sie wird vergessen | an der neuen Stelle denkt niemand daran |
| Sie ist nicht auffindbar | „wo steht die Regel" hat keine Antwort |

**Das ist dieselbe Beobachtung wie bei den Aggregaten:** Was keinen Ort hat, steht überall.

---

## 6 · Die zwölf Angaben der Anschrift

| Angabe | Gehört zu | Begründung |
|---|---|---|
| Straße | **Anschrift** | Bestandteil des Werts |
| Hausnummer | **Anschrift** | |
| Postleitzahl | **Anschrift** | |
| Ort | **Anschrift** | |
| Land | **Anschrift** | |
| Kennung | **überflüssig** | Ein Wert braucht keine Identität — er ist durch seine Werte bestimmt |
| Anlagedatum | **Zuordnung** | Wann begann dieser Kunde, diese Anschrift zu verwenden |
| Änderungsdatum | **überflüssig** | Ein Wert wird nicht geändert, sondern ersetzt. Was sich ändert, ist die Zuordnung |
| Bearbeitervermerk | **Zuordnung** | Wer hat die Zuordnung geändert |
| Gültigkeitszeitraum | **Zuordnung** | „Der Kunde verwendet sie von–bis" |
| Unzustellbarkeitsmerkmal | siehe Aufgabe 10 | |
| Vermerk zur Unzustellbarkeit | siehe Aufgabe 10 | |

**Fünf Angaben gehören zur Anschrift** — genau die ursprünglichen fünf.

**Vier gehören zur Zuordnung.** Sie beschreiben nicht die Anschrift, sondern die Verbindung zwischen Kunde und Anschrift.

**Zwei sind überflüssig**, sobald die Anschrift ein Wert ist.

---

## 7 · Der Unterschied der beiden Sätze

> „Die Anschrift gilt bis 31.12."

Das ist falsch. Eine Anschrift gilt nicht bis zu einem Datum — sie existiert oder existiert nicht. Die Musterstraße 5 in 20095 Hamburg gibt es unabhängig davon, wer dort Post empfängt.

> „Der Kunde verwendet diese Anschrift bis 31.12."

Das trifft den Sachverhalt. Die **Verbindung** hat einen Zeitraum, nicht die Anschrift.

**Die allgemeine Form:** Wenn ein Wert eine Geschichte zu brauchen scheint, trägt meist die **Zuordnung** die Geschichte.

Dieselbe Auflösung galt bei der Kaution: Nicht der Betrag hat einen Verlauf, sondern die Sperrung.

---

## 8 · Was auf einer Rechnung von 2023 steht

**Die Werte, nicht ein Verweis.**

**Begründung:** Rechnungen müssen zehn Jahre unverändert nachweisbar bleiben. Ein Verweis wird beim Anzeigen aufgelöst — und liefert dann den heutigen Stand, nicht den von 2023.

Der Vorfall AV-3098 ist genau das: Der Verweis wurde aufgelöst und lieferte eine Anschrift, die der Kunde längst abgemeldet hatte.

**Was das für das Modell bedeutet:** Die Rechnung enthält die Anschrift als Wert — kopiert zum Zeitpunkt der Erstellung, danach unveränderlich.

**Der scheinbare Nachteil:** Redundanz. Dieselbe Anschrift steht auf hundert Rechnungen.

**Warum das richtig ist:** Es ist keine Redundanz, sondern ein Beleg. Eine Rechnung ist ein Dokument mit Beweiskraft; sie zeigt, was damals galt. Ein Verweis auf einen veränderlichen Gegenstand kann das nicht leisten.

---

## 9 · Die 14 Doppelten

**Wie sie entstehen:** Weil eine Anschrift eine Kennung hat, ist sie ein Gegenstand, der angelegt werden muss. Wer eine vorhandene nicht findet, legt eine neue an. Zwei Gegenstände mit identischen Werten, verschiedenen Kennungen.

**Warum sie im Vorschlag nicht entstehen können:**

Ein Wert ist durch seine Werte bestimmt. Zwei Anschriften mit gleicher Straße, Hausnummer, Postleitzahl, Ort und Land **sind dieselbe Anschrift** — es gibt nichts, worin sie sich unterscheiden könnten.

**Die Dublettenprüfung wird überflüssig.** Sie prüfte, ob zwei Gegenstände gleiche Werte haben. In einem Modell ohne Kennung ist die Frage gegenstandslos.

**Nebeneffekt:** Auch die drei falsch verknüpften Anschriften können nicht entstehen. Eine Verwechslung bei der Auswahl setzt voraus, dass es etwas auszuwählen gibt.

---

## 10 · Das Unzustellbarkeitsmerkmal

Drei vertretbare Antworten. Der Vorschlag wählt die dritte.

### Möglichkeit A · Eigenschaft der Anschrift

**Dafür:** Wenn die Straße nicht existiert, ist die Anschrift als solche unbrauchbar.

**Dagegen:** Dann wäre sie kein reiner Wert mehr — sie trüge einen Zustand. Und: Eine Anschrift kann für einen Empfänger unzustellbar sein und für einen anderen nicht.

### Möglichkeit B · Eigenschaft der Zuordnung

**Dafür:** „Dieser Kunde ist unter dieser Anschrift nicht erreichbar" ist präziser als „diese Anschrift ist unzustellbar".

**Dagegen:** Es sagt nichts darüber, warum und wann. Ein einzelner Rückläufer kann ein Zufall sein.

### Möglichkeit C · Ein eigener Gegenstand: der Zustellversuch

**Dafür:**

- Ein Zustellversuch hat Datum, Ergebnis und Grund — das sind Angaben, die weder zur Anschrift noch zur Zuordnung passen
- Mehrere Versuche sind möglich; erst ihre Häufung rechtfertigt eine Bewertung
- Die Frage „seit wann unzustellbar" wird beantwortbar
- Die 80 fehlerhaften Gültigkeitszeiträume deuten darauf hin, dass Zeitangaben an der Anschrift ohnehin ein Problem sind

**Dagegen:** Ein weiterer Gegenstand im Modell für etwas, das selten vorkommt.

**Der Vorschlag wählt C**, weil das Merkmal offensichtlich Angaben mit sich bringt (wann, warum, wie oft), die einen eigenen Gegenstand nahelegen. Ein Wahrheitswert komprimiert eine Aussage auf ein Bit und verliert, worum es ging.

**Die Zuordnung erhält daraus abgeleitet** ein Merkmal „erreichbar ja/nein" — aber als Ergebnis, nicht als Eingabe.

---

## Diskussionsanschluss

Die Anschrift wird jetzt auf jede Rechnung kopiert. Bei 400.000 Rechnungen im Jahr steht dieselbe Anschrift tausendfach. Ist das ein Problem — und wenn ja, für wen?
