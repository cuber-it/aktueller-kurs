# Tag 2 – while-Schleife
#
# Eine while-Schleife läuft, solange ihre Bedingung wahr ist.

zaehler = 1
while zaehler <= 5:
    print(f"Durchgang {zaehler}")
    zaehler += 1

# --- Eingabe wiederholen, bis sie passt ---
while True:
    eingabe = input("Tippe 'ende' zum Beenden: ")
    if eingabe == "ende":
        break              # Schleife sofort verlassen
    print("Verstanden, weiter geht's...")

print("Tschüss!")

# --- continue: aktuellen Durchgang abbrechen, weitermachen ---
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue           # gerade Zahlen überspringen
    print(i)               # gibt 1, 3, 5, 7, 9 aus

# Vorsicht: Endlosschleifen!
# Wenn die Bedingung nie False wird (und kein break greift),
# läuft die Schleife für immer. Mit Strg+C abbrechen.
