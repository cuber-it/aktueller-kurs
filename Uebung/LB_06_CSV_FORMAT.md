# Lottobude – CSV-Format

## Zweck

Annahmestellen können mehrere Tippscheine in einer CSV-Datei liefern.

Das Format ist bewusst einfach und eignet sich für Übungen zu Syntax, Testdaten, Grenzwerten, Äquivalenzklassen und Fehlerbehandlung.

## Encoding

UTF-8.

## Trennzeichen

Semikolon (`;`).

## Header

Pflicht.

```text
ticket_id;draw_date;tip_no;n1;n2;n3;n4;n5;n6
```

## Beispiel

```csv
ticket_id;draw_date;tip_no;n1;n2;n3;n4;n5;n6
HH-10001;2026-08-15;1;3;7;12;18;23;31
HH-10001;2026-08-15;2;1;9;17;24;35;49
HH-10002;2026-08-15;1;4;11;19;22;33;41
```

## Semantik

### `ticket_id`

Externe Kennung des Tippscheins innerhalb der Annahmestelle.

Alle Zeilen mit derselben `ticket_id` gehören zu demselben Tippschein.

### `draw_date`

Datum der Ziehung im Format:

```text
YYYY-MM-DD
```

Die Ziehung muss im System existieren und für Tippabgaben offen sein.

### `tip_no`

Laufende Nummer des Tipps innerhalb eines Tippscheins.

Zulässiger Bereich:

```text
1..10
```

### `n1` bis `n6`

Die sechs Lottozahlen.

Regeln:

- Ganzzahl
- 1..49
- innerhalb des Tipps eindeutig

## Regeln pro Tippschein

- mindestens 1 Tipp
- höchstens 10 Tipps
- alle Zeilen haben dieselbe `ticket_id`
- alle Zeilen gehören zur selben Ziehung
- `tip_no` darf innerhalb eines Tippscheins nicht doppelt vorkommen

## Importergebnis

Ein Import liefert mindestens:

- Dateiname
- Gesamtzahl gelesener Datensätze
- Anzahl importierter Tipps
- Anzahl abgewiesener Datensätze
- Fehlerliste

Fehlerliste:

- Zeilennummer
- Fehlercode
- verständliche Fehlermeldung

## Beispielhafte Fehlercodes

- `CSV_HEADER_INVALID`
- `CSV_COLUMN_COUNT_INVALID`
- `DRAW_NOT_FOUND`
- `DRAW_CLOSED`
- `TIP_NUMBER_INVALID`
- `LOTTO_NUMBER_NOT_INTEGER`
- `LOTTO_NUMBER_OUT_OF_RANGE`
- `LOTTO_NUMBER_DUPLICATE`
- `TICKET_TOO_MANY_TIPS`

## Bewusst zu klärende Produktfragen

Diese Punkte sollen nicht automatisch durch den Parser „erfunden“ werden:

- Wird bei einer fehlerhaften Zeile die gesamte Datei verworfen oder teilweise importiert?
- Wie wird ein erneuter Upload derselben Datei behandelt?
- Ist `ticket_id` nur je Annahmestelle oder global eindeutig?
- Sind Leerzeichen um Felder erlaubt?
- Sind leere Zeilen erlaubt?
- Wie wird mit einer BOM umgegangen?
- Wie groß darf eine Datei sein?
