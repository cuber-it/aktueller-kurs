# 2-7 · Legacy und Evolution

Die meisten Vorhaben beginnen nicht auf der grünen Wiese, sondern in einem gewachsenen System. Die Frage ist deshalb selten „wie baue ich das richtig", sondern: **wie komme ich dorthin, ohne den Betrieb anzuhalten?**

Die Antwort ist immer dieselbe Form: eine Grenze ziehen, dahinter neu bauen, schrittweise umleiten.

- **Anticorruption Layer** – Die Übersetzung zwischen Altsystem und neuem Modell. Verhindert, dass alte Begriffe ins neue Modell wandern.
- **In beide Richtungen** – Auch das Neue muss dem Alten liefern, solange beide laufen. Die Übersetzung ist keine Einbahnstraße.
- **Strangler Fig** – Neues wächst um das Alte herum; nach und nach wird umgeleitet, bis das Alte nichts mehr trägt und abgeschaltet wird.
- **Warum nicht am Stück** – Ein Neubau mit Umschaltung an einem Tag ist selten beherrschbar; das Alte ändert sich während des Baus weiter.
- **Wo anfangen** – Nicht beim Einfachsten, sondern dort, wo der Schmerz ist und die Grenze klar verläuft.
- **Die Core Domain zuerst** – Was den Unterschied macht, gehört zuerst befreit. Generic Subdomains lohnen den Aufwand selten.
- **Grenzen finden im Bestand** – Wo eine Formulierung wechselt, wo eine Abteilung endet, wo Daten nur in eine Richtung fließen.
- **Beides läuft eine Zeit lang** – Doppelte Pflege, doppelte Fehlerquellen, ein Weg zurück. Das ist der Preis und muss eingeplant sein.
- **Der Umschaltpunkt** – Vorab festlegen, woran erkennbar ist, dass das Neue trägt. Ohne Kriterium läuft beides dauerhaft weiter.
- **Häufiger Fehler** – Anbau ohne Grenze. Dann wandern die alten Begriffe mit, und das Neue ist nach zwei Jahren wie das Alte.
- **Zweiter Fehler** – Alles auf einmal ablösen wollen. Das Vorhaben wird zu groß, verliert Rückhalt und wird abgebrochen.
- **Was DDD hier beiträgt** – Kontextgrenzen sind die Schnittlinien für die Ablösung. Wer sie kennt, weiß, wo er trennen kann.

---

## Abschluss · Was bleibt

- **Die Sprache ist der Anfang.** Wo Begriffe unklar sind, hilft kein Muster.
- **Grenzen entstehen dort, wo die Bedeutung wechselt.** Nicht am Organigramm.
- **Wichtig und unterscheidend sind zweierlei.** Aufwand gehört in die Core Domain.
- **Ein Modell ist eine Auswahl.** Für einen Zweck, nicht für alle.
- **Konsistenz kostet.** Was zusammen gültig bleiben muss, muss zusammen geändert werden.
- **DDD ist kein Werkzeugkasten, den man abarbeitet.** Es ist eine Art, Fragen zu stellen.
