"""Referenzlösung: Nummer nachschlagen und einen neuen Eintrag ergänzen."""

telefonbuch = {"anna": "0151-111", "ben": "0151-222"}

name = input("Gesuchter Name: ").strip().casefold()
nummer = telefonbuch.get(name)
if nummer is None:
    print("Name nicht gefunden.")
else:
    print(f"Nummer von {name}: {nummer}")

name = input("Neuer Name (Enter beendet): ").strip().casefold()
if name in telefonbuch:
    print("Name ist bereits vorhanden; Nummer bleibt erhalten.")
elif name:
    nummer = input("Telefonnummer: ").strip()
    if nummer:
        telefonbuch[name] = nummer
    else:
        print("Kein Eintrag ohne Telefonnummer.")

for name, nummer in sorted(telefonbuch.items()):
    print(f"{name}: {nummer}")
