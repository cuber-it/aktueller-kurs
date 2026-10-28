MIN = 1
MAX = 11

dateiname = input("Dateiname: ")

with open(dateiname, "w") as datei:
    for reihe in range(MIN, MAX):
        print(f"\nTipp {reihe} – Eingabe 'ende' beendet das Programm.")

        eingabe = input("5 Zahlen aus 50: ")
        if eingabe.lower() == "ende":
            break

        eurozahlen = input("2 Zahlen aus 12: ")

        tipp = f"{eingabe.strip()} | {eurozahlen.strip()}"

        print(f"{reihe:>03}: {tipp}", file=datei)
        print(f"Tipp {reihe} gespeichert.")

print("Datei geschlossen.")
