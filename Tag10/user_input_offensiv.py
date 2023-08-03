def get_input():
    eingabe = input("Eingabe 10-90: ")
    try:
        wert = int(eingabe)
        if wert < 10 or wert > 90:
            raise ValueError()
        return wert
    except ValueError as e:
        return "Das war nix!"
