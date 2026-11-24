# Experiment – Eine eigene Funktion importieren
# Start aus dem Repository: python3 -m tag4.experimente.import_1

from .fkt_1 import erstelle_adresse


def main():
    """Erzeugt einen Datensatz mithilfe des importierten Moduls."""
    felder = ["name", "kenntnis"]
    werte = ["Anna", "Python"]
    print(erstelle_adresse(felder, werte))


if __name__ == "__main__":
    main()
