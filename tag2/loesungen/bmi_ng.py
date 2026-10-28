# Nehmt das BMI-Beispiel vom Vortag.
#
# Gestaltet mit Hilfe von if, elif und else die Ausgabe
# gemäß der vorgegebenen BMI-Tabelle ausdrucksstärker.

# E – Eingabe
name = input("Name: ")
groesse = input("Größe in m: ").replace(",", ".")
gewicht = input("Gewicht in kg: ").replace(",", ".")

# V – Verarbeitung
groesse = float(groesse)
gewicht = float(gewicht)

bmi = gewicht / (groesse ** 2)

if bmi < 18.5:
    kategorie = "Untergewicht"
elif bmi < 25:
    kategorie = "Normalgewicht"
elif bmi < 30:
    kategorie = "Übergewicht"
elif bmi < 35:
    kategorie = "Adipositas Grad I"
elif bmi < 40:
    kategorie = "Adipositas Grad II"
else:
    kategorie = "Adipositas Grad III"

# A – Ausgabe
print(f"{name}, dein BMI beträgt {bmi:.2f}.")
print(f"Kategorie: {kategorie}")
