def runner(code, finally_code):
    try:
        code()
    finally:
        finally_code()



def f():
    # print("HUHU")
    return 1/0

def fc():
    print("alles easy")

def fc2():
    print("Ups!")

runner(f, fc2)