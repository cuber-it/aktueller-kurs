# Tag 1 – Typkonvertierung (Casting)
#
# Werte zwischen Typen umwandeln. Sehr wichtig im
# Zusammenspiel mit input(), das immer einen str liefert.

# str -> int
zahl = int("42")
print(zahl, type(zahl))

# str -> float
preis = float("3.99")
print(preis, type(preis))

# int -> str
text = str(2026)
print(text, type(text))

# int <-> float
print(float(7))    # 7.0
print(int(7.9))    # 7  (schneidet ab, rundet NICHT!)

# bool() – wann ist etwas "wahr"?
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False (leerer String)
print(bool("nein")) # True  (jeder nicht-leere String ist True!)
print(bool(None))   # False

# Achtung: nicht jede Umwandlung klappt
# int("abc")  -> ValueError
# Wie man solche Fehler abfängt, kommt an Tag 2.
