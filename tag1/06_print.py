# Tag 1 – Ausgabe mit print()

# Ein Wert
print("Hallo Welt")

# Mehrere Werte – per Komma getrennt, Standard-Trenner ist ein Leerzeichen
print("Name:", "Ulrich", "Alter:", 42)

# Trenner ändern mit sep=
print("2026", "05", "06", sep="-")     # 2026-05-06

# Zeilenende ändern mit end= (Standard ist "\n")
print("ohne Umbruch...", end=" ")
print("weiter in derselben Zeile")

# Sonderzeichen in Strings
print("Zeile 1\nZeile 2")     # \n = Zeilenumbruch
print("Spalte1\tSpalte2")     # \t = Tabulator
print("Sie sagte: \"Hallo\"") # \" = Anführungszeichen im String

# Strings über mehrere Zeilen
print("""Erste Zeile
Zweite Zeile
Dritte Zeile""")
