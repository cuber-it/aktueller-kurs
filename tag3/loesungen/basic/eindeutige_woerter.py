"""Referenzlösung: Wörter und unterschiedliche Wörter zählen."""

text = "Die Katze sieht die Maus und die Maus sieht die Katze"
woerter = text.casefold().split()
eindeutig = set(woerter)

print("Wörter gesamt:", len(woerter))
print("Verschiedene Wörter:", len(eindeutig))
print("Alphabetisch:", ", ".join(sorted(eindeutig)))
