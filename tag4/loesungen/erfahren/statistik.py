"""Referenzlösung: Mehrere Kennzahlen als Tupel zurückgeben."""


def statistik(*zahlen):
    """Liefert (Minimum, Maximum, Mittelwert); ohne Zahlen entsteht ValueError."""
    if not zahlen:
        raise ValueError("Mindestens eine Zahl ist erforderlich.")
    minimum = min(zahlen)
    maximum = max(zahlen)
    mittelwert = sum(zahlen) / len(zahlen)
    return minimum, maximum, mittelwert


if __name__ == "__main__":
    kleinste, groesste, mittelwert = statistik(7, 2, 9, 4)
    print(f"Minimum: {kleinste}; Maximum: {groesste}; Mittelwert: {mittelwert:.2f}")
