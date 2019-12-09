while input("Vergleichen?") != "Stopp":
    eingabe_a = input("Erste Eingabe: ")
    eingabe_b = input("Zweite Eingabe: ")

    if eingabe_a == eingabe_b:
        print("Beide sind gleich")
    else:
        print("Eingaben unterscheiden sich")
print("Fertig")