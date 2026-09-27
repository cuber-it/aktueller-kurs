# Pro und Contra · Lücken melden statt überbrücken, dünne Step-Funktionen nur bei Bedarf

Bewertet wird der Vorschlag aus dem Lösungspapier: Jede Zeile auf einen vorhandenen Aufruf oder eine benannte Lücke; fehlende Elemente mit belegtem Real Name im UI-Modul; Step-Funktionen nur, wenn Szenarien ausführbar sein sollen.

---

## Pro

**Keine geratenen Namen**
Ein Button-Name nach Muster ohne Beleg kann nicht entstehen.

**Lücken werden zu Aufgaben fürs Framework**
Ein `[helper-missing]` ist ein Ticket, kein versteckter Fehler.

**Keine zweite Architektur**
Step-Funktionen rufen nur auf, Real Names bleiben in den UI-Modulen.

**Prüfungen einheitlich**
`UIElementTest` statt handgeschriebener `if`/`test.fail`.

---

## Contra

**Ein Test bleibt unfertig**
Bis der Button ergänzt ist, ist der Test nicht lauffähig.

**Spy braucht ein Target**
Ein Spy-Dump kostet ein Target und eine Rückfrage.

**Bestehende Tests weichen ab**
Der Testfall aus Material B prüft mit `test.passes`/`test.fail`; umgestellt wird bei Anlass.

---

## Bewertung

Der Vorschlag trägt, weil **eine Lücke, die als TODO auffällt, billiger ist als ein geratener Name, der erst im Lauf auffällt**.

Gegenprobe – *den Button nach Muster anlegen und im Lauf prüfen, bleiben Nachteile?* Ja: Ein falscher Name kostet einen Lauf, ein richtig geratener Name ist nicht belegt und bricht beim nächsten Umbau ohne Hinweis.

**Die Grenzen:**

1. **Lücken sammeln und abarbeiten**, sonst wachsen TODOs.
2. **Spy-Läufe bündeln**, etwa einmal je Menü statt je Test.
3. **Step-Funktionen nur für ausführbare Szenarien**, nicht zusätzlich zur Routing-Tabelle.

---

## Diskussionsfragen

1. Wer arbeitet `[helper-missing]`-Markierungen ab?
2. Wann würden Sie Szenarien ausführbar machen?
3. Wie viel darf ein Agent am Framework selbst ergänzen?
4. Welche bestehenden Tests prüfen noch mit `test.passes`/`test.fail`?
