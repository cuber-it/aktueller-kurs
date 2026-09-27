# Pro und Contra · Der schlanke Entwurf A gegenüber dem expliziten Entwurf B

Bewertet wird Entwurf A aus dem Lösungspapier: Funktionen für Einlesen und JSON, `NumValueDTO` mit Bereichsprüfung, `default_factory` für Vorgabewerte, eine Konfiguration als reiner Datenhalter und `test_wrapper` mit `ExitStack`. Verglichen wird mit Entwurf B, der Quellen, Leser und Sitzung als Objekte mit Protocols modelliert.

---

## Pro Entwurf A

**Jeder Baustein hat einen Change Request**
Vier Bausteine, vier Begründungen. AK7 ist ohne Streichungen erfüllt.

**Geteilter Vorgabewert und Folgefehler haben keine Ursache mehr**
Jeder Traktor bekommt eigene Werte. Eine leere Spalte lässt den Vorgabewert stehen. Ein Wert außerhalb des Bereichs fällt beim Einlesen auf. Die Simulation wird auch dann gestoppt, wenn das Sichern scheitert.

**Einlesen ist in Sekunden prüfbar**
`read_tractor` bekommt ein Dictionary und liefert einen Traktor. Kein Squish, kein Target, keine Datei.

**Der Umbau ist überschaubar**
Wer den Ausgangscode kennt, findet sich in Entwurf A sofort zurecht. Die Namen sind geblieben, die Aufgaben sind getrennt.

**Ein zweites Format ist eine Funktion**
Solange ein Format Datensätze als Dictionaries liefert, genügt eine Funktion wie `records_from_json`.

---

## Contra Entwurf A

**Formate mit eigenem Zustand passen schlecht**
Braucht eine künftige Quelle eine Verbindung, eine Anmeldung oder Paging, wird aus der Funktion doch eine Klasse. Entwurf B hätte dafür schon den Platz.

**Spaltennamen stehen im Code**
`read_tractor` kennt `tr_turn_radius` und `tr_wheelbase`. Für die übrigen Spalten des Testframeworks wächst die Funktion. Entwurf B sammelt die Zuordnung in `COLUMNS`, das ließe sich auch in A übernehmen.

**Target und Simulation haben keinen beschriebenen Vertrag**
Welche Methoden `test_wrapper` braucht, steht nur im Code. Wer ein Double schreibt, liest nach. In B stehen die Verträge in den Protocols.

**Die 64 Aufrufe von `get_test_config()` sind nicht gelöst**
Beide Entwürfe übergeben die Konfiguration. Für die vorhandenen Helper braucht es einen Übergang, den keiner der Entwürfe beschreibt.

---

## Bewertung

Entwurf A trägt die fünf Change Requests mit der kleinsten Zahl neuer Konzepte. Entwurf B trägt dieselben fünf und bereitet zusätzlich Quellen mit eigenem Zustand vor, die heute niemand ankündigt.

Gegenprobe – *nur die zwei Fehler beheben (`default_factory`, `ExitStack`), sonst nichts ändern, bleiben Nachteile?* Ja: CR1, CR2 und CR5 blieben offen. Das Einlesen stünde weiter in `__post_init__`, der Datensatz wäre weiter fest verdrahtet, und JSON aus der CI bräuchte einen zweiten Weg durch dieselbe Klasse.

**Die Grenzen:**

1. **Der Übergang für die übrigen 45 Konfigurationen ist offen.** Beide Entwürfe zeigen die Referenz, nicht den Weg dahin.
2. **Die globale Konfiguration verschwindet nicht von selbst.** Solange Helper `get_test_config()` aufrufen, muss es sie geben.
3. **Entwurf B ist kein falscher Entwurf.** Er ist für eine Zukunft gebaut, die im Ticket nicht vorkommt. Tritt sie ein, ist er die bessere Wahl.

---

## Diskussionsfragen

1. Welche Ankündigung würde Sie von Entwurf A zu Entwurf B wechseln lassen?
2. Wie stellen Sie die 64 Aufrufe von `get_test_config()` um, ohne alle Helper auf einmal zu ändern?
3. Würden Sie die Protocols aus Entwurf B trotzdem behalten, nur für mypy?
4. Welche Regel aus Aufgabe 10 würden Sie als erste verbindlich machen?
