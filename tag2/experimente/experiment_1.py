mail = input("EMailadresse eingeben:")

if mail.count("@") != 1:
    print("Das ist keine valide Mail")
else:
    name, domain = mail.split("@")

    if name != "" and domain != "":
        print("Gefunden:", name, domain)
    else:
        print("Daten unvollständig")

print("Fertig")
