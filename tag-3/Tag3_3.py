import LottoEngine as LE

ergebnisse = LE.new_result_dict()

t = LE.tippeingabe(sorted=True)

for n in range(1000):
    z = LE.ziehung(sorted=True)
    ergebnis = LE.auswertung(t, z)
    ergebnisse[str(ergebnis)] += 1
    print("{} {} -> {}".format(t, z, ergebnis))

for k, v in ergebnisse.items():
    print("{} -> {}".format(k, v))
