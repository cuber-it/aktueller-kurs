# Lottobude – Domänenmodell

## Überblick

```text
Benutzer ───────┐
                ├──> Tippschein ──> Tipp
Annahmestelle ──┘        │
                         v
                      Ziehung
                         │
                         v
                     Auswertung
                         │
                         v
                       Gewinn

Annahmestelle ──> CSV-Import ──> Tippscheine
```

## Benutzer

Repräsentiert einen Spieler, der Tipps über die Weboberfläche abgibt.

Attribute:

- `id`
- `username`
- `display_name`
- `active`
- `created_at`

Beziehung:

- besitzt 0..n Tippscheine

## Annahmestelle

Repräsentiert eine Stelle, die Tipps gesammelt per CSV liefert.

Attribute:

- `id`
- `code`
- `name`
- `active`
- `created_at`

Beziehungen:

- besitzt 0..n CSV-Importe
- kann Quelle von 0..n Tippscheinen sein

## Ziehung

Attribute:

- `id`
- `draw_date`
- `status`
- `winning_numbers`
- `created_at`
- `completed_at`
- `evaluated_at`

Status:

```text
GEPLANT -> DURCHGEFUEHRT -> AUSGEWERTET
```

## Tippschein

Bündelt 1 bis 10 Tipps.

Attribute:

- `id`
- `draw_id`
- `user_id` oder `outlet_id`
- `source`
- `status`
- `created_at`
- `submitted_at`

Quelle:

- `WEB`
- `CSV`

Status:

```text
ENTWURF -> ABGEGEBEN -> AUSGEWERTET
```

CSV-Importe erzeugen Tippscheine unmittelbar im Status `ABGEGEBEN`.

## Tipp

Attribute:

- `id`
- `ticket_id`
- sechs Tippzahlen
- `created_at`

Invarianten:

- genau 6 Zahlen
- jede Zahl 1..49
- keine Zahl doppelt

## CSVImport

Attribute:

- `id`
- `outlet_id`
- `filename`
- `status`
- `total_records`
- `imported_records`
- `rejected_records`
- `started_at`
- `completed_at`

Status:

```text
HOCHGELADEN -> VALIDIERUNG -> IMPORTIERT
                         \-> FEHLER
```

## Importfehler

Attribute:

- `id`
- `import_id`
- `line_number`
- `error_code`
- `message`
- `raw_data`

## Auswertung

Attribute:

- `id`
- `tip_id`
- `draw_id`
- `hit_count`
- `prize_class`
- `prize_amount`
- `evaluated_at`

## Value Object: Lottozahlen

Eine Menge aus genau sechs unterschiedlichen Ganzzahlen im Bereich 1..49.

Die Reihenfolge hat fachlich keine Bedeutung.

## Wichtige Invarianten

1. Ein Tipp enthält genau sechs unterschiedliche Zahlen aus 1..49.
2. Ein Tippschein enthält mindestens einen und höchstens zehn Tipps.
3. Ein Tippschein gehört genau zu einer Ziehung.
4. Ein abgegebener Tippschein ist unveränderlich.
5. Eine Ziehung kann nur einmal durchgeführt werden.
6. Nur eine durchgeführte Ziehung kann ausgewertet werden.
7. Ein Tipp darf pro Ziehung nur einmal ausgewertet werden.
