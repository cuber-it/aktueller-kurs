"""Referenzlösung: Daten laden, vergleichen und mit Funktionsbausteinen auswerten."""

import json
from pathlib import Path
from tag4 import data_source as ds


def erstelle_bericht(daten):
    """Liefert Kennzahlen; Ausgabe und Dateizugriff gehören nicht in diese Funktion."""
    if not daten:
        raise ValueError("Für den Bericht sind Kursdaten erforderlich.")
    return {
        "anzahl": len(daten),
        "von": daten[0]["date"],
        "bis": daten[-1]["date"],
        "hoch": ds.hoch(daten),
        "tief": ds.tief(daten),
        "mittel": ds.mittel(daten),
        "aenderung_prozent": ds.gesamtrendite(daten),
    }


def main():
    """Verarbeitet die vorhandene CSV und legt eigene Ergebnisse unter ausgabe ab."""
    kurs = Path(__file__).resolve().parents[3]
    ausgabe = kurs / "tag4" / "ausgabe"
    ausgabe.mkdir(exist_ok=True)
    daten = ds.load_csv(kurs / "materialien" / "HistoricalQuotes.csv")
    ds.save_sql(daten, ausgabe / "quotes.db")
    rueckgelesen = ds.load_sql(ausgabe / "quotes.db")
    if daten != rueckgelesen:
        raise ValueError("CSV und Datenbank liefern unterschiedliche Datensätze.")
    bericht = erstelle_bericht(daten)
    with (ausgabe / "kursbericht.json").open("w", encoding="utf-8") as ziel:
        json.dump(bericht, ziel, indent=2, ensure_ascii=False)
    print("Datensätze:", bericht["anzahl"])
    print(f"Zeitraum: {bericht['von']} bis {bericht['bis']}")
    print(f"Hoch: {bericht['hoch']:.4f}; Tief: {bericht['tief']:.4f}")
    print(f"Mittel: {bericht['mittel']:.2f}")
    print(f"Änderung: {bericht['aenderung_prozent']:.2f} %")
    print("Bericht:", ausgabe / "kursbericht.json")


if __name__ == "__main__":
    main()
