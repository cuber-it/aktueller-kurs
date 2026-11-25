import json

rolo = []

while True:
    # Menu
    print("f -- Einträge finden")
    print("n -- neuer Eintrag")
    print("p -- alle anzeigen")
    print("s -- speichern (überschreibt!)")
    print("l -- laden (löscht Inhalte)")
    print("x -- Beenden")

    cmd = input("Kommando: ").strip().lower()

    if cmd == "x":
        print("Rolo beendet")
        break
    elif cmd == "p":
        for entry in rolo:
            print(entry)
    elif cmd == "n":
        name = input("Name: ").strip()
        vorname = input("Vorname: ").strip()
        plz = input("PLZ: ").strip()
        ort = input("Ort: ").strip()
        strasse = input("Strasse: ").strip()
        telefon = input("Tel.: ").strip()

        if not name:
            print("Ein Name muss vergeben werden!")
        elif not plz:
            print("Eine PLZ muss vergeben werden")
        elif not telefon:
            print("Eine Telefonnummer muss vergeben werden!")
        else:
            eintrag = {
                "name": name,
                "vorname": vorname,
                "telefon": telefon,
                "plz": plz,
                "ort": ort,
                "strasse": strasse,
            }
            rolo.append(eintrag)
    elif cmd == "f":
        name = input("Name: ").strip()
        plz = input("PLZ: ").strip()
        if not name:
            print("Ein Name muss vergeben werden!")
        elif not plz:
            print("Eine PLZ muss vergeben werden")
        else:
            count = 0
            for daten in rolo:
                if daten["name"].casefold() == name.casefold() and daten["plz"] == plz:
                    print("Gefunden: ", daten)
                    count += 1
            if count == 0:
                print(f"Die Kombination {name} {plz} ist nicht bekannt")
    elif cmd == "d":
        pass
    elif cmd == "l": # load from file
        dateiname = input("Dateiname: ").strip()
        try:
            with open(dateiname, "r") as fd:
                rolo = json.load(fd)
        except Exception as e:
            print("Fehler:", e)
    elif cmd == "s": # save to file
        dateiname = input("Dateiname: ").strip()
        try:
            with open(dateiname, "w") as fd:
                json.dump(rolo, fd, indent=4, ensure_ascii=False)
        except Exception as e:
            print("Fehler:", e)
    else:
        print("Unbekanntes Kommando: ", cmd)
