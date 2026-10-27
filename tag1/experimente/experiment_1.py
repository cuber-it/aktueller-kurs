import decimal

# E ingabe
name = input("Name: ")
alter = input("Alter: ")
adresse = input("Adresse: ")
kontostand = input("Kontostand: ").replace(",", ".")

# V erarbeitung
alter = int(alter)
kontostand = decimal.Decimal(kontostand)
kontostand = kontostand + decimal.Decimal("3500.00")

# A usgabe
print(name, adresse, alter, kontostand, sep=',')
