#!/usr/bin/python3
gewicht = input("Gewicht in KG: ")
groesse = input("Grösse in Metern: ")

bmi = int(gewicht) / (float(groesse) * float(groesse)) 

# print("Ihr BMI ist: "+ str(bmi))
print("Ihr BMI ist: {:03.2f}".format(bmi))