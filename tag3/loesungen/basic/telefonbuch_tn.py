telefonbuch = {
    "anna": "0151-111",
    "ben": "0151-222",
}

name = input("Welchen Namen suchst du? ").strip().casefold()
if name in telefonbuch:
    print(f"Telefonnummer von {name}: {telefonbuch[name]}")
else:
    print("Dieser Name wurde nicht gefunden.")

neuer_name = input("Neuer Name (Enter zum Überspringen): ").strip().casefold()

if not neuer_name:
    print("Kein neuer Kontakt.")
elif neuer_name in telefonbuch:
    print("Dieser Name ist bereits vorhanden.")
else:
    nummer = input("Telefonnummer: ").strip()
    if nummer:
        telefonbuch[neuer_name] = nummer
    else:
        print("Eine leere Telefonnummer wird nicht gespeichert.")

print("\nTelefonbuch:")
for name in sorted(telefonbuch):
    print(f"{name}: {telefonbuch[name]}")
