# Experiment – Unterschiedliche Texte sammeln
# Rand-Leerraum wird entfernt; Groß- und Kleinschreibung bleiben bedeutsam.

werte = []
while True:
    eingabe = input("Text eingeben, exit beendet: ").strip()
    if eingabe == "exit":
        break
    if not eingabe:
        print("Leere Eingabe übersprungen.")
    elif eingabe in werte:
        print("Wert ist bereits vorhanden.")
    else:
        werte.append(eingabe)
print("Gesammelt:", werte)
