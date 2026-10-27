# BMI Berechnung:

# Eingabe: Name, Grösse, Gewicht
# Verarbeitung: Daten vorbereiten (Typ!!!) - Berechnung -> Zahl
# Ausgabe: Eineziel mit "Ist ok: True/False"

# E
name = input("Name: ")
groesse = input("Grösse in m: ").replace(",", ".")
gewicht = input("Gewicht in kg: ").replace(",", ".")

# V
bmi = None

groesse = float(groesse)
gewicht = float(gewicht)

bmi = gewicht / (groesse ** 2)

# A
print(f"Ist gut: {bmi:.2f} - {18.5 <= bmi <= 24.9}")
