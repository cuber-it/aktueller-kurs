# Lottobude

## Zweck

**Lottobude** ist eine kleine, vollständige Webanwendung für einen QA-/Testdesign-Kurs.

Das System bildet einen vereinfachten Lotto-Spielbetrieb ab:

- Benutzer geben Tipps über eine Weboberfläche ab.
- Annahmestellen liefern Tipps gesammelt per CSV-Datei.
- Ziehungen werden durchgeführt.
- Abgegebene Tipps werden gegen die Gewinnzahlen ausgewertet.
- Gewinne werden ermittelt und gespeichert.
- Ergebnisse können anschließend eingesehen werden.

Die Anwendung ist bewusst überschaubar, enthält aber genügend fachliche und technische Tiefe für realistische Übungen zu Anforderungsanalyse, Testfallerstellung, Testdaten, Äquivalenzklassen, Grenzwerten, Entscheidungstabellen, Zuständen, Testorakeln, GUI-/API-/Datenbanktests, explorativem Testen und Testautomatisierung.

## Lotto-Variante

Für die Trainingsanwendung gilt ein vereinfachtes **6 aus 49**:

- Ein Tipp besteht aus genau 6 unterschiedlichen Zahlen.
- Zulässige Zahlen sind 1 bis 49.
- Ein Tippschein enthält 1 bis 10 Tipps.
- Ein Tippschein gehört genau zu einer Ziehung.
- Ein abgegebener Tippschein kann nicht mehr verändert werden.

Superzahl, Zusatzzahl, Spieleinsatz, Jackpot, Quotenberechnung und reale Lotto-Regularien gehören zunächst nicht zum Scope.

## Fachlicher Scope

### Benutzer

Ein Benutzer kann:

- sich anmelden,
- einen Tippschein anlegen,
- 1 bis 10 Tipps erfassen,
- einen Tippschein für eine Ziehung abgeben,
- eigene Tipps ansehen,
- nach der Auswertung Ergebnisse ansehen.

### Annahmestelle

Eine Annahmestelle kann:

- eine CSV-Datei mit Tippscheinen hochladen,
- das Importergebnis ansehen,
- fehlerhafte Datensätze erkennen,
- frühere Importe einsehen.

### Spielbetrieb

Der Spielbetrieb kann:

- Ziehungen anlegen,
- Gewinnzahlen erfassen,
- eine Ziehung abschließen,
- die Auswertung starten,
- Ergebnisse einsehen.

## Technischer Rahmen

Vorgesehener Stack:

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- einfache HTML/JavaScript-Weboberfläche
- REST API
- Docker / Docker Compose
- Reverse Proxy mit HTTPS

## Entwicklungsprinzipien

- Fachlogik gehört in Services bzw. Domänenlogik.
- Persistenz wird gekapselt.
- GUI und CSV-Import verwenden dieselbe fachliche Validierungslogik.
- REST-Endpunkte müssen für API-Tests nutzbar sein.
- Die Datenbank enthält nachvollziehbare Trainingszustände.
- Die Anwendung muss deterministisch zurücksetzbar sein.
- Produktanforderungen und absichtlich eingebaute Trainingsfehler werden getrennt dokumentiert.

## Dokumente

- `DOMAIN.md`
- `BUSINESS_RULES.md`
- `EPICS_AND_STORIES.md`
- `ARCHITECTURE.md`
- `CSV_FORMAT.md`
- `TRAINING_CONCEPT.md`

## Nicht im Scope

- echtes Geld
- Zahlungsanbieter
- reale Lotteriegesellschaften
- regulatorisch korrekte Glücksspielabwicklung
- komplexes Rollen-/Rechtesystem
- Hochverfügbarkeit
- horizontale Skalierung
