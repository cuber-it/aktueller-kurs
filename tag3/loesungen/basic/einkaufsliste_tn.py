dateiname = r"materialien/beispiel.txt"
with open(dateiname, encoding="utf-8") as datei:
    artikel = [zeile.strip() for zeile in datei if zeile.strip()]
    # evtl kürzer: artikel = datei.read().splitlines()

neuer_artikel = input("Weiteren Artikel eingeben: ").strip()

if neuer_artikel and neuer_artikel.casefold() not in [name.casefold() for name in artikel]:
    artikel.append(neuer_artikel)

for nummer, name in enumerate(sorted(artikel, key=str.casefold), start=1):
    print(f"{nummer}. {name}")
