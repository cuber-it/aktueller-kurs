# Tag 1 – Sonderkapitel: Moderne Operatoren
#
# Python entwickelt sich weiter. Hier ein Vorgriff auf einen
# Operator, den du in modernem Code immer häufiger siehst.
# Sinnvoll einsetzbar wird er erst mit Kontrollstrukturen
# (kommt an Tag 2) – die Syntax schauen wir uns aber schon an.

# --- Walross-Operator  :=  (seit Python 3.8) ---
#
# Erlaubt eine Zuweisung MITTEN in einem Ausdruck.
#
# Klassisch (zwei Zeilen):
#   p = 3.14159
#   print(f"Pi: {p:.4f}")
#
# Mit Walross (zuweisen + verwenden in einem Schritt):

print(f"Pi auf 4 Nachkommastellen: {(p := 3.14159):.4f}")
print(f"Wir haben Pi gerade in p gespeichert: p = {p}")

# Ein zweites Beispiel: Länge eines Strings prüfen UND merken
print(f"'Python' hat {(n := len('Python'))} Zeichen, n ist jetzt {n}.")

# Wofür ist das gut?
# Vor allem in Schleifen und if-Bedingungen wird der Walross
# nützlich – das schauen wir uns morgen an, z. B.:
#
#   while (zeile := datei.readline()):
#       print(zeile)
#
# Faustregel: nur einsetzen, wenn der Code dadurch *kürzer*
# UND *klarer* wird. Sonst lieber zwei normale Zeilen.

# Weitere "moderne" Schreibweisen begegnen uns morgen:
#   - match / case        (Pattern Matching, seit 3.10)
#   - Union-Types  int | str   (seit 3.10, bei Typhinweisen)
