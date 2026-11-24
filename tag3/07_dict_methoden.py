# Tag 3 – Dictionaries: Methoden und Iteration
# keys(), values() und items() liefern Sichten auf das Dictionary.

lager = {"Apfel": 50, "Birne": 20, "Kirsche": 120}
print("Schlüssel:", list(lager.keys()))
print("Werte:", list(lager.values()))
print("Paare:", list(lager.items()))

for produkt, menge in lager.items():
    print(f"{produkt}: {menge} Stück")
print("Gesamtbestand:", sum(lager.values()))

# setdefault() ergänzt nur einen fehlenden Schlüssel.
lager.setdefault("Apfel", 0)
lager.setdefault("Mango", 0)
lager.update({"Birne": 25, "Banane": 60})
print("Aktualisiert:", lager)

# get liefert für jeden Schlüssel den zu vergleichenden Bestand.
produkt = max(lager, key=lager.get)
print(f"Größter Bestand: {produkt} ({lager[produkt]})")
