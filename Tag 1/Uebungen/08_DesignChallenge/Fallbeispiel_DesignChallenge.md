# Fallbeispiel · Eine Konfiguration, die alles selbst erledigt

**Situationstyp:** Ein Objekt, das ursprünglich nur Werte hielt, übernimmt nach und nach Einlesen, Auswahl und Registrierung. Jede Ergänzung war klein, zusammen erzeugen sie schwer auffindbare Fehler.

---

## Ausgangslage

312 Section-Control-Tests laufen nachts gegen eine Simulation, die je Rechner nur einmal laufen darf. Jeder Test fährt mit simulierten Traktoren eine Feldgrenze ab und prüft, wann das Terminal Teilbreiten schaltet. Seit 2020 gibt es je Test eine Konfigurationsklasse, anfangs mit wenigen Werten.

## Wie es gewachsen ist

Mit datengetriebenen Tests las die Konfiguration die TSV-Datei der Fachabteilung in `__post_init__` ein. Damit Hilfsfunktionen an die Konfiguration kommen, trägt sich jede in eine globale Variable ein; `get_test_config()` wird 64-mal aufgerufen. Traktoren sind `dataclass`es mit `NumValueDTO`-Feldern und Vorgabewerten direkt in der Klasse. Der gemeinsame Wrapper räumt im `finally` nacheinander auf: Testdaten sichern, Target aufräumen, Simulation stoppen.

## Was auffällt

**Die Traktoren teilen sich ihre Werte.** Der Vorgabewert eines `NumValueDTO` wird einmal beim Laden der Klasse erzeugt. Alle Traktoren bekommen dasselbe Objekt; eine leere Spalte übernimmt den Wert des vorherigen Testsatzes.

**Der Konstruktor gibt nicht zurück, was man übergibt.** `AbstractSectionControlTest(data_set="sc_set_3")` ergibt eine Konfiguration mit `with_sc_boundary`, weil `__post_init__` den Wert überschreibt.

**Die Grenzen stehen im Objekt, geprüft werden sie nicht.** `NumValueDTO` kennt `min` und `max`. Ein Wenderadius von 150 m fällt erst im Test auf.

**Ein gescheiterter Aufräumschritt verhindert alle weiteren.** Wirft das Sichern der Testdaten, laufen Target-Cleanup und Simulationsstopp nicht mehr. Die Simulation läuft weiter, alle folgenden Tests scheitern beim Start.

## Naheliegende Ansätze

**Die Simulation vor jedem Test hart beenden.** Weniger Folgefehler, langsamerer Lauf, die Ursache bleibt.

**Testdaten ohne leere Spalten.** Mit jeder neuen Spalte entstehen wieder leere Felder.

## Diskussionsfragen

1. Jede Ergänzung in `__post_init__` war einzeln sinnvoll. Wann hätte jemand eingreifen sollen?
2. Warum löst das harte Beenden der Simulation das Problem nicht?
3. Wessen Aufgabe ist es, mit leeren Spalten richtig umzugehen?
4. Wo haben Sie so etwas?
