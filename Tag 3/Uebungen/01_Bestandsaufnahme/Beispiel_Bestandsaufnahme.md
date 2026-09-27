# Beispiel · Wer setzt welche Regel durch? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Team pflegt die Übersetzungsdateien einer App mit einem Coding-Agenten. Der Agent liest neue Texte aus dem Code, übersetzt sie in fünf Sprachen, schreibt die Dateien, prüft sie und öffnet einen Pull Request.

Regeln:

| Nr. | Regel |
|---|---|
| U1 | Keine bestehende Übersetzung überschreiben, die ein Mensch freigegeben hat. |
| U2 | Platzhalter wie `{name}` unverändert übernehmen. |
| U3 | Rechtstexte nie übersetzen, sondern markieren. |
| U4 | Vor dem Pull Request die App-Tests laufen lassen. |

---

## Schritt 1 · Landkarte

```text
neuer Text im Code → Agent übersetzt → schreibt Dateien → prüft → Pull Request → Mensch reviewt ◆
```

---

## Schritt 2 · Durchsetzung

| Regel | heute | Folge eines Verstoßes |
|---|---|---|
| U1 | Modell | freigegebene Übersetzung verloren, fällt im Review vielleicht nicht auf |
| U2 | Prüfung im Build (Platzhalter-Vergleich) | Build rot |
| U3 | Modell | Rechtstext maschinell übersetzt, rechtliches Risiko |
| U4 | CI | Pull Request rot |

---

## Schritt 3 · Kandidaten

- **U1 technisch:** Freigegebene Einträge tragen ein Kennzeichen; eine Prüfung verbietet Änderungen daran.
- **U3 technisch:** Rechtstexte liegen in einer eigenen Datei; der Agent hat darauf keine Schreibrechte.
- **U2, U4** sind bereits technisch.

---

## Was dieses Beispiel zeigt

**Die gefährlichsten Regeln hingen am Modell.** Die harmloseren waren längst technisch geprüft, weil sie leicht zu prüfen waren.

**Die Folge entscheidet, nicht die Häufigkeit.** U3 wird selten verletzt, aber teuer.

**Technische Durchsetzung heißt oft: weniger erlauben.** Schreibrechte entziehen ist einfacher als eine Regel prüfen.
