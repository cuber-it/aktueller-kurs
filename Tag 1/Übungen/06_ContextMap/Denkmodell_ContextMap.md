# Denkmodell · Beziehungen zwischen Kontexten bestimmen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Was im Gespräch auffällt

| Signal | Deutet auf |
|---|---|
| „Auf deren Format haben wir keinen Einfluss" | Conformist oder Anticorruption Layer |
| „Wenn wir was brauchen, reden die mit uns" | Customer/Supplier |
| „Da gibt es eine öffentliche Spezifikation" | Published Language, oft mit Open Host Service |
| „Wir arbeiten mit denselben Daten" | Shared Kernel |
| „Wir müssen gemeinsam ausliefern" | Shared Kernel oder Partnership |
| „Wenn die was ändern, kriegen wir eine Mail" | einseitige Abhängigkeit, wir sind unten |
| „Damit haben wir nichts zu tun" | Separate Ways — prüfen, ob es stimmt |

### Was in der Zusammenarbeit auffällt

| Signal | Konkret |
|---|---|
| Fremde Begriffe im eigenen Modell | Bezeichnungen des Lieferanten tauchen auf, wo er nichts zu suchen hat |
| Eine fremde Kennung wird in mehreren Kontexten ausgewertet | es fehlt eine Grenze |
| Niemand kann sagen, wen eine Änderung trifft | es gibt keine Übersicht |
| Zwei Kontexte ändern dasselbe Modell | Shared Kernel, ob gewollt oder nicht |
| Eine Anbindung ohne Übersetzungsschicht | Conformist ohne Grenze — der teure Fall |

---

## Stufe 2 · Erkenntnisse

**1. Jede Beziehung hat eine Richtung.**
Wer muss nachziehen, wenn sich beim anderen etwas ändert? Das ist die bestimmende Frage, nicht die Datenrichtung.

**2. Der Einfluss entscheidet über das Muster.**
Kein Einfluss, viel Einfluss oder gegenseitige Abhängigkeit — daraus folgt fast alles.

**3. Conformist ohne Grenze ist der teure Fall.**
Sich einem Format zu fügen ist legitim. Es ungeschützt in die eigenen Kontexte zu lassen, ist der Fehler.

**Was gesucht wird:** nicht die Schnittstellen, sondern die **Art der Abhängigkeit**.

---

## Stufe 3 · Die Muster im Überblick

| Muster | Einfluss des Abnehmers | Wer zieht nach |
|---|---|---|
| **Customer / Supplier** | Anforderungen möglich, es gibt Absprache | Abnehmer, mit Vorlauf |
| **Conformist** | keiner | Abnehmer, vollständig |
| **Anticorruption Layer** | keiner, aber geschützt | nur die Übersetzung |
| **Open Host Service** | (Sicht des Lieferanten) viele Abnehmer | Abnehmer |
| **Published Language** | gemeinsames Format | alle, koordiniert |
| **Shared Kernel** | gegenseitig | beide, sofort |
| **Partnership** | gegenseitig, organisatorisch | beide, koordiniert |
| **Separate Ways** | keine Beziehung | niemand |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es überhaupt eine Beziehung?

- **Nein**, kein Informationsfluss → **Separate Ways**. Das ist eine Entscheidung, keine Lücke, und gehört in die Map.
- **Ja** → weiter.

### Frage 2 — Ist die Abhängigkeit gegenseitig?

- **Nein**, einer liefert, einer nimmt → weiter mit Frage 3.
- **Ja**, beide ändern dasselbe → **Shared Kernel** (geteiltes Modell) oder **Partnership** (geteilte Planung).

**Zum Preis:** Shared Kernel ist das teuerste Muster. Koordination bei jeder Änderung, gemeinsame Releases, der langsamere bestimmt das Tempo. Es lohnt nur bei fachlicher Untrennbarkeit.

### Frage 3 — Wie viel Einfluss hat der Abnehmer?

