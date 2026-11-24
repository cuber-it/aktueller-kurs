# Tag 4 – Rückgabewerte und Gültigkeitsbereiche
# Lokale Namen und übergebene Werte helfen, Änderungen nachvollziehbar zu halten.

def min_max(werte):
    """Liefert Minimum und Maximum; eine leere Sammlung ist ungültig."""
    if not werte:
        raise ValueError("Mindestens ein Wert ist erforderlich.")
    return min(werte), max(werte)


def vorzeichen(zahl):
    """Liefert eine Beschreibung und beendet sich beim passenden return."""
    if zahl > 0:
        return "positiv"
    if zahl < 0:
        return "negativ"
    return "null"


def erhoehe(stand):
    """Liefert den nächsten Stand ohne einen äußeren Namen neu zu binden."""
    stand += 1
    return stand


kleinste, groesste = min_max([7, 2, 9, 4])
print("Minimum und Maximum:", kleinste, groesste)
print("Vorzeichen:", vorzeichen(-3))

stand = 10
naechster_stand = erhoehe(stand)
print("Äußerer Stand:", stand)
print("Rückgabewert:", naechster_stand)

# Das Tupel aus min_max kann auch als ein Wert gespeichert werden.
print("Rückgabetupel:", min_max([5, 1, 8]))

# Funktionen können auch Sortierkriterien liefern.
datensaetze = [{"name": "Apfel", "menge": 3}, {"name": "Birne", "menge": 1}]
nach_menge = sorted(datensaetze, key=lambda eintrag: eintrag["menge"])
print("Nach Menge sortiert:", nach_menge)
# lambda eintrag: eintrag["menge"] ist eine kurze Funktion mit einem Rückgabewert.
