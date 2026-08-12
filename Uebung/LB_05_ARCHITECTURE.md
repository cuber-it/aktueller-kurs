# Lottobude – Zielarchitektur

## Ziel

Die Architektur soll klein, verständlich und für QA-Übungen transparent sein. Sie ist keine Demonstration maximaler Architekturkomplexität.

## Kontext

```text
                    +----------------+
                    |    Browser     |
                    +-------+--------+
                            |
                            v
+------------+       +------+-------+
| CSV-Datei  | ----> |  Web / REST  |
+------------+       +------+-------+
                            |
                            v
                    +-------+--------+
                    | Application    |
                    | Services       |
                    +---+---------+--+
                        |         |
               +--------+         +----------+
               v                              v
      +--------+---------+          +---------+--------+
      | Domain / Rules   |          | CSV Import       |
      +--------+---------+          +---------+--------+
               |                              |
               +---------------+--------------+
                               |
                               v
                      +--------+---------+
                      | Persistence      |
                      | SQLAlchemy       |
                      +--------+---------+
                               |
                               v
                      +--------+---------+
                      | PostgreSQL       |
                      +------------------+
```

## Komponenten

### Web UI

Aufgaben:

- Tippscheine erfassen
- Tipps anzeigen
- CSV hochladen
- Importergebnisse anzeigen
- Ziehungen verwalten
- Ergebnisse anzeigen

Die UI soll funktional und bewusst nicht überentwickelt sein.

### REST API

Die wesentlichen fachlichen Funktionen sollen auch über HTTP-Endpunkte erreichbar sein.

Beispielhafte Ressourcen:

- `/api/users`
- `/api/draws`
- `/api/tickets`
- `/api/tips`
- `/api/imports`
- `/api/results`

FastAPI stellt zusätzlich OpenAPI-Dokumentation bereit.

### Application Services

Vorgesehene Services:

- `TicketService`
- `TipValidationService`
- `CsvImportService`
- `DrawService`
- `EvaluationService`
- `TrainingResetService`

### Persistenz

SQLAlchemy mit PostgreSQL.

Die Persistenzschicht soll so gestaltet sein, dass Fachlogik nicht von SQLAlchemy-Details abhängig wird.

## Testbarkeit

### Unit Tests

Geeignet für:

- Tippvalidierung
- Trefferermittlung
- Gewinnberechnung
- Zustandsregeln
- CSV-Feldvalidierung

### Integration Tests

Geeignet für:

- Service + Repository
- CSV-Parser + Validierung
- Datenbanktransaktionen
- REST API + Datenbank

### System/API Tests

Geeignet für:

- vollständiger CSV-Import
- Tippscheinabgabe
- Ziehung und Auswertung
- Fehlerbehandlung

### GUI Tests

Geeignet für wenige kritische End-to-End-Flows:

- Tipp abgeben
- CSV importieren
- Ergebnis ansehen

## Deployment

Vorgesehen:

```text
Internet
   |
 HTTPS
   |
Reverse Proxy
   |
Docker Compose
   +-- lottobude-app
   +-- postgres
```

Optional kann ein Admin-/Reset-Endpunkt nur intern oder durch separate Authentifizierung erreichbar sein.

## Konfiguration

Alle umgebungsabhängigen Werte über Environment-Variablen:

- Datenbank
- Base URL
- Admin-/Reset-Credential
- Logging
- Trainingsmodus

Keine Secrets im Repository.

## Reset

Der Reset muss:

1. laufende Daten entfernen,
2. Schema in definierten Zustand bringen,
3. Fixtures laden,
4. reproduzierbare Ausgangsdaten herstellen.

Der Reset darf die Anwendung nicht neu bauen müssen.
