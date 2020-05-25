gewicht = input("Gewicht (kg): ")
groesse = input("Größe (cm): ")

bmi = int(gewicht) / (float(groesse) ** float(groesse))

if bmi > 30.00:
    print("Heute keine Schokolade mehr")
else:
    if bmi < 20.00:
        print("Esst mehr Schokolade")
    else:
        print("Alles ist gut!")

print ("der BMI ist: " + str(bmi))
print ("Der BMI ist: {:03.2f}".format(bmi))