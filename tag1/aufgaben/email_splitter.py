# E-Mail zerlegen

#  Aufgabe: E-Mail-Adresse einlesen, lokalen Teil und Domain getrennt ausgeben.
#  Eingabe: info@uc-it.de
#  Ausgabe: Lokal: info | Domain: uc-it.de
mail = input("Mailadresse: ")

if mail.count("@") != 1:
    print(f"Keine valide mail: '{mail}'")
else:
    name, domain = mail.split("@")
    print("Name:", name)
    print("Domäne:", domain)
