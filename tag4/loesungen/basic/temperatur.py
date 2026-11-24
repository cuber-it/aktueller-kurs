"""Referenzlösung: Eine Berechnung von der Ausgabe trennen."""


def celsius_nach_fahrenheit(celsius):
    """Rechnet einen Celsius-Wert in Fahrenheit um."""
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    for celsius in [0, 100, -40]:
        print(f"{celsius:.1f} °C = {celsius_nach_fahrenheit(celsius):.1f} °F")
