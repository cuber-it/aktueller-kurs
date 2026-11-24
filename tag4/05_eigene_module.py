# Tag 4 – Eigene Module
# geometrie.py liegt neben diesem Skript und enthält wiederverwendbare Funktionen.

import geometrie

print(f"Kreisfläche bei Radius 2: {geometrie.kreis_flaeche(2):.2f}")
print(f"Kreisumfang bei Radius 2: {geometrie.kreis_umfang(2):.2f}")

# Ein Modulname macht die Herkunft eines aufgerufenen Namens sichtbar.
from geometrie import kreis_flaeche

print(f"Direkter Funktionsname: {kreis_flaeche(3):.2f}")

import geometrie as geo

print(f"Mit Modulalias: {geo.kreis_umfang(1):.2f}")
