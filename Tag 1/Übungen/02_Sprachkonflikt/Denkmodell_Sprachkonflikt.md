# Denkmodell · Sprachkonflikte erkennen und auflösen

Wie man von einer Begriffsverwirrung zu Kontextgrenzen kommt. Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Was im Gespräch mit dem Fachbereich auffällt

| Signal | Beispielformulierung |
|---|---|
| „Das ist bei uns was anderes" | ein Wort, zwei Sachen — der gefährlichste Fall |
| „Bei uns heißt das anders" | zwei Wörter, eine Sache — harmloser, weil auffällig |
| „Kommt darauf an, wen Sie fragen" | die direkteste Ansage |
| Zwei Bereiche liefern verschiedene Zahlen für dieselbe Frage | und beide haben recht |
| Eine Definition wurde festgelegt und wird nicht verwendet | der Kompromiss passte für niemanden |
| Ein Glossar hängt aus, ändert aber nichts | es beschreibt keine Praxis |
| Jemand erklärt einen Begriff mit einem Nebensatz | „Kunde, also der, der zahlt" |

### Was in der täglichen Arbeit auffällt

| Signal | Konkret |
|---|---|
| Ein Begriff mit vielen Merkmalen, meist leer | jedes Merkmal gehört einem Bereich |
| „Art", „Typ", „Status", „Kategorie" nebeneinander | Bedeutungsunterschiede, als Einteilung getarnt |
| Dieselbe Angabe wird je nach Bereich anders verwendet | nirgends festgehalten |
| Auswertungen werden von Hand nachbearbeitet | die Software kann die Frage nicht beantworten |
| Mündlich weitergegebene Sonderregeln | Wissen ohne Ort |
| Ein Begriff, der allen dienen soll | „Kunde" mit 47 Merkmalen |

---

## Stufe 2 · Erkenntnisse

**1. Die Bedeutungen sind fachlich berechtigt.**
Niemand irrt sich. Jede Bedeutung folgt aus der Arbeit des Bereichs. Ein Stationsleiter *kann* nicht anders, als die Person vor sich als Kunden zu sehen.

**2. Sie sind nicht verhandelbar.**
Deshalb scheitern Einigungsworkshops. Ein Kompromiss zwingt mindestens zwei Bereiche zu einem Hilfsbegriff für das, was sie eigentlich meinen.

**3. Die Grenze verläuft dort, wo die Bedeutung wechselt.**
Nicht entlang der Abteilungsstruktur, nicht entlang der Systeme — entlang der Sprache.

**Was gesucht wird:** die Grenzen des Modells, nicht der einheitliche Begriff.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Bounded Contexts** | die Bedeutungen fachlich berechtigt verschieden sind |
| **Eine gemeinsame Definition** | es sich um dieselbe Sache mit verschiedenen Wörtern handelt |
| **Glossar ohne Grenzen** | nur Verständigung fehlt, kein Modellkonflikt |
| **Unterschiedliche Sichten auf ein Modell** | derselbe Gegenstand, verschiedener Detailbedarf |
| **Ein Begriff, der neu benannt wird** | ein Bereich verwendet einen Begriff erkennbar unpräzise |

---

## Stufe 4 · Entscheidung

### Frage 1 — Widerspruch oder Vereinigungsmenge?

- Die Zusammenführung ergäbe einen **Widerspruch** — derselbe Konzern ist 1 und ist 340 → **Kontextgrenze**.
- Sie ergäbe eine **Vereinigungsmenge** — der eine braucht fünf Felder, der andere zwanzig → **eine Sache, verschiedene Sichten**.

Das ist der schärfste Prüfstein. Unterschiedliche Detailtiefe ist kein Konflikt.

### Frage 2 — Folgt die Bedeutung aus der Arbeit?

- **Ja** — der Stationsleiter sieht die Person, der Vertrieb sieht das Unternehmen → die Bedeutung ist berechtigt, die Grenze ist echt.
- **Nein**, es ist Gewohnheit oder Nachlässigkeit → ein Begriff kann bereinigt werden.

### Frage 3 — Wird das Wort in beiden Bedeutungen gebraucht?

