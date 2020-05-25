a= input("Gewicht in kg ?:")
b= input("Groesse in m ?:")

bmi= int(a)/(float(b)*float(b))
print("ihr bmi ist"+str(bmi))

if bmi < 20:
    print("zu geringer BMI")
elif bmi > 30:
    print("zu grosser BMI")
else:
    print("alles gut")
