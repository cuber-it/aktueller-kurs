import math

breite = 61
hoehe = 15
mittelwert = 0.0
sigma = 1.0

raster = [[" " for _ in range(breite)] for _ in range(hoehe)]

for spalte in range(breite):
    x = mittelwert + (spalte / (breite - 1) * 6 - 3) * sigma
    y = math.exp(-0.5 * ((x - mittelwert) / sigma) ** 2)
    zeile = hoehe - 1 - round(y * (hoehe - 1))
    raster[zeile][spalte] = "*"

for zeile in raster:
    print("|" + "".join(zeile))

print("+" + "-" * breite)
print(" -3σ" + " " * 26 + "μ" + " " * 26 + "+3σ")
