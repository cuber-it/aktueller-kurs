# Tag 2 – Strings (Schwerpunkt)
#
# Strings sind in Python eine eigene Welt: sehr mächtig,
# unveränderlich (immutable) und mit vielen eingebauten Methoden.

text = "Hallo Python"

# --- Länge ---
print(len(text))               # 12

# --- Indizierung (0-basiert) ---
print(text[0])                 # 'H'
print(text[-1])                # 'n'   (negativ = von hinten)

# --- Slicing   [start:stop:step]   stop ist exklusiv ---
print(text[0:5])               # 'Hallo'
print(text[6:])                # 'Python'
print(text[:5])                # 'Hallo'
print(text[::2])               # 'HloPto'   (jedes zweite Zeichen)
print(text[::-1])              # umgedreht

# --- Wichtige Methoden ---
roh = "  Hallo Welt  "
print(roh.strip())             # 'Hallo Welt'   (Whitespace außen weg)
print(roh.upper())             # '  HALLO WELT  '
print(roh.lower())

print("Hallo Welt".replace("Welt", "Python"))
print("a;b;c".split(";"))      # 'a', 'b', 'c' (Ergebnis ist eine Liste – kommt später)

print(text.find("Py"))         # Position oder -1, wenn nicht gefunden
print(text.startswith("Hallo"))
print(text.endswith("ython"))

# --- Operator "in" ---
print("Python" in text)        # True
print("ruby" in text)          # False

# --- Immutability ---
# Strings können NICHT direkt verändert werden:
#   text[0] = "h"     # -> TypeError!
#
# Stattdessen baut man einen NEUEN String:
text = "h" + text[1:]
print(text)                    # 'hallo Python'
