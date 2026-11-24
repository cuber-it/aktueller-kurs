# Tag 4 – Namensräume und Programmstart
# Importieren soll Funktionen verfügbar machen, ohne das Hauptprogramm zu starten.

import sys
import geometrie as geo
from geometrie import kreis_flaeche


def main():
    """Zeigt Modulnamen und die beiden Zugriffsformen."""
    print("Name dieses Skripts:", __name__)
    print("Name des importierten Moduls:", geo.__name__)
    print("Skriptordner im Suchpfad:", sys.path[0])
    print(f"Über den Modulnamen: {geo.kreis_flaeche(2):.2f}")
    print(f"Über den Funktionsnamen: {kreis_flaeche(2):.2f}")


if __name__ == "__main__":
    main()
