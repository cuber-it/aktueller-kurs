koerper_groesse = input("Gebe Deine Größe in Meter  ein: ")
koerper_gewicht = input("Gebe Dein Gewicht in Kilogramm ein: ")
body_mass_index = int(koerper_gewicht) /(float(koerper_groesse) * float(koerper_groesse))


#print("Dein BMI Wert lautet: " + str(body_mass_index))
print("Ihr BMI ist: {:03.2f}".format(body_mass_index))