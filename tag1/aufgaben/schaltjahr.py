# Aufgabe: Jahr einlesen, einen Boolean ausgeben, der angibt, ob es ein Schaltjahr ist — ohne if.
#  Regel: durch 4 teilbar und nicht durch 100, oder durch 400 teilbar.

# E
jahr = input("Jahr: ")

# V
jahr = int(jahr)

# A
ist_schaltjahr = (jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0
print(f"Ist Schaltjahr: {jahr} {ist_schaltjahr}")

# Oder auch:
jahr_4_regel = jahr % 4 == 0
jahr_100_regel = jahr % 100 != 0
jahr_400_regel = jahr % 400 == 0

ist_schaltjahr = (jahr_4_regel and jahr_100_regel) or jahr_400_regel
print(f"Ist Schaltjahr: {jahr} {ist_schaltjahr}")
