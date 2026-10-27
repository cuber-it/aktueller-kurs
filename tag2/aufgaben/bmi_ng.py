# Nehmt das BMI Beispiel vom Vortag
#
# Und gestaltet mit Hilfe vom if die Ausgabe ausdrucksstärker,
# gemäss der offiziellen Tabelle
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
# ...
