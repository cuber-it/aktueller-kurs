spalten = 4

kopf = " " + " || ".join([f"{'Code':>4} | {'Zeichen':^7}"] * spalten)
breite = len(kopf)

print(kopf)
print("-" * breite)

for i in range(32, 128, spalten):
    print(" " + " || ".join(
        f"{j:4} | {chr(j):^7}"
        for j in range(i, min(i + spalten, 128)) # List-Comprehension - Abgekürzte Listenerstellung mittels for
    ))

print("-" * breite)
