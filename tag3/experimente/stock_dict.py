# Experiment – CSV-Zeilen als Datensätze lesen
# Der CSV-Parser behandelt die Felder; Preise und Volumen werden Zahlen.

import csv
from pathlib import Path

datei = Path(__file__).resolve().parents[2] / "materialien" / "HistoricalQuotes.csv"
kurse = []
with datei.open(encoding="utf-8", newline="") as quelle:
    for zeile in csv.DictReader(quelle, skipinitialspace=True):
        preis_text = zeile["Close/Last"].strip().removeprefix("$")
        kurse.append({
            "date": zeile["Date"].strip(),
            "close": float(preis_text),
            "volume": int(zeile["Volume"]),
        })

print("Datensätze:", len(kurse))
print("Erster Datensatz:", kurse[0])
schlusskurse = [tag["close"] for tag in kurse]
print(f"Minimum: {min(schlusskurse):.4f}")
print(f"Maximum: {max(schlusskurse):.4f}")
# Die Datumstexte behalten hier das US-Format der Quelldatei.
