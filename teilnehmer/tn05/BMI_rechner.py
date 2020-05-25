# Hash ist ein Kommentar --> geht bis Zeilenende

gewicht = input ("Hallo wie viel KG wiegen Sie?")
groesse = input ("Wie Gross sind Sie in Meter?")

BMI = int(gewicht) / (float(groesse)* float(groesse))


if BMI <= 20:
    print ("Ihr BMI ist {:03.2f}. Iss mehr Schoki!".format(BMI) )
elif BMI >= 30:
    print("Ihr BMI ist {:03.2f}. Keine Schoki mehr".format(BMI) )
else:
    print ("alles gut")

#print ("Ihr BMI ist: " + str(BMI))
#print( "Ihr BMI ist: {:03.2f}".format(BMI)) #formatiert variable an stelle der Klammer mit spezieller Formatierung