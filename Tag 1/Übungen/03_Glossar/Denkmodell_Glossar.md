# Denkmodell · Ein Glossar bauen, das benutzt wird

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Woran man merkt, dass ein Glossar fehlt

| Signal | Beispiel |
|---|---|
| Dieselbe Frage wird mehrfach gestellt | „Was ist bei uns nochmal ein Vorgang?" |
| Missverständnisse werden mündlich geklärt und nirgends festgehalten | beim nächsten Mal beginnt es von vorn |
| Neue Mitarbeiter brauchen lange, bis sie mitreden | die Sprache steht nirgends |
| Anforderungen werden falsch verstanden | ein Begriff wurde anders gelesen als gemeint |
| In Tickets stehen mehrdeutige Begriffe ohne Präzisierung | niemandem fällt es auf |

### Woran man merkt, dass ein vorhandenes Glossar nicht taugt

| Signal | Diagnose |
|---|---|
| Kaum Zugriffe | es liegt am falschen Ort oder hilft nicht |
| Kein Dokument verweist darauf | es ist nicht Teil der Arbeit |
| Definitionen mit „je nach Kontext" | es umfasst mehrere Kontexte |
| Definitionen aus dem Lehrbuch | „Kunde: wer Leistungen bezieht" sagt nichts über dieses Unternehmen |
| Alphabetisch sortiert | Zusammengehöriges steht auseinander |
| Enthält Begriffe, die niemand verwendet | Vollständigkeit war das Ziel, nicht Nutzen |
| Niemand ist zuständig | es veraltet ab dem Tag der Fertigstellung |

---

## Stufe 2 · Erkenntnisse

**1. Eindeutigkeit ist nur innerhalb eines Kontextes möglich.**
Über Grenzen hinweg gibt es keine gemeinsame Definition — sonst wäre es keine Grenze.

**2. Ein Glossar wird nicht gelesen, sondern nachgeschlagen.**
Und zwar bei drei Anlässen: Einstieg in einen Kontext, Klärung eines Missverständnisses, Formulierung einer Anforderung. Alle drei sind punktuell.

**3. Vollständigkeit ist kein Ziel.**
Ein Verzeichnis mit zehn nützlichen Einträgen wird benutzt, eines mit 84 nicht.

**Was gesucht wird:** die Begriffe, die in diesem Kontext täglich vorkommen — mit einer Definition, die eine Frage beantwortet.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Glossar je Kontext** | Kontextgrenzen bestehen und Begriffe sich unterscheiden |
| **Ein Gesamtglossar** | es nur einen Kontext gibt |
| **Kein Glossar, dafür sprechende Namen im Code** | das Modell selbst die Sprache trägt |
| **Begriffsverzeichnis als Teil des Modells** | Klassennamen und Glossareinträge dieselben sind |
| **Nur Abgrenzungen dokumentieren** | die meisten Begriffe unstrittig sind |

---

## Stufe 4 · Entscheidung

### Frage 1 — Wie viele Kontexte umfasst das Verzeichnis?

- **Einen** → Eindeutigkeit ist erreichbar.
- **Mehrere** → es entstehen zwangsläufig Oberdefinitionen. Aufteilen, bevor geschrieben wird.

Das ist die erste und wichtigste Entscheidung. Ein Gesamtglossar über vier Kontexte kann gar nicht gut werden.

### Frage 2 — Beantwortet die Definition eine Frage, die jemand hat?

- **Ja** → aufnehmen.
- **Nein**, sie beschreibt nur, was ohnehin klar ist → weglassen.

Der Prüfstein: Würde jemand diesen Eintrag nachschlagen? „Kennzeichen: amtliches Kennzeichen eines Fahrzeugs" schlägt niemand nach.

### Frage 3 — Definition oder Beispiel?

- Wo eine **Abgrenzung** nötig ist → Definition mit „nicht zu verwechseln mit".
- Wo der Begriff **anschaulich** ist → Beispiel. „Ein Mieter ist die Person, die den Führerschein vorlegt" ist besser als jede Definition.

