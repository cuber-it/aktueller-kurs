"""Kursdaten aus CSV oder SQLite laden und mit Funktionen auswerten.

Datensatz: {"date": "YYYY-MM-DD", "close": Zahl, "volume": ganze Zahl}.
Die Ladefunktionen liefern nach Datum aufsteigend sortierte Datensätze.
Kennzahlen bleiben ungerundet; die Ausgabe entscheidet über die Darstellung.
"""

from contextlib import closing
import csv
from datetime import datetime
from pathlib import Path
import sqlite3


def load_csv(pfad):
    """Liest das Format von HistoricalQuotes.csv; bereinigt Datum und Zahlen."""
    daten = []
    with Path(pfad).open(encoding="utf-8", newline="") as quelle:
        for zeile in csv.DictReader(quelle, skipinitialspace=True):
            datum_text = zeile["Date"].strip()
            datum = datetime.strptime(datum_text, "%m/%d/%Y").date()
            preis_text = zeile["Close/Last"].strip().removeprefix("$")
            datensatz = {
                "date": datum.isoformat(),
                "close": float(preis_text),
                "volume": int(zeile["Volume"]),
            }
            daten.append(datensatz)
    # lambda liefert für jeden Datensatz das Datum als Sortierschlüssel.
    return sorted(daten, key=lambda tag: tag["date"])


def load_sql(pfad):
    """Liest die Tabelle quotes; eine fehlende Datenbank erzeugt FileNotFoundError."""
    pfad = Path(pfad)
    if not pfad.is_file():
        raise FileNotFoundError(pfad)
    with closing(sqlite3.connect(pfad)) as verbindung:
        verbindung.row_factory = sqlite3.Row
        zeilen = verbindung.execute(
            "SELECT date, close, volume FROM quotes ORDER BY date"
        )
        return [dict(zeile) for zeile in zeilen]


def save_sql(daten, pfad):
    """Ersetzt den Inhalt der Tabelle quotes durch die übergebenen Datensätze."""
    with closing(sqlite3.connect(pfad)) as verbindung:
        with verbindung:
            verbindung.execute(
                "CREATE TABLE IF NOT EXISTS quotes ("
                "date TEXT PRIMARY KEY NOT NULL, close REAL NOT NULL, volume INTEGER NOT NULL)"
            )
            verbindung.execute("DELETE FROM quotes")
            verbindung.executemany(
                "INSERT INTO quotes (date, close, volume) VALUES (:date, :close, :volume)",
                daten,
            )


def load(quelle, pfad):
    """Lädt aus 'csv' oder 'sql'; andere Kennungen erzeugen ValueError."""
    if quelle == "csv":
        return load_csv(pfad)
    if quelle == "sql":
        return load_sql(pfad)
    raise ValueError("Die Quelle muss csv oder sql sein.")


def closes(daten):
    """Liefert die Schlusskurse als neue Liste."""
    return [tag["close"] for tag in daten]


def zeitraum(daten, von, bis):
    """Filtert inklusive beider ISO-Datumsgrenzen; vertauschte Grenzen sind ungültig."""
    if von > bis:
        raise ValueError("Der Beginn darf nicht nach dem Ende liegen.")
    return [tag for tag in daten if von <= tag["date"] <= bis]


def hoch(daten):
    """Liefert den höchsten Schlusskurs; bei leeren Daten entsteht ValueError."""
    return max(closes(daten))


def tief(daten):
    """Liefert den niedrigsten Schlusskurs; bei leeren Daten entsteht ValueError."""
    return min(closes(daten))


def mittel(daten):
    """Liefert den ungerundeten Mittelwert; leere Daten erzeugen ValueError."""
    werte = closes(daten)
    if not werte:
        raise ValueError("Für den Mittelwert sind Kursdaten erforderlich.")
    return sum(werte) / len(werte)


def rendite(kurs_alt, kurs_neu):
    """Liefert die Änderung in Prozent; der Ausgangskurs muss positiv sein."""
    if kurs_alt <= 0:
        raise ValueError("Der Ausgangskurs muss größer als 0 sein.")
    return (kurs_neu - kurs_alt) / kurs_alt * 100


def gesamtrendite(daten):
    """Vergleicht letzten und ersten Kurs; erwartet zeitlich aufsteigende Daten."""
    if not daten:
        raise ValueError("Für die Änderung sind Kursdaten erforderlich.")
    return rendite(daten[0]["close"], daten[-1]["close"])


def sma(daten, fenster):
    """Liefert (Datum, Mittelwert)-Paare; das Datum gehört zum Fensterende.

    fenster muss eine positive ganze Zahl sein. Bei einem größeren Fenster
    als der Datenreihe ist das Ergebnis leer.
    """
    if type(fenster) is not int or fenster < 1:
        raise ValueError("Das Fenster muss eine positive ganze Zahl sein.")
    kurse = closes(daten)
    ergebnis = []
    for start in range(len(kurse) - fenster + 1):
        ende = start + fenster
        fensterkurse = kurse[start:ende]
        mittelwert = sum(fensterkurse) / fenster
        letzter_tag = daten[ende - 1]["date"]
        ergebnis.append((letzter_tag, mittelwert))
    return ergebnis


def tagesveraenderung(daten):
    """Liefert (Datum, Prozentänderung)-Paare ab dem zweiten Datensatz."""
    ergebnis = []
    for vortag, aktueller_tag in zip(daten, daten[1:]):
        aenderung = rendite(vortag["close"], aktueller_tag["close"])
        ergebnis.append((aktueller_tag["date"], aenderung))
    return ergebnis


def bester_tag(daten):
    """Liefert den Datensatz mit dem höchsten Schlusskurs; bei Gleichstand den ersten."""
    return max(daten, key=lambda tag: tag["close"])


def groesster_tagesgewinn(daten):
    """Liefert (Datum, Änderung); mindestens zwei Datensätze sind erforderlich."""
    aenderungen = tagesveraenderung(daten)
    if not aenderungen:
        raise ValueError("Mindestens zwei Kurstage sind erforderlich.")
    return max(aenderungen, key=lambda paar: paar[1])
