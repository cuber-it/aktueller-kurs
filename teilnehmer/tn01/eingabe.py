gewicht = input("Gewicht (kg): ")
groesse = input("Größe (cm): ")

bmi = int(gewicht) / (float(groesse) ** float(groesse))

print ("der BMI ist: " + str(bmi))
print ("Der BMI ist: {:03.2f}".format(bmi))