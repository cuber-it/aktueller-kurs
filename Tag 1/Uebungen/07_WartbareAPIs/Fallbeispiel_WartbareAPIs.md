# Fallbeispiel · Ein gemeinsames Framework ohne öffentliche Schnittstelle

**Situationstyp:** Gemeinsam genutzter Code hat keine erkennbare öffentliche Schnittstelle. Jede interne Änderung kann Nutzer brechen, von denen die Autoren nichts wissen.

---

## Ausgangslage

Vier Testsuiten (Universal Terminal, AEF-Konformität, Einstellungen, Section Control) werden von vier Teams gepflegt. Seit 2020 fassen sie wiederkehrende Hilfsfunktionen in einem gemeinsamen Testframework zusammen, das ein Plattformteam pflegt. Die Suite-Teams übernehmen neue Versionen im Mittel nach drei Wochen.

## Wie es gewachsen ist

Aus `common.py` wurden `utils.py`, `helpers.py`, `test_helpers.py` und `screens.py`, aufgeteilt nach dem Zeitpunkt, zu dem etwas dazukam. Heute rund 2.100 Zeilen in fünf Modulen. Eine Wiki-Seite „Public API“ von 2022 nennt 14 Funktionen, fünf davon gibt es nicht mehr. Die Suite-Teams suchen in der IDE, was sie brauchen.

## Was auffällt

**Der Unterstrich ist bekannt, seine Nutzer nicht.** `ResultCollector._write_json` gilt als intern, drei Suite-Teams rufen es direkt auf. Eine Suche über alle Repositories findet 87 Zugriffe auf Namen mit Unterstrich in 41 Dateien.

**Die Zugriffe haben Gründe.** Eigene Exportziele, formatierte Laufzeiten, die Liste der fehlgeschlagenen Tests. Für ihren Zweck gibt es keinen öffentlichen Weg.

**Ein Team verändert Ergebnisse nachträglich.** Es setzt über das interne Dictionary den Status einzelner Tests auf `"flaky"`.

**Die Reviews haben keine Zeit für solche Fragen.** Von 420 Review-Kommentaren im letzten Quartal betrafen 160 Formatierung, Importreihenfolge und Leerzeilen.

**Namen und Docstrings helfen nicht weiter.** `add`, `proc`, `get_results`; Docstrings wie „Adds a result.“

## Naheliegende Ansätze

**Eine Rundmail „keine Methoden mit Unterstrich verwenden“.** Die Rückfrage lautet, wie man den Export sonst schreiben soll.

**Die Wiki-Seite aktualisieren.** Sie veraltet, sobald die nächste Funktion umbenannt wird.

## Diskussionsfragen

1. Die Unterstrich-Konvention wird eingehalten. Warum schützt sie die Nutzer nicht?
2. Wessen Aufgabe wäre es, die Gründe für die Zugriffe zu kennen?
3. Warum veraltet eine Wiki-Seite über die API, während der Code sich weiterentwickelt?
4. Wo haben Sie so etwas?
