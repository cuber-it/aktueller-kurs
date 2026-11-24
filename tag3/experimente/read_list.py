# Experiment – Text in Zeichen, Wörter oder Zeilen zerlegen
# Die Datei wird einmal gelesen und anschließend unterschiedlich betrachtet.

from pathlib import Path

datei = Path(__file__).resolve().parents[2] / "materialien" / "small_sample.log"
inhalt = datei.read_text(encoding="utf-8")

zeichen = list(inhalt)
woerter = inhalt.split()
zeilen = inhalt.splitlines()
print("Zeichen:", len(zeichen))
print("Wörter:", len(woerter))
print("Zeilen:", len(zeilen))
print("Erste Zeile:", zeilen[0])
