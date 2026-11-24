# Experiment – Tabellarische Daten als Liste von Zeilen
# Jede Zeile enthält Datum, Schlusskurs und Handelsvolumen.

kurse = [
    ["2020-06-02", 323.34, 21910700],
    ["2020-06-01", 321.85, 20254650],
    ["2020-05-29", 317.94, 38399530],
]
for datum, schlusskurs, volumen in kurse:
    print(f"{datum}: {schlusskurs:.2f}, Volumen {volumen}")
