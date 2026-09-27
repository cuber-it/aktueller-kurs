# Beispiel · Was prüft dieser Testfall wirklich? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Testfall für das Terminal eines Fahrradverleihs:

| Schritt | Erwartetes Ergebnis |
|---|---|
| Kundenkarte vorhalten | Startbildschirm mit Namen |
| Rad an Station 3 wählen | Rad 3 ist entriegelt |
| Rad zurückstellen | Ausleihe beendet |

---

## Schritt 1 · Gherkin

```gherkin
Scenario: Rad ausleihen und zurückgeben
  Given eine gültige Kundenkarte ohne offene Ausleihe
  And an Station 3 steht ein verfügbares Rad
  When ich die Karte vorhalte und Station 3 wähle
  Then wird das Schloss an Station 3 geöffnet
  And im Kundenkonto steht eine offene Ausleihe für Rad 3
  When ich das Rad an Station 3 zurückstelle
  Then ist das Schloss geschlossen
  And im Kundenkonto ist die Ausleihe beendet und abgerechnet
```

---

## Schritt 2 · Was sichtbar wurde

| Befund | im Testfall |
|---|---|
| „Ausleihe beendet“ ist nur im Konto beobachtbar | Anzeige am Terminal geprüft |
| „ohne offene Ausleihe“ ist Vorbedingung | nicht genannt |
| Station 3 leer, Karte gesperrt, Rückgabe an anderer Station | fehlen |
| Abrechnung | nicht erwähnt |

---

## Schritt 3 · Fragen an die Fachseite

1. Darf eine Karte zwei Räder gleichzeitig leihen?
2. Ab wann wird abgerechnet: Entriegeln oder Losfahren?

---

## Was dieses Beispiel zeigt

**Then zwingt zur Beobachtung.** „Ausleihe beendet“ wird zur Aussage über das Konto.

**Given zwingt zum Ausgangszustand.** Eine Karte mit offener Ausleihe hätte das Ergebnis verfälscht.

**Die Fragen entstehen vor dem Code.** Nach der Automatisierung wären sie als Testfehler aufgetaucht.
