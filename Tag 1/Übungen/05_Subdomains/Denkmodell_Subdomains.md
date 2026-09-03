# Denkmodell · Fachbereiche einordnen und Aufwand zuteilen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Gespräch

| Signal | Deutet auf |
|---|---|
| „Damit gewinnen wir jede zweite Ausschreibung" | Core |
| „Das können die Großen nicht" | Core |
| „Das ist bei allen gleich" | Supporting oder Generic |
| „Dafür gibt es Branchenlösungen" | Supporting, zukaufen |
| „Das macht jedes Unternehmen so" | Generic |
| „Das haben wir aus historischen Gründen selbst gebaut" | vermutlich falsch eingeordnet |
| „Da war nie Kapazität" bei einem Kernthema | Fehlverteilung |
| „Das weiß ich halt" | Wissen in Köpfen statt in Software — bei Core ein Risiko |

### In der Aufwandsverteilung

| Signal | Diagnose |
|---|---|
| Der größte Entwicklungsaufwand liegt nicht im Kernbereich | Fehlverteilung |
| Ein Kernbereich ist zugekauft und wird nicht weiterentwickelt | schwerwiegend |
| Ein Standardbereich ist selbst gebaut | erheblich, aber oft nicht mehr korrigierbar |
| Ein Standardprodukt wurde stark angepasst | Nachteile beider Wege |
| Ein Sonderfall hat einen ganzen Bereich in die Eigenentwicklung gezogen | falsche Grenze |

---

## Stufe 2 · Erkenntnisse

**1. Core Domains sind selten.**
Meist gibt es genau eine. Wer drei findet, hat vermutlich Wichtigkeit mit Unterscheidung verwechselt.

**2. Wichtig und unterscheidend sind zweierlei.**
Die Buchhaltung ist unverzichtbar und unterscheidet niemanden. Verzichtbarkeit ist nicht das Kriterium.

**3. Die Einordnung ist eine Aussage über den Wettbewerb, nicht über die Software.**
Sie betrifft den Problemraum. Was das Unternehmen tut, nicht wie es gebaut ist.

**Was gesucht wird:** die Bereiche, in denen Aufwand einen Unterschied macht.

---

## Stufe 3 · Die drei Kategorien

| Kategorie | Erkennungszeichen | Vorgehen |
|---|---|---|
| **Core** | Wettbewerber können es nicht; es steht im Verkaufsgespräch | selbst bauen, beste Leute, laufend |
| **Supporting** | notwendig, branchenüblich, kein Vorteil | selbst wenn nötig, sparsam; zukaufen wenn möglich |
| **Generic** | überall gleich, Standardprodukte vorhanden | Standard nehmen, **nicht anpassen** |

---

## Stufe 4 · Entscheidung

### Frage 1 — Würde ein Wettbewerber, der es genauso gut kann, uns gefährlich?

- **Ja, und er kann es nicht** → Core
- **Ja, aber alle können es** → Supporting
- **Nein, gleichgültig** → Generic

Die zweite Hälfte der Frage ist entscheidend. „Können es alle?" trennt Core von Supporting.

### Frage 2 — Gibt es Standardprodukte?

- **Ja, und sie decken es ab** → Generic. Standard nehmen.
- **Ja, aber sie passen nicht ganz** → prüfen, ob der eigene Prozess anpassbar ist, bevor das Produkt angepasst wird.
- **Nein** → Supporting oder Core.

### Frage 3 — Zieht ein Sonderfall einen ganzen Bereich in die Eigenentwicklung?

- **Ja** → die Grenze ist falsch gezogen. Den Sonderfall abtrennen, den Rest als Standard nehmen.
- **Nein** → die Einordnung trägt.

Diese Frage rettet oft eine ganze Generic Subdomain. Im Beispiel: Die Kautionsabwicklung ist speziell, die Buchhaltung ist es nicht.

### Frage 4 — Passt der tatsächliche Aufwand zur Einordnung?

Für jeden Bereich Soll und Ist gegenüberstellen:

