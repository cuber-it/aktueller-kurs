a = input("Bitte geben Sie Ihren Namen ein: ")
b = input("Hallo "+a+" wie groß bist du (in m)?")
c = input("Wie schwer bist du (in kg)?")
d = int(c)/(float(b)*float(b))
if (d) >= 18.5:
    e = "Normalgewicht"
    if (d) >= 25:
        e = "leichtes Übergewicht"
        if (d) >= 30:
            e = "Adipositas (Fettleibigkeit) Grad I"
            if (d) >= 35 and d <= 39.9:
                e = "Adipositas (Fettleibigkeit) Grad II"
                if (d) >= 40:
                    e = "Adipositas (Fettleibigkeit) Grad III"
else:
    e = "Leider nicht bestimmbar"
print("Ihr BMI beträgt: "+str(d) + " Damit hast du "+e)