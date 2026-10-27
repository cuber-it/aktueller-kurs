# Tag 1 – Operatoren

# --- Arithmetische Operatoren ---
print(7 + 3)   # Addition          -> 10
print(7 - 3)   # Subtraktion       -> 4
print(7 * 3)   # Multiplikation    -> 21
print(7 / 3)   # Division          -> 2.3333... (float!)
print(7 // 3)  # Ganzzahldivision  -> 2
print(7 % 3)   # Rest (Modulo)     -> 1
print(2 ** 8)  # Potenz            -> 256

# --- Vergleichsoperatoren (Ergebnis: bool) ---
print(5 == 5)  # gleich
print(5 != 3)  # ungleich
print(5 < 10)
print(5 > 10)
print(5 <= 5)
print(5 >= 6)

# --- Logische Operatoren ---
print(True and False)  # nur True wenn beide True
print(True or False)   # True wenn mindestens einer True
print(not True)        # negiert

# --- Zuweisungs-Kurzformen ---
zaehler = 0
zaehler += 1   # entspricht: zaehler = zaehler + 1
zaehler *= 3
print(zaehler)

# --- String-Operatoren ---
print("Hallo" + " " + "Welt")  # Verkettung
print("ha" * 3)                 # Wiederholung -> "hahaha"
