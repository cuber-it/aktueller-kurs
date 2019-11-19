class X:
    def __str__(self):
        return "Ich bins, dein Objekt"

    def __init__(self):
        pass

#----------------------------------------
def f1(p1):
    print(type(p1))
    print("{}".format(p1))

def f2(p1, p2):
    print("{} {}".format(p1, p2))

def f3(p1, p2="Daddel"):
    print("{} {}".format(p1, p2))

# f3()
f3(1)
f3(2, "a")
#f2("a", 2)
# f2(1, 2, 3)



# f1()
#f1(1)
#f1("Text")
#f1(12.34)
#f1(X())
#f1([1,2,3])
#f1({"a":1, "B":2})