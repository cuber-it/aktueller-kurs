# Experiment – Doppelte Zahlen erkennen
# Die Liste bewahrt alle Eingaben, die Menge nur unterschiedliche Werte.

text = input("Ganze Zahlen, mit Leerzeichen getrennt: ")
try:
    zahlen = [int(teil) for teil in text.split()]
except ValueError:
    print("Bitte ausschließlich ganze Zahlen eingeben.")
else:
    print("Eingelesen:", zahlen)
    print("Doppelte Werte vorhanden:", len(zahlen) != len(set(zahlen)))
