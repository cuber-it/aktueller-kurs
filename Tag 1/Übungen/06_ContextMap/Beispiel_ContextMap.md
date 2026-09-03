# Beispiel · Eine Context Map in klein

Drei Kontexte, vier Beziehungen, vollständig durchgeführt.

---

## Die Ausgangslage

Eine Hausverwaltung mit drei Bereichen und einem Fremdsystem.

| Kontext | Verantwortet |
|---|---|
| **Mietverwaltung** | Mietverträge, Mieterwechsel, Kündigungen |
| **Instandhaltung** | Reparaturaufträge, Handwerker, Termine |
| **Buchhaltung** | Mieteingänge, Nebenkostenabrechnung, Mahnungen |
| **Bankschnittstelle** (extern) | Kontoauszüge, Lastschriften |

---

## Was die Beteiligten sagen

**Mietverwaltung:** „Wenn ein Mietvertrag beginnt oder endet, muss die Buchhaltung das wissen. Sonst wird falsch abgerechnet."

**Buchhaltung:** „Ich bekomme die Vertragsdaten und mache daraus Sollstellungen. Wenn die Mietverwaltung ihr Format ändert, muss ich nachziehen. Mitsprache habe ich nicht, brauche ich auch nicht."

**Instandhaltung:** „Wir brauchen von der Mietverwaltung nur, wer in welcher Wohnung wohnt — für den Zugang. Und wir melden zurück, wenn eine Wohnung nicht bewohnbar ist, weil das die Miete mindert."

**Buchhaltung zur Bank:** „Das ist ein Bankformat, CAMT. Da ändert sich alle paar Jahre was, und dann müssen wir ran. Einfluss haben wir null."

---

## Schritt 1 · Wer zieht nach?

| Beziehung | Ändert sich bei… | …zieht nach |
|---|---|---|
| Mietverwaltung → Buchhaltung | Mietverwaltung | Buchhaltung |
| Mietverwaltung → Instandhaltung | Mietverwaltung | Instandhaltung |
| Instandhaltung → Mietverwaltung | Instandhaltung | Mietverwaltung |
| Bank → Buchhaltung | Bank | Buchhaltung |

## Schritt 2 · Einfluss prüfen

| Beziehung | Einfluss des Abnehmers |
|---|---|
| Buchhaltung auf Mietverwaltung | gering — „Mitsprache habe ich nicht" |
| Instandhaltung auf Mietverwaltung | nicht erwähnt, vermutlich gering |
| Mietverwaltung auf Instandhaltung | nicht erwähnt |
| Buchhaltung auf Bank | **keiner** — „Einfluss haben wir null" |

## Schritt 3 · Muster zuordnen

```
   ┌──────────────────┐
   │  Mietverwaltung  │
   └───┬──────────┬───┘
       │ C/S      │ C/S
       ▼          ▼
┌──────────────┐  ┌──────────────────┐
│ Buchhaltung  │  │ Instandhaltung   │
└──────▲───────┘  └────────┬─────────┘
       │                   │ C/S
       │ Conformist        │ (Minderung)
       │                   ▼
┌──────┴───────┐    ┌──────────────────┐
│ Bank (CAMT)  │    │  Mietverwaltung  │
└──────────────┘    └──────────────────┘
```

| Beziehung | Muster | Begründung |
|---|---|---|
| Mietverwaltung → Buchhaltung | Customer/Supplier | intern, im selben Haus, Absprache grundsätzlich möglich |
| Mietverwaltung → Instandhaltung | Customer/Supplier | dito |
| Instandhaltung → Mietverwaltung | Customer/Supplier | die Rückmeldung zur Bewohnbarkeit |
| Bank → Buchhaltung | **Conformist** auf **Published Language** | CAMT ist ein veröffentlichter Standard, kein Einfluss |

## Schritt 4 · Wo fehlt eine Grenze?

**Prüffrage:** Tauchen CAMT-Begriffe außerhalb der Bankanbindung auf?

Angenommen, die Buchhaltung führt Zahlungen mit dem CAMT-Statuscode `BOOK` und `PDNG` und die Mahnläufe werten diese Codes direkt aus.

**Dann ist das Bankformat durchgesickert.** Bei der nächsten CAMT-Version ist nicht nur die Anbindung betroffen, sondern auch das Mahnwesen.

**Die Grenze gehört zwischen Bank und Buchhaltung:**

```
   ┌──────────────┐
   │  Bank (CAMT) │
   └──────┬───────┘
   ╔══════▼═══════╗
   ║ Anticorruption║
   ║    Layer      ║
   ╚══════┬═══════╝
   ┌──────▼───────┐
   │ Buchhaltung  │   kennt "gebucht" und "vorgemerkt",
   └──────────────┘   nicht BOOK und PDNG
   ```

---

## Was dieses Beispiel zeigt

**Die Datenrichtung und die Abhängigkeitsrichtung sind dasselbe** — hier. Das ist nicht immer so: Bei einem Open Host Service liefert der Lieferant Daten und bestimmt trotzdem das Format.

**Interne Beziehungen sind meist Customer/Supplier.** Wo Leute im selben Haus sitzen, ist Absprache möglich, auch wenn sie nicht genutzt wird. Der Befund „Mitsprache brauche ich nicht" bedeutet nicht, dass keine möglich wäre.

**Bei Fremdsystemen ohne Einfluss lautet die Frage nicht, ob Conformist**, sondern ob es eine Grenze gibt. Conformist ist gesetzt; die Frage ist nur, wie weit es reicht.

**Die Map ist klein und trotzdem nützlich.** Vier Kästen genügen, um vor einer CAMT-Umstellung zu wissen, wen es trifft.

---

## Zum Vergleich: was ein Shared Kernel wäre

Angenommen, Mietverwaltung und Instandhaltung würden dieselbe Wohnungsklasse verwenden — mit Grundriss, Ausstattung, Zustand, Mieter, Vertragsdaten.

Dann müsste jede Änderung daran mit beiden abgestimmt werden, und beide müssten gemeinsam ausliefern.

**Der bessere Weg:** Zwei Modelle. Die Mietverwaltung kennt die Wohnung als Vertragsgegenstand, die Instandhaltung als Objekt mit Zustand. Was die Instandhaltung braucht — wer wohnt dort — kommt über eine Übersetzung.

Das kostet eine Schnittstelle und spart dauerhafte Koordination.
