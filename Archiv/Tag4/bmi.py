# https://www.askpython.com/python/examples/bmi-calculator

h = input("Enter your height in meters: ").replace(",", ".")
h = float(h)
if h < 0.5 or h > 2.5:
    print("Ungültige Grösse")
    exit(1)

w=float(input("Enter your Weight in Kg: ").replace(",", "."))
if w <= 0 or w >= 300:
    print("Ungültiges Gewicht")
    exit(2)

BMI=w/(h*h)

print("BMI Calculated is:  ",BMI.replace(".", ","))

if(BMI>0):
    if(BMI<=16):
        print("You are very underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("Congrats! You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are very overweight")
else:
    print("enter valid details")
    exit(3)

exit(0)
