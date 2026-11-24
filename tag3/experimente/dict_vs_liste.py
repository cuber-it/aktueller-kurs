# Experiment – Positionen und benannte Felder
# Ein Dictionary macht die Zuordnung von Feldnamen zu Werten ausdrücklich.

felder = ["name", "kenntnis", "ort"]
werte = ["Anna", "Python", "Hamburg"]

position = felder.index("kenntnis")
print("Über die Feldposition:", werte[position])

profil = dict(zip(felder, werte, strict=True))
print("Über den Schlüssel:", profil["kenntnis"])