- **Ja**, beide Seiten brauchen es täglich → Kontexte trennen, jede Seite behält ihr Wort.
- **Nein**, eine Seite verwendet es nebenbei → dort umbenennen. Im Beispiel wird „Kunde" an der Station zu **Mieter** — präziser und näher am tatsächlichen Sprachgebrauch.

### Frage 4 — Was passiert an der Grenze?

Für jede gezogene Grenze:

- **Welche Information überquert sie?**
- **Wie wird übersetzt?**
- **Wer übersetzt?** — der **empfangende** Kontext, sonst müsste der Sender alle Empfänger kennen.

Eine Grenze ohne benannte Übersetzung ist keine Entscheidung, sondern eine Verschiebung des Problems.

---

## Der Denkweg auf einen Blick

```
Ein Begriff bedeutet in mehreren Bereichen Verschiedenes
        ↓
Beide Bedeutungen sind fachlich richtig  →  gesucht: Grenzen, nicht Einheitlichkeit
        ↓
Optionen: Bounded Contexts · gemeinsame Definition · Sichten · Umbenennung
        ↓
Widerspruch oder Vereinigungsmenge?      Vereinigung → eine Sache, zwei Sichten
        ↓ Widerspruch
Folgt die Bedeutung aus der Arbeit?      nein → Begriff bereinigen
        ↓ ja
Brauchen beide Seiten das Wort?          nein → eine Seite benennt um
        ↓ ja
Uebersetzung an der Grenze geklaert?     nein → Entscheidung unvollstaendig
        ↓ ja
                              BOUNDED CONTEXTS
```

---

## Die eine Prüffrage

> **Führt die Zusammenführung der Bedeutungen zu einem Widerspruch — und folgt jede Bedeutung aus der Arbeit des Bereichs?**

Zweimal ja → Kontextgrenze.

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Meinen beide dasselbe, brauchen nur verschieden viel? | eine Sache, zwei Sichten — keine Grenze |
| Verwendet eine Seite den Begriff nur nebenbei? | dort umbenennen |
| Fehlt nur Verständigung, nicht Modelltrennung? | ein Glossar genügt |
| Lässt sich die Grenze nicht mit einer Aufgabe begründen? | vermutlich Abteilungsstruktur statt Fachlichkeit |

---

## Wenn die Entscheidung steht

**Die Sprache folgt der Grenze, nicht umgekehrt.**
Innerhalb eines Kontextes gilt ein Begriff eindeutig. An der Grenze endet seine Gültigkeit. Wer versucht, einen Begriff über Grenzen hinweg zu retten, baut den Konflikt wieder ein.

**Grenzen entlang von Aufgaben, nicht entlang von Abteilungen.**
Die Organisationsstruktur ändert sich häufiger als die Fachlichkeit. Wer Kontexte nach dem Organigramm schneidet, muss beim nächsten Umbau nachziehen. Im Beispiel liegen Flotte und Werkstatt in einem Kontext, obwohl es zwei Abteilungen sind — weil sie dieselben Objekte meinen.

**Umbenennen ist ein legitimes Mittel.**
„Kunde" an der Station zu „Mieter" zu machen, ist kein Verlust. Es zwingt zur Präzision und deckt auf, ob der Begriff überhaupt gemeint war.

**Eine Anforderung, die über Grenzen geht, gehört präzisiert.**
„Umsatz je Kunde" ist unterspezifiziert, sobald es mehrere Kundenbegriffe gibt. Die richtige Antwort ist die Rückfrage, nicht der Kompromiss.

**Das Glossar kommt danach, nicht davor.**
Ein Glossar über Kontextgrenzen hinweg beschreibt einen Kompromiss und wird nicht benutzt. Ein Glossar **je Kontext** beschreibt, was dort tatsächlich gilt — und wird benutzt.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Fehler in den Daten | die Daten sind richtig, nur die Frage ist mehrdeutig |
| Kommunikationsproblem | Reden hilft nicht, wenn beide Bedeutungen berechtigt sind |
| Unterschiedliche Detailtiefe | kein Widerspruch, nur unterschiedlicher Bedarf |
| Fehlende Dokumentation | ein Glossar löst es nicht, wenn Modellgrenzen fehlen |
| Subdomain | die Subdomain liegt im Problemraum, der Bounded Context im Lösungsraum |
