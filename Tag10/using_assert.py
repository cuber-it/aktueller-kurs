def calculate_a(a, b): # klappt für int int float float aber auch str int!! wollen wir str int wirklich?
    try: # reicht leider nicht aus weil str * int erlaubt ist!
        return a * b
    except ValueError as e:
        print("Böser Fehler")
        raise e


def calculate_a_gerettet(a, b): # Rettungsversuch
    try:
        return int(a) * int(b) # erzwingt int - dafür kein float mehr!!
    except ValueError as e:
        print("Böser Fehler")
        raise e



def calculate_b(a, b): # defensiv
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    else:
        raise TypeError("Böser Fehler")

def calculate_c(a, b): # defensiv - pythonic
    assert isinstance(a, int), "Böser Fehler in a"
    assert isinstance(b, int), "Böser Fehler in b"
    return a * b


#print(calculate_a(1, 1))
#print(calculate_a(1.0, 1.0))
#print(calculate_a("a", 5)) # ???? Echt jetzt ???
#print(calculate_a(5, "a"))
#print(calculate_a(5.0, "a")) # Fehler, wie erwartet

#print(calculate_b(1, 1))
#print(calculate_b(1.0, 1.0))
#print(calculate_b("a", 5))
#print(calculate_b(5, "a"))
#print(calculate_b(5.0, "a"))

print(calculate_c(1, 1))
#print(calculate_c(1.0, 1.0))
#print(calculate_c("a", 5))
#print(calculate_c(5, "a"))
#print(calculate_c(5.0, "a"))
