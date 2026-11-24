# Tag 4 – Standardbibliothek kombinieren
# pathlib, re und Counter übernehmen Pfade, Textextraktion und Häufigkeiten.

from collections import Counter
from pathlib import Path
import re


def zaehle_stufen(pfad):
    """Zählt Logstufen im Format der Datei small_sample.log."""
    anzahl = Counter()
    with Path(pfad).open(encoding="utf-8") as quelle:
        for zeile in quelle:
            treffer = re.search(r"\s([A-Z]+)\s*:", zeile)
            if treffer:
                anzahl[treffer.group(1)] += 1
    return anzahl


def main():
    """Wertet die vorhandene Beispieldatei aus."""
    pfad = Path(__file__).resolve().parent.parent / "materialien" / "small_sample.log"
    anzahl = zaehle_stufen(pfad)
    for stufe in sorted(anzahl):
        print(f"{stufe}: {anzahl[stufe]}")
    print("Erkannte Logzeilen:", sum(anzahl.values()))


if __name__ == "__main__":
    main()
