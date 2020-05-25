def bmi (m,  l):
    bmi = m / (l ** 2)
    return bmi

print ("Dieses Programm berechnet den Body-Mass-Index (BMI).")

groesse = input ("Geben Sie bitte Ihre Koepergroesse in cm ein: ")
groesse = float(groesse) / 100

gewicht = input ("Geben Sie bitte Ihr Gewicht in kg ein: ")

print("Ihr BMI betraegt " + str( float(bmi( float(gewicht),  float(groesse)) * 100) / 100.0 ))   # Gibt einen Wert mit 2 Nachkommastellen aus

# Bewertung moeglich

bmi = int(bmi( float(gewicht), float(groesse)) * 100) / 100.0 # bmi nimmt den Wert auf!

if bmi < 16:
    print ("Starkes Untergewicht!")
elif 16 <= bmi < 17:
    print ("Maessiges Untergewicht!")
elif 17 <= bmi < 18.5:
    print ("Leichtes Untergewicht!")
elif 18.5 < bmi < 25:
    print ("Sie haben Normalgewicht!) Herzlichen Glueckwunsch!")
elif 25 <= bmi < 30:
    print ("Sie befinden sich im Praeadipositas-Bereich.")
elif 30 <= bmi < 35:
    print ("Adipositas Grad I")
elif 35 <= bmi < 40:
    print ("Adiposiats Grad II")
elif bmi >= 40:
    print ("Adipositas Grad III")
else:
    print ("Programmfehler: Fall nicht definiert.")