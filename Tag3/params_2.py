def sum(werte: list): #
    result = 0
    for wert in werte:
        result += wert
    return result

l = [1,2,3,4,5]
print(sum(l))

# failt! -> print(sum(1))

def summe(*werte):
    """
    Parameter werte: eine beliebige Anzahl von int und/oder float
    """
    result = 0
    for wert in werte:
        result += wert
    return result

print(summe(), summe(1), summe(1, 2, 3), summe(1,2,3,4,5))
#print(summe("a", "b", "c"))
print(summe(1.1, 1.5, 1.9))