#!/usr/bin/python3

a = input("Geben Sie Ihren Namen ein:")
print("Hallo " + a)



KG = input("Berechnen Sie Ihren BMI. Geben Sie Ihr Körpergewicht ein: ")
CM = input("Geben Sie Ihre Größe in Metern ein: ")

CM = float(CM) * float(CM) 
BMI = int(KG) / float(CM)

print("Ihr BMI beträgt: " + str(BMI))

if int(BMI) >= 30:
    print("Heute keine Schokolade")
elif int(BMI) <= 20: 
    print("Iss mehr Schokolade")
else:
    print("Alles ist gut")