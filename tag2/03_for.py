# Tag 2 – for-Schleife
#
# Mit "for" iteriert man über etwas Durchlaufbares.
# Heute: range() und Strings (Dateizeilen folgen beim Datei-Input).

# --- range() liefert Zahlenfolgen ---
for i in range(5):
    print(i)               # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)               # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)               # 0, 2, 4, 6, 8

# --- über einen String iterieren (Zeichen für Zeichen) ---
for buchstabe in "Python":
    print(buchstabe)

# --- break / continue funktionieren auch hier ---
for i in range(10):
    if i == 5:
        break              # Schleife verlassen
    print(i)               # 0..4

for i in range(6):
    if i == 3:
        continue           # 3 überspringen
    print(i)               # 0, 1, 2, 4, 5

# --- Klassiker: Quersumme einer Eingabe ---
zahl = input("Gib eine positive ganze Zahl ein: ")
summe = 0
for ziffer in zahl:
    summe += int(ziffer)
print(f"Quersumme von {zahl}: {summe}")
