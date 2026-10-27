# Tag 2 – Sonderkapitel: Moderne Kontrollstrukturen
#
# Pattern Matching mit  match / case  (seit Python 3.10).
# Erinnert auf den ersten Blick an switch/case aus anderen
# Sprachen, kann aber deutlich mehr.

farbe = input("Welche Ampelfarbe? ").lower()

match farbe:
    case "rot":
        print("Stehen.")
    case "gelb":
        print("Achtung.")
    case "grün":
        print("Fahren.")
    case _:
        # _ ist der Wildcard – fängt alles, was sonst nichts trifft.
        print("Unbekannte Farbe.")

# --- Mehrere Werte in einem Zweig zusammenfassen ---
befehl = input("Befehl: ").lower()

match befehl:
    case "hilfe" | "?" | "h":
        print("Hilfetext anzeigen…")
    case "ende" | "exit" | "quit":
        print("Programm beenden.")
    case _:
        print("Unbekannter Befehl.")

# match / case wird besonders mächtig bei strukturierten Daten
# (Tupeln, Dicts, Klassen) – dazu mehr, wenn wir diese Typen
# eingeführt haben.
