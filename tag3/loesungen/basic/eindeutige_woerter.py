"""Referenzlösung: Wörter und unterschiedliche Wörter zählen."""

text = "Die Katze sieht die Maus und die Maus sieht die Katze"
woerter = text.casefold().split()
eindeutig = set(woerter)

print("Wörter gesamt:", len(woerter))
print("Verschiedene Wörter:", len(eindeutig))
print("Alphabetisch:", ", ".join(sorted(eindeutig)))

# oder aber:

haeufigkeiten = {}

for wort in woerter:
    if wort in haeufigkeiten:
        haeufigkeiten[wort] += 1
    else:
        haeufigkeiten[wort] = 1

print("Gesamtzahl:", len(woerter))
print("Unterschiedliche Wörter:", len(haeufigkeiten))
print("Wörter:", ", ".join(sorted(haeufigkeiten)))