- **Einfluss durch Absprache** → **Customer / Supplier**. Erkennungszeichen: Änderungswünsche werden gehört, es gibt Vorlauf.
- **Kein Einfluss** → weiter mit Frage 4.

### Frage 4 — Wird das fremde Modell übersetzt?

- **Nein**, es wird übernommen → **Conformist**. Legitim bei stabilem Format und geringer Bedeutung.
- **Ja**, an der Grenze wird in eigene Begriffe übersetzt → **Anticorruption Layer**.

**Der Prüfstein:** Tauchen Begriffe des Lieferanten außerhalb der Anbindung auf? Dann ist es Conformist — auch wenn niemand das entschieden hat.

---

## Der Denkweg auf einen Blick

```
Zwei Kontexte tauschen Information aus
        ↓
Wer zieht nach, wenn sich etwas aendert?
        ↓
Gibt es ueberhaupt eine Beziehung?      nein → Separate Ways
        ↓ ja
Gegenseitige Abhaengigkeit?             ja → Shared Kernel / Partnership
        ↓ einseitig
Einfluss durch Absprache?               ja → Customer / Supplier
        ↓ kein Einfluss
Wird an der Grenze uebersetzt?          nein → Conformist
        ↓ ja
                        ANTICORRUPTION LAYER
```

---

## Die eine Prüffrage

> **Wer muss nachziehen, wenn sich beim anderen etwas ändert — und wie viel Einfluss hat er darauf?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Tauchen fremde Begriffe im eigenen Modell auf? | Conformist ohne Grenze — der teure Fall |
| Wird ein Fremdcode in mehreren Kontexten ausgewertet? | es fehlt ein Anticorruption Layer |
| Ändern zwei Kontexte dasselbe Modell? | Shared Kernel, ob gewollt oder nicht |
| Ist das Format stabil und die Bedeutung gering? | Conformist ist ausreichend |
| Kann niemand sagen, wen eine Änderung trifft? | die Map fehlt |

---

## Wenn die Entscheidung steht

**Conformist ist eine Wahl, kein Versäumnis.**
Bei einem stabilen Standardformat von geringer Bedeutung ist ein Anticorruption Layer Aufwand ohne Gegenwert. Der Fehler entsteht, wenn Conformist aus Zeitdruck **entsteht**, statt entschieden zu werden — und wenn das Fremdformat dann über die Anbindung hinaus wandert.

**Conformist und Anticorruption Layer schließen einander nicht aus.**
Man fügt sich dem Format **und** übersetzt es an der Grenze. Das ist der Regelfall bei Fremdsystemen ohne Einfluss.

**Der Shared Kernel gehört regelmäßig überprüft.**
Er entsteht leicht und ist schwer wieder loszuwerden. Die Frage lautet: Brauchen beide wirklich dasselbe Modell, oder nur dieselben Objekte in verschiedener Sicht?

**Die Map gehört auf eine Seite.**
Eine Darstellung über drei Seiten wird vor einer Änderung nicht gelesen. Lieber acht Kästen mit benannten Beziehungen als eine vollständige Systemlandschaft.

**Die Map beantwortet eine Frage, die vor jeder Änderung gestellt wird:**
Wen trifft es? Wenn niemand das beantworten kann, fehlt die Map — oder sie ist nicht aktuell.

**Aktualität kommt durch Anlass, nicht durch Turnus.**
Eine Map, die jährlich überarbeitet wird, ist meist veraltet. Eine, die bei jeder neuen Anbindung ergänzt wird, bleibt brauchbar.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Systemlandschaft | zeigt Systeme und Technik, nicht fachliche Abhängigkeiten |
| Schnittstellenliste | zeigt, **dass** etwas fließt, nicht **wie** die Abhängigkeit beschaffen ist |
| Architekturdiagramm | zeigt Bausteine, nicht wer bei Änderungen nachzieht |
| Datenflussdiagramm | zeigt die Richtung der Daten — die Abhängigkeitsrichtung kann entgegengesetzt sein |
| Organigramm | Teams sind nicht Kontexte, auch wenn sie oft zusammenfallen |
