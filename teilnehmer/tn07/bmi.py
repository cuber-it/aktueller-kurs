gewicht = input("Gewicht in kg: ")
groesse = input("Größe in Metern: ")

bmi = int(gewicht) / (float(groesse) * float(groesse))

if bmi > 30:
    print("Heute keien Schoki")
elif bmi < 20:
    print("Esst mehr Schoki")
else:
    print("Ihr BMI ist: " + str(bmi))
    print("Alles ok")
