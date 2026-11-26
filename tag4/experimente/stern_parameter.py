""" <- dient hier als bequemes Auskommentieren von Codeblöcken, ist de  facto ein grosser String der niemand interessiert
def summe(werte):
    erg = 0
    for wert in werte:
        erg += wert
    return erg

print(summe([1,2]))
print(summe([1,2,3,4]))
"""

def summe_ng(*werte):
    erg = 0
    for wert in werte:
        erg += wert
    return erg

print(summe_ng(1,2))
print(summe_ng(1,2,3,4))

#--------------------------------
import decimal
def mach_was(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    print("Fertig")

mach_was()
mach_was(wert=1)
mach_was(wert=1, text="HUHU", betrag=12.34, konto=decimal.Decimal("12.3456"))