| Ist | Soll | Bewertung |
|---|---|---|
| Core zugekauft | selbst | schwerwiegend |
| Generic selbst gebaut | Standard | erheblich, aber selten korrigierbar |
| Supporting selbst, sparsam | dasselbe | passt |

---

## Der Denkweg auf einen Blick

```
Wo fliesst der Entwicklungsaufwand hin?
        ↓
Womit unterscheidet sich das Unternehmen?
        ↓
Waere ein Wettbewerber mit gleicher Faehigkeit gefaehrlich?
        ↓ nein → Generic          ↓ ja
                        Koennen es alle?
                        ↓ ja → Supporting   ↓ nein → CORE
        ↓
Zieht ein Sonderfall einen Bereich in die Eigenentwicklung?
        ↓ ja → Grenze falsch, Sonderfall abtrennen
        ↓ nein
Passt der Ist-Aufwand zur Einordnung?
        ↓ nein → Abweichung benennen, mit Risiko und Nutzen
```

---

## Die eine Prüffrage

> **Würde ein Wettbewerber, der dies genauso gut kann wie wir, uns gefährlich — und können es alle?**

Gefährlich und nicht alle → Core.
Gefährlich, aber alle → Supporting.
Nicht gefährlich → Generic.

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wurde mit Umsatzanteil begründet? | kein Kriterium — die Buchhaltung verarbeitet 100 Prozent |
| Wurde mit Kompliziertheit begründet? | kein Kriterium — Kompliziertheit ist kein Wert |
| Wurde mit bisherigem Aufwand begründet? | zirkulär |
| Sind drei oder mehr Bereiche Core? | vermutlich Wichtigkeit mit Unterscheidung verwechselt |
| Ist gar nichts Core? | dann ist das Unternehmen austauschbar — oder die Analyse unvollständig |

---

## Wenn die Entscheidung steht

**Eine falsche Einordnung ist nicht automatisch ein Auftrag zur Korrektur.**
Was gebaut und bezahlt ist, kostet im Wechsel mehr als es spart. Der Befund ist dann eine Lehre für künftige Entscheidungen. Handlungsbedarf entsteht bei laufenden Kosten, bei Risiko oder bei einer ohnehin anstehenden Änderung.

**Wissen in Köpfen ist bei einer Core Domain ein Risiko.**
Wenn der Unterschied zum Wettbewerb an vier Personen hängt, ist er nicht gesichert. Dieses Wissen zu erheben ist der erste Schritt vor jeder Weiterentwicklung — wer erst baut und dann fragt, baut das Alte nach.

**Standard nehmen heißt: nicht anpassen.**
Ein stark angepasstes Standardprodukt hat Lizenzkosten und Entwicklungsaufwand. Wo Anpassung nötig scheint, gehört zuerst der eigene Prozess geprüft.

**Die Einordnung ändert sich mit dem Geschäftsmodell, nicht mit dem Entwurf.**
Sie ist selten neu zu treffen — aber wenn sich das Geschäft ändert, gründlich.

**Subdomain und Bounded Context nicht verwechseln.**
Die Subdomain liegt im Problemraum: was das Unternehmen tut. Der Bounded Context im Lösungsraum: wie die Software geschnitten ist. Sie fallen nicht notwendig zusammen — Deckungsgleichheit ist wünschenswert, aber nicht erzwingbar.

**Die Einordnung gehört in jeden Vorhabensvorschlag.**
Sonst landet ein Vorhaben bei dem, der gerade Kapazität hat. Genau so entsteht die Fehlverteilung.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Bounded Context | Problemraum gegen Lösungsraum |
| Priorisierung | betrifft einzelne Vorhaben, nicht ganze Bereiche |
| Kritikalität | ein Ausfall der Buchhaltung ist kritisch und macht sie nicht zur Core Domain |
| Make-or-Buy im Einzelfall | die Einordnung gilt für den Bereich, nicht für ein Produkt |
| Organigramm | Abteilungen sind keine Subdomains |
