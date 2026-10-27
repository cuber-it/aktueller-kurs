# Tag 1 – Skalare Datentypen + None
#
# "Skalar" = ein einzelner Wert (im Gegensatz zu Listen, Dicts etc.).
# In dieser Einheit konzentrieren wir uns auf vier Typen plus None.

# int – Ganzzahl
anzahl = 7

# float – Fließkommazahl
preis = 3.99

# str – Zeichenkette
gruss = "Hallo Welt"

# bool – Wahrheitswert (True oder False)
ist_offen = True

# None – "kein Wert" / "noch nichts gesetzt"
ergebnis = None

print(type(anzahl))     # <class 'int'>
print(type(preis))      # <class 'float'>
print(type(gruss))      # <class 'str'>
print(type(ist_offen))  # <class 'bool'>
print(type(ergebnis))   # <class 'NoneType'>

# Ausblick: Python kennt noch weitere Typen, z. B.
#   list   [1, 2, 3]
#   tuple  (1, 2, 3)
#   dict   {"name": "Ulrich"}
#   set    {1, 2, 3}
# Diese sammeln mehrere Werte und kommen später im Kurs.
