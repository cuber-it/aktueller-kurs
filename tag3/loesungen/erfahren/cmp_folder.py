"""Referenzlösung: Dateinamen und Dateiinhalte zweier Ordner vergleichen."""

import filecmp
import hashlib
from pathlib import Path

ordner_a = Path(input("Ordner A: ").strip()).expanduser().resolve()
ordner_b = Path(input("Ordner B: ").strip()).expanduser().resolve()
if not ordner_a.is_dir() or not ordner_b.is_dir():
    raise SystemExit("Beide Pfade müssen vorhandene Ordner sein.")
if ordner_a == ordner_b:
    raise SystemExit("Bitte zwei unterschiedliche Ordner angeben.")

dateien = []
for ordner in (ordner_a, ordner_b):
    nach_name = {}
    nach_inhalt = {}
    for pfad in sorted(ordner.iterdir()):
        if not pfad.is_file():
            continue
        pruefsumme = hashlib.sha256()
        with pfad.open("rb") as quelle:
            while block := quelle.read(65536):
                pruefsumme.update(block)
        nach_name[pfad.name] = pfad
        nach_inhalt.setdefault(pruefsumme.hexdigest(), []).append(pfad.name)
    dateien.append((nach_name, nach_inhalt))

namen_a, inhalte_a = dateien[0]
namen_b, inhalte_b = dateien[1]
print("Gleiche Namen:")
for name in sorted(namen_a.keys() & namen_b.keys()):
    print(name)

print("Gleicher Inhalt (SHA-256):")
for pruefsumme in sorted(inhalte_a.keys() & inhalte_b.keys()):
    for name_a in inhalte_a[pruefsumme]:
        for name_b in inhalte_b[pruefsumme]:
            gleicher_inhalt = filecmp.cmp(
                namen_a[name_a], namen_b[name_b], shallow=False
            )
            if gleicher_inhalt:
                print(f"{name_a} | {name_b}")
