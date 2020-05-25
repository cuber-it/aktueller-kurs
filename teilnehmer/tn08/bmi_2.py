gewicht = input("Gewicht in KG: ")
groesse = input("Grösse in Metern: ")

bmi = int(gewicht) / (float(groesse) * float(groesse)) 

# print("Ihr BMI ist: "+ str(bmi))
if bmi < 20:
    print ("Esst mehr Schoki!")
elif bmi > 30:
    print ("Heute kein Schoki!")
else:
    print("Alles gut")
