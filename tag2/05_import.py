# Tag 2 – Import-Grundlagen
#
# Mit "import" holst du dir fertige Module aus der
# Standardbibliothek (oder später aus eigenen Modulen).

# --- Komplettes Modul importieren ---
import math

print(math.pi)
print(math.sqrt(2))
print(math.floor(3.7))
print(math.ceil(3.2))

# --- Einzelne Namen direkt importieren ---
from math import pi, sqrt
print(pi)
print(sqrt(9))

# --- Umbenennen mit "as" ---
import math as m
print(m.pi)

from math import sqrt as wurzel
print(wurzel(16))

# --- Ein paar nützliche Module aus der Standardbibliothek ---
import random
print(random.randint(1, 6))            # Würfel
print(random.choice("Python"))         # zufälliges Zeichen aus dem String

import datetime
print(datetime.date.today())

import os
print(os.getcwd())                     # aktuelles Arbeitsverzeichnis

# Tipp: was die Standardbibliothek alles bietet, steht hier:
#   https://docs.python.org/3/library/
