# Denkmodell · Die richtige Prüfart für eine Regel

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### In Regeln und Prüfungen

| Signal | Beispiel |
|---|---|
| Prüfung nach Namen, Regel nach Verhalten | C004 und Umschalter |
| Regel nur in der Abschlussliste | Punkt 6c |
| dokumentiertes Beispiel ohne Test der Prüfung | `layout_manager_btn` |
| Regeln mit Begriffen wie „angemessen“, „nur nötig“ | Urteil nötig |

### Im Ablauf

| Signal | Konkret |
|---|---|
| Fehler trotz sauberem Prüflauf | „wrong“-Variante von `click_and_wait` ohne Befund |
| Prüfausgabe wird ignoriert | zu viele Warnungen |
| KI-Review-Ergebnisse versickern | Kommentare im Chat |

---

## Stufe 2 · Erkenntnisse

**1. Was eine Maschine sicher entscheiden kann, soll sie entscheiden.**
Schnell, reproduzierbar, ohne Modell.

**2. Eine unsichere Prüfung ist schlimmer als keine.**
Fehlalarme erziehen dazu, die Ausgabe zu ignorieren.

**3. KI-Review braucht einen Maßstab.**
„Prüfe gegen Regel X aus Dokument Y“, nicht „prüfe die Qualität“.

**4. Die beste Prüfung ist eine, die niemand braucht.**
Eine API, die den Fehler nicht zulässt, ersetzt Regel, Prüfung und Review.

**Was gesucht wird:** für jede Regel die günstigste Prüfart, die sicher greift.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **API ändern** | der Fehler sich im Framework ausschließen lässt |
| **statische Prüfung** | der Verstoß an der Form erkennbar ist |
| **statische Prüfung mit Liste** | der Verstoß an bekannten Namen erkennbar ist |
| **KI-Review gegen Standard** | Urteil über Absicht nötig ist |
| **keine Prüfung** | die Folge gering ist |

---

## Stufe 4 · Entscheidung

### Frage 1 — Lässt sich der Fehler im Framework ausschließen?

- **Ja** → API ändern, Prüfung übergangsweise.

### Frage 2 — Ist der Verstoß an der Form sicher erkennbar?

- **Ja** → statische Prüfung, still bei Unsicherheit.
- **Nein** → weiter.

### Frage 3 — Braucht es Urteil?

- **Ja** → KI-Review mit Regel und Quelle, Ergebnis an einem festen Ort.

---

## Der Denkweg auf einen Blick

```
Regel
   ↓
im Framework ausschließbar?      ja → API
   ↓ nein
an der Form sicher erkennbar?    ja → statisch, still bei Unsicherheit
   ↓ nein
KI-Review gegen Standard, Ergebnis dokumentiert
```

---

## Die eine Prüffrage

> **Kann eine Maschine das sicher entscheiden, oder braucht es Urteil?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Schlägt die Prüfung beim dokumentierten Beispiel nicht an? | Prüfung falsch gebaut |
| Meldet sie mehr als eine Warnung je Test im Schnitt? | wird ignoriert |
| Nennt der Review-Auftrag keine Regel? | Geschmack des Modells |

---

## Wenn die Entscheidung steht

**Prüfungen gegen Beispiele testen.** Jedes „wrong“ aus den Coding-Regeln ist ein Testfall für die Prüfung.

**KI-Review in den Merge Request.** Als Kommentar mit Regelbezug.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| KI-Review mit Linter | ein Linter ist reproduzierbar |
| Warnung mit Fehler | eine Warnung blockiert nicht |
| Namenskonvention mit Verhalten | ein Name kann lügen |
