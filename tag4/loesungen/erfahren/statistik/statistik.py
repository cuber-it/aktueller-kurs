def statistik(*zahlen: int | float) -> tuple[int | float, int | float, float]:
    """
        Berechnet Minimum, Maximum und Mittelwert der übergebenen Zahlen.

        Returns:
            tuple: Minimum, Maximum und Mittelwert.

        Raises:
            ValueError: Wenn keine Zahlen übergeben werden.
    """
    if not zahlen:
        #Fehlermeldung ausgeben <- sinnloser Trivialkommentar
        raise ValueError("Mindestens eine Zahl ist erforderlich.")
    # Kommentar - wenig und nur da wo wirklich wichtig
    minimum = min(zahlen)
    maximum = max(zahlen)
    # Mittelwert = Summe der Einzelwerte / anzahl der Einzelwerte <- sinnlose Trivialkommentar
    mittelwert = sum(zahlen) / len(zahlen)
    return minimum, maximum, mittelwert
