while True:
    zahl_1 = input("Zahl 1: ").replace(",", ".")
    zahl_2 = input("Zahl 2: ").replace(",", ".")
    operator = input("+ - * /:")
    ergebnis = f"{zahl_1} {operator} {zahl_2}"
    print(f"{ergebnis} = {eval(ergebnis)}") # eval ist riskant, wiell alles damit ausgeführt wird was der Benutzer eingibt
    if input("Weiter/Ende? ").lower().strip().startswith("e"): # evtl zu kurz, das jedes Wort mit e dann passt
        break
print("Auf Wiedersehen")
