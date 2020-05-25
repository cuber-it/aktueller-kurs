
try:
    eingabe = int(input("EIngabe: "))
    ergebnis = 42 / eingabe
    print(ergebnis)
except:
    print("Fehler")

finally:
    print("wird immer durchlaufen")
    
print("Ende")