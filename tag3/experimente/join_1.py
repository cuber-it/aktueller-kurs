# Experiment – Zeilen als einen Text darstellen
# join() verbindet die gelesenen Obstnamen mit einem gewählten Trenner.

from pathlib import Path

datei = Path(__file__).resolve().parents[2] / "materialien" / "beispiel.txt"
obst = datei.read_text(encoding="utf-8").splitlines()
print(", ".join(obst))
