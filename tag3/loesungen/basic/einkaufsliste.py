"""Referenzlösung: Obstliste ergänzen, Duplikate vermeiden und sortieren."""

from pathlib import Path

datei = Path(__file__).resolve().parents[3] / "materialien" / "beispiel.txt"
obst = datei.read_text(encoding="utf-8").splitlines()

artikel = input("Neuer Artikel (Enter beendet): ").strip()
vorhanden = {name.casefold() for name in obst}
if not artikel:
    print("Kein Artikel ergänzt.")
elif artikel.casefold() in vorhanden:
    print("Artikel ist bereits vorhanden.")
else:
    obst.append(artikel)
    print("Artikel ergänzt.")

for nummer, name in enumerate(sorted(obst, key=str.casefold), start=1):
    print(f"{nummer}. {name}")
