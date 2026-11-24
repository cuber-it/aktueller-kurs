"""Referenzlösung: Noten auswerten und alle besten Ergebnisse berücksichtigen."""

schueler = [
    {"name": "Anna", "note": 2},
    {"name": "Ben", "note": 5},
    {"name": "Cem", "note": 1},
    {"name": "Dora", "note": 4},
    {"name": "Emil", "note": 5},
]

noten = [person["note"] for person in schueler]
beste_note = min(noten)
beste = [person["name"] for person in schueler if person["note"] == beste_note]
gruppen = {"bestanden": [], "durchgefallen": []}
for person in schueler:
    gruppe = "bestanden" if person["note"] <= 4 else "durchgefallen"
    gruppen[gruppe].append(person["name"])

print(f"Durchschnitt: {sum(noten) / len(noten):.2f}")
print(f"Beste Note: {beste_note} ({', '.join(beste)})")
print("Bestanden:", ", ".join(gruppen["bestanden"]))
print("Durchgefallen:", ", ".join(gruppen["durchgefallen"]))
