def machwas(wert):
    '''
        machwas: show data input on stdout

        @params: wert - integer
        @return: nothing
    '''
    print(wert)

#machwas(4711)
#--------------------------------------------
def f1():
    print("f1")

def f2(p1):
    print("f2 " + p1)

def f3(p1, p2):
    print("f3 " + p1 + "," + p2)

def f4(p1, p2="X"):
    print("f4 " + p1 + "," + p2)

def f5(p1="1", p2="X"):
    print("f5 " + p1 + "," + p2)

f1()
f2("1")
f3("1", "2")

f4("1")
f4("1", "Z")

f5()
f5("99")
f5("99", "Z")
f5(p2="Z")
f5(p2="Z", p1="Willi")