### Frage 4 — Wo liegt es?

- **Am Ort der Arbeit** — im Repository neben dem Code, im Ticketsystem, im Wiki des Teams.
- **Nicht** in einem separaten Dokumentenablagesystem. Elf Zugriffe in acht Monaten sind ein Ortsproblem, kein Inhaltsproblem.

---

## Der Denkweg auf einen Blick

```
Begriffe werden unterschiedlich verstanden
        ↓
Ein Verzeichnis soll helfen  →  aber welches, fuer wen, wo?
        ↓
Optionen: je Kontext · gesamt · sprechende Namen · nur Abgrenzungen
        ↓
Umfasst es mehrere Kontexte?          ja → erst aufteilen
        ↓ einen
Beantwortet der Eintrag eine Frage?   nein → weglassen
        ↓ ja
Abgrenzung noetig?                    ja → Definition, sonst Beispiel
        ↓
Liegt es am Ort der Arbeit?           nein → verschieben
        ↓ ja
                          GLOSSAR JE KONTEXT
```

---

## Die eine Prüffrage

> **Kann jeder Eintrag eindeutig formuliert werden — ohne „je nach Kontext"?**

Ja → der Kontext ist richtig geschnitten.
Nein → das Verzeichnis umfasst mehrere Kontexte.

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Enthält eine Definition eine Aufzählung von Bedeutungen? | Kontext falsch geschnitten oder Begriff gehört geteilt |
| Würde niemand den Eintrag nachschlagen? | weglassen |
| Steht der Begriff so auch im Lehrbuch? | er sagt nichts über dieses Unternehmen |
| Ist der Begriff historisch? | kennzeichnen oder entfernen |
| Gibt es keine Zuständigkeit? | das Verzeichnis veraltet ab Tag eins |

---

## Wenn die Entscheidung steht

**Das Glossar kommt nach den Kontextgrenzen, nicht davor.**
Wer zuerst ein Glossar baut, landet bei Oberdefinitionen. Wer zuerst die Grenzen zieht, kann eindeutig formulieren.

**Die Gliederung kommt aus der Fachlichkeit.**
Nach Ablauf, nach Zusammenhang, nach Aggregat — nur nicht alphabetisch. Ein Verzeichnis, das man von vorn lesen kann, wird gelesen.

**Abgrenzungen sind wertvoller als Definitionen.**
„Mieter — nicht zu verwechseln mit dem Rahmenvertragspartner" verhindert mehr Fehler als jede sorgfältige Definition. Die Fehlentwicklung in AV-2298 wäre durch genau diesen Satz vermieden worden.

**Übersetzungshinweise an den Grenzen gehören dazu.**
„Wird in der Fakturierung zur Position" sagt, wo der Begriff endet. Ohne das wirkt jeder Kontext, als stünde er allein.

**Wenige Einträge, dafür gepflegt.**
Zehn Einträge, die stimmen, schlagen 84, die veralten. Ein Eintrag entsteht, wenn ein Missverständnis auftrat — nicht, wenn jemand die Liste vervollständigen will.

**Die beste Fassung ist die, die im Code steht.**
Wenn Klassen und Methoden die Begriffe des Glossars tragen, pflegt sich das Verzeichnis mit. Das ist der Zustand, den DDD anstrebt — dann ist das Glossar eine Lesehilfe zum Modell, kein Parallelwerk.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Datenwörterbuch | beschreibt Felder und Typen, nicht Fachbegriffe |
| Fachkonzept | beschreibt Abläufe, nicht Sprache |
| Ubiquitous Language | die Sprache ist das Ziel, das Glossar nur ihre Aufzeichnung |
| Anforderungsdokument | hält fest, was gebaut wird, nicht was Wörter bedeuten |
| Onboarding-Material | überschneidet sich, hat aber einen anderen Zweck |
