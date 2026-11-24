# Tag 3 – Dictionaries: zählen und gruppieren
# Zuordnungen lassen sich erzeugen, als Zähler nutzen und gruppieren.

from collections import Counter, defaultdict

woerter = ["Apfel", "Birne", "Apfel", "Kirsche", "Birne"]
laengen = {wort: len(wort) for wort in woerter}
print("Wortlängen:", laengen)

haeufigkeit = {}
for wort in woerter:
    haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1
print("Mit Dictionary gezählt:", haeufigkeit)

zaehler = Counter(woerter)
print("Mit Counter gezählt:", dict(zaehler))
print("Die zwei häufigsten:", zaehler.most_common(2))

gruppen = defaultdict(list)
for wort in ["Apfel", "Ananas", "Birne", "Banane"]:
    gruppen[wort[0]].append(wort)
print("Nach Anfangsbuchstaben:", dict(gruppen))

for wort in sorted(haeufigkeit, key=haeufigkeit.get, reverse=True):
    print(f"{wort}: {haeufigkeit[wort]}")
