#!/usr/bin/python3
gewicht = input("Gewicht in KG: ")
groesse = input("Grösse in Metern: ")

bmi = int(gewicht) / (float(groesse) * float(groesse)) 

if bmi > 30:
    print("Heute keine Schoki")
elif bmi < 20:
    print("Esst mehr Schoki") 
else:
    print("Alles ok!")   