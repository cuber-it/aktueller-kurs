# Tag 2 – Aufgabe: Encodings vergleichen
#
# Aufgabe (Stufe 3):
#   Lies ein Wort ein und gib die Bytes in UTF-8 und Latin-1 aus.
#   Welche Variante ist kürzer? Warum?
#   Zusätzlich: versuche es als reines ASCII zu kodieren – was passiert?
#
# Aufgabe (Stufe 4 – Detektiv-Modus):
#   "MÃ¼sli" reparieren – aus dem zerschossenen String wieder
#   "Müsli" machen.
#
# Lernziel:
#   str ↔ bytes, encode/decode, warum encoding="utf-8" in open() wichtig ist.

# --- Stufe 3: Encoding-Vergleich ---
text = input("Gib ein Wort ein (gerne mit Umlauten): ")

print()
print(f"Klartext           : {text}")
print(f"Anzahl Zeichen     : {len(text)}")
print()

utf8 = text.encode("utf-8")
print(f"UTF-8 Bytes        : {utf8}")
print(f"UTF-8 Anzahl Bytes : {len(utf8)}")

try:
    latin1 = text.encode("latin-1")
    print(f"Latin-1 Bytes      : {latin1}")
    print(f"Latin-1 Anzahl    : {len(latin1)}")
except UnicodeEncodeError as e:
    print(f"Latin-1: geht nicht ({e})")

try:
    ascii_bytes = text.encode("ascii")
    print(f"ASCII Bytes        : {ascii_bytes}")
except UnicodeEncodeError as e:
    print(f"ASCII: geht nicht ({e})")
    # ASCII kennt nur Codes 0–127, also keine Umlaute.

print()

# Beobachtung (typisch für "Müsli"):
#   Klartext           : Müsli       -> 5 Zeichen
#   UTF-8 Bytes        : b'M\xc3\xbcsli'   -> 6 Bytes (ü = 2 Bytes!)
#   Latin-1 Bytes      : b'M\xfcsli'        -> 5 Bytes (ü = 1 Byte)
#   ASCII              : UnicodeEncodeError

# --- Stufe 4: Mojibake reparieren ---
zerschossen = "MÃ¼sli"
# Was ist passiert?
#   Original:  "Müsli" -> als UTF-8 codiert: b'M\xc3\xbcsli'
#   Diese Bytes wurden FÄLSCHLICH als Latin-1 dekodiert.
#   In Latin-1 ist \xc3 = 'Ã' und \xbc = '¼' -> "MÃ¼sli".
#
# Reparatur: rückwärts durch beide Schritte.

repariert = zerschossen.encode("latin-1").decode("utf-8")
print(f"zerschossen : {zerschossen}")
print(f"repariert   : {repariert}")

# Genau diese Logik braucht man, wenn man auf eine kaputte CSV
# trifft, die mit dem falschen Encoding gespeichert wurde.
