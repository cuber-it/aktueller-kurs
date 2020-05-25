try:
    eingabe = int(input("Eingabe: "))

    # hier würde der Test der Eingabe hingehören!!!

    ergebnis = 42 / eingabe
    print(ergebnis)
#except:
#    print("Fehler")
finally:
    print("Wird immer durchlaufen")
print("Ende")