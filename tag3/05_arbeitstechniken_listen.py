# Tag 3 – Listen auswerten
# Comprehensions erzeugen Listen; enumerate() und zip() unterstützen Schleifen.

zahlen = [1, 2, 3, 4, 5, 6]
quadrate = []
for zahl in zahlen:
    quadrate.append(zahl ** 2)
print("Mit Schleife:", quadrate)
print("Mit Comprehension:", [zahl ** 2 for zahl in zahlen])
print("Gerade Zahlen:", [zahl for zahl in zahlen if zahl % 2 == 0])

obst = ["Apfel", "Birne", "Kirsche"]
for nummer, name in enumerate(obst, start=1):
    print(f"{nummer}. {name}")

preise = [2.50, 1.20, 3.00]
# strict=True meldet unterschiedliche Längen mit ValueError.
for name, preis in zip(obst, preise, strict=True):
    print(f"{name}: {preis:.2f}")

# key=len verwendet die Wortlänge als Sortierkriterium.
woerter = ["Banane", "Ei", "Apfel"]
print("Nach Länge:", sorted(woerter, key=len))
print("Ursprüngliche Reihenfolge:", woerter)

werte = [10, 5, 8, 3]
print("Summe:", sum(werte))
print("Minimum und Maximum:", min(werte), max(werte))
print("Mittelwert:", sum(werte) / len(werte))
