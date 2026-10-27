# Tag 2 – if / elif / else
#
# Mit "if" reagiert dein Programm auf Bedingungen.
# Beachte: Einrückung ist Pflicht (Standard: 4 Leerzeichen).

alter = int(input("Wie alt bist du? "))

if alter < 18:
    print("Minderjährig.")
elif alter < 65:
    print("Erwachsen.")
else:
    print("Im Ruhestand?")

# --- Wahrheitswerte / Truthiness ---
# Diese Werte gelten als "falsy":
#   False, None, 0, 0.0, ""   (leerer String)
# Alles andere ist "truthy".

eingabe = input("Sag etwas (oder einfach Enter): ")
if eingabe:
    print(f"Du hast '{eingabe}' gesagt.")
else:
    print("Du hast nichts eingegeben.")

# --- Mehrere Bedingungen kombinieren ---
zahl = 7

if zahl > 0 and zahl < 10:
    print("einstellige positive Zahl")

# Schöner: Verkettung
if 0 < zahl < 10:
    print("dasselbe, kürzer geschrieben")

# --- Einzeiler: ternärer Ausdruck ---
# Aufbau:  wert = ergebnis_wenn_wahr  if  bedingung  else  ergebnis_wenn_falsch

n = 5
art = "gerade" if n % 2 == 0 else "ungerade"
print(f"{n} ist {art}.")

# Praktisch für kurze Zuweisungen –
# bei komplizierter Logik lieber ein normales if schreiben.
