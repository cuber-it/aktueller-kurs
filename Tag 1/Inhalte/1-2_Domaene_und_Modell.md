# 1-2 · Domäne und Modell: Der Weg zum Modell

Ein Modell ist **eine Auswahl, kein Abbild**. Es bildet die Wirklichkeit nicht vollständig ab, sondern trifft eine Entscheidung darüber, was für einen bestimmten Zweck wichtig ist. Was weggelassen wird, gehört zum Modell.

Die zentrale Frage lautet deshalb nicht „ist das Modell vollständig", sondern: **beantwortet es die Fragen, die im Betrieb gestellt werden?**

- **Modell** – Eine zweckgebundene Vereinfachung der Domäne; es enthält, was für die zu lösenden Aufgaben nötig ist, und lässt den Rest weg.
- **Auswahl statt Abbild** – Zwei Modelle derselben Domäne können verschieden und beide richtig sein, wenn sie verschiedene Zwecke bedienen.
- **Fachliches Modell** – Trägt die Begriffe des Fachbereichs, kennt die Regeln und lässt ungültige Zustände nicht zu.
- **Datenmodell** – Beschreibt, wie Daten gespeichert werden; Normalisierung ist eine Eigenschaft der Speicherung, keine der Fachlichkeit.
- **Anämisches Modell** – Klassen mit Gettern und Settern ohne Verhalten; die Regeln liegen außerhalb, in Klassen wie `…Service` oder `…Manager`.
- **Regeln im Modell** – Eine Regel, die im Modell steht, gilt für jeden Zugriff; eine Regel außerhalb muss von jedem Aufrufer beachtet werden.
- **Ungültige Zustände** – Ein gutes Modell macht sie **unmöglich**, nicht nur unerwünscht; der Unterschied ist der zwischen Zusicherung und Absprache.
- **Der Weg zum Modell** – Aus Gesprächen mit dem Fachbereich, aus den Begriffen, die dort tatsächlich verwendet werden; nicht aus einem Datenbankschema abgeleitet.
- **Prüfbarkeit** – Ein Modell, das ein Fachvertreter nicht lesen kann, kann er auch nicht prüfen; Fehler bleiben, bis sie im Betrieb auffallen.
- **Warnzeichen** – Wahrheitswerte für fachliche Sachverhalte (`geprueft`), Zahlencodes für Zustände (`statusCode = 2`), technische Begriffe in Klassennamen (`Kopf`, `Position`, `Historie`).
- **Der Preis eines fachlichen Modells** – Auswertungen werden schwieriger, Korrekturen und Datenmigration brauchen eigene Wege; wo überwiegend gelesen wird, kann ein Datenmodell angemessen sein.
