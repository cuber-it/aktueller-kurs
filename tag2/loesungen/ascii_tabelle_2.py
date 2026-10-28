# Tag 2 – Aufgabe: ASCII-Tabelle
#
# Aufgabe (Stufe 1):
#   Drucke die druckbaren ASCII-Zeichen (Code 32 bis 126).
#   Pro Zeile: Dezimalwert | Zeichen | Hex | Oktal.
#
# Aufgabe (Stufe 2 – für Schnelle):
#   Hänge die Latin-1-Erweiterung (Code 160 bis 255) an.
#   Was siehst du?
#
# Lernziel:
#   for-Schleife, range(), chr(), Format-Spezifizierer in f-Strings.

# --- Stufe 1: ASCII (32–126) ---
print("=== ASCII (druckbar) ===")
print("Dez | Zch | Hex | Oct")
print("----+-----+-----+----")
for i in range(32, 127):
    print(f"{i:3} |  {chr(i)}  | {i:02x}  | {i:03o}")

# --- Stufe 2: Latin-1-Bonus (160–255) ---
print()
print("=== Latin-1-Erweiterung ===")
print("Dez | Zch")
print("----+----")
for i in range(160, 256):
    print(f"{i:3} |  {chr(i)}")

# Beobachtung:
#   Plötzlich tauchen ä, ö, ü, ß, à, é, ç & Co. auf.
#   Das ist der Bereich, in dem sich ASCII (7 Bit) und
#   Latin-1 / UTF-8 voneinander unterscheiden.
#   Mehr dazu im nächsten Programm: encoding_vergleich.py
