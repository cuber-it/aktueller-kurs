# Tag 2 – Fehlerbehandlung mit try / except
#
# Wenn etwas schiefgeht, "wirft" Python eine Exception.
# Mit try/except kannst du den Fehler abfangen und
# kontrolliert reagieren – statt das Programm abstürzen zu lassen.

# --- Klassiker: Eingabe in Zahl umwandeln ---
text = input("Gib eine Zahl ein: ")

try:
    zahl = int(text)
    print(f"Doppelt so viel: {zahl * 2}")
except ValueError:
    print(f"'{text}' ist keine gültige Zahl.")

# --- Mehrere Exceptions getrennt behandeln ---
try:
    a = int(input("Zähler: "))
    b = int(input("Nenner: "))
    print(a / b)
except ValueError:
    print("Bitte ganze Zahlen eingeben.")
except ZeroDivisionError:
    print("Durch 0 teilen geht nicht.")

# --- Datei lesen, die vielleicht nicht existiert ---
try:
    with open("vielleicht_nicht_da.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Datei existiert nicht – egal, weiter im Programm.")

# --- try / except / else / finally ---
try:
    x = int("123")
except ValueError:
    print("Fehler beim Umwandeln.")
else:
    # läuft NUR, wenn KEINE Exception geflogen ist
    print(f"Erfolgreich umgewandelt: {x}")
finally:
    # läuft IMMER (egal ob Fehler oder nicht)
    print("Aufräumen / Abschluss-Meldung.")

# --- Eigene Fehler werfen mit raise ---
alter = -3
if alter < 0:
    # raise ValueError("Alter darf nicht negativ sein!")
    # (auskommentiert, damit das Skript ohne Crash durchläuft)
    print("Negatives Alter würde hier eine Exception werfen.")
