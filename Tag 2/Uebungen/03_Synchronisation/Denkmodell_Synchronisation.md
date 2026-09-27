# Denkmodell · Synchronisation auf die richtige Ebene legen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| feste Wartezeit nach Aktionen | `squish.snooze(1)` |
| Schleife aus Klick und kurzem Warten | `click_and_wait` |
| Lesen mit vorheriger Existenzprüfung | `if self.exists(): …` |
| Wartezeit als Parameter eines Helpers | `snooze_time=8` |
| Meldungen ohne Objektbezug | „Found: None“ |

### Im Nachtlauf

| Signal | Konkret |
|---|---|
| sporadische Fehlschläge nach Hardwarewechsel | langsameres Terminal |
| Tests werden durch zusätzliches `snooze` grün | „Found: None“ verschwindet |
| längere Laufzeit ohne neue Tests | zusätzliche Wartezeiten |

---

## Stufe 2 · Erkenntnisse

**1. Warten auf Zeit ist eine Annahme über die Umgebung.**
Warten auf einen Zustand ist unabhängig davon, wie schnell die Umgebung ist.

**2. Eine Wiederholung braucht eine Bedingung, die den Erfolg der Aktion beobachtet.**
Beobachtet sie etwas anderes, kann sie eine angekommene Aktion wiederholen.

**3. Lesen ist auch eine Interaktion.**
Wer liest, erwartet ein vorhandenes Objekt. Fehlt es, ist das eine andere Aussage als ein falscher Wert.

**4. Synchronisation gehört dorthin, wo der Zustand bekannt ist.**
Klickbarkeit kennt das Control, „Menü ist offen“ das Screen Object des Menüs.

**Was gesucht wird:** für jede Wartestelle der Zustand, auf den eigentlich gewartet wird, und die Ebene, die ihn kennt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **einmal klicken, dann auf Zustand warten** | das Ziel abfragbar ist |
| **klicken, bis der geklickte Control verschwindet** | Klicks verloren gehen können und der Control nach Erfolg verschwindet |
| **Lesen mit Warten** | ein Wert direkt nach einer Navigation gelesen wird |
| **begründetes `snooze`** | es keinen abfragbaren Zustand gibt, etwa eine Animation |
| **Timeout erhöhen** | die AUT tatsächlich länger braucht und der Zustand abgefragt wird |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es einen abfragbaren Zustand?

- **Ja** → darauf warten. Weiter mit Frage 2.
- **Nein** → begründetes `snooze`, eingetragen in die Tabelle der Ausnahmen.

### Frage 2 — Wird wiederholt?

- **Nein** → einmal handeln, dann warten.
- **Ja** → beobachtet die Bedingung den Erfolg dieser Aktion? Nein → nicht wiederholen.

### Frage 3 — Wer kennt den Zustand?

- Element → Control
- Komponente (Liste geladen, Overlay offen) → Component
- Menü gewechselt → Screen Object

### Frage 4 — Was steht in der Meldung, wenn der Zustand nicht eintritt?

- Objekt, Real Name, auslösende Aktion.

---

## Der Denkweg auf einen Blick

```
Wartestelle
        ↓
Abfragbarer Zustand?                  nein → begründetes snooze (Policy)
        ↓ ja
Wiederholung?                         ja → beobachtet sie den Erfolg? nein → einmal
        ↓
Wer kennt den Zustand?  →  Control / Component / Screen Object
        ↓
Meldung nennt Objekt und Aktion
```

---

## Die eine Prüffrage

> **Worauf genau wird hier gewartet, und wer kennt diesen Zustand?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wird ein Test durch ein zusätzliches `snooze` grün? | es fehlt ein Warten auf Zustand |
| Hilft ein längeres `iteration_delay`? | die Schwelle ist verschoben, nicht beseitigt |
| Klickt eine Schleife auf eine Quelle, die umschaltet? | Wiederholung kann schaden |
| Steht eine Gefahr nur als Regel für den Aufrufer in der Dokumentation? | Kandidat für eine sichere API |
| Meldet eine Prüfung `None` als Wert? | Lesen ohne Warten |

---

## Wenn die Entscheidung steht

**Schrittweise.** Erst `click_and_wait` und `get_property_value` umbauen, dann die `snooze` nach Klicks prüfen. Wird ein Test ohne `snooze` rot, zeigt er eine fehlende Wartebedingung.

**Coding-Regeln anpassen.** Beispiele in den Regeln werden kopiert, auch von Werkzeugen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Robustheit mit Wiederholen | wiederholen ist robust nur, wenn es den Erfolg beobachtet |
| `object.exists` mit Warten | `exists` prüft sofort |
| Timeout mit Wartezeit | ein Timeout endet beim Zustand, eine Wartezeit nie früher |
| grüner Test mit richtigem Test | ein `snooze` kann einen Fehler verdecken |
