import random
import re

def _read_data(fname):
    with open(fname) as fd:
        daten = fd.readlines()
    return daten[0].strip("\n").split(",")

def _check_size(tipp):
    if len(tipp) != 6:
        raise Exception("invalid length", len(tipp))

def _check_numbers(tipp):
    for i in range(0, len(tipp)):
        if not re.search(r"[1-9]|[1-4][0-9]", tipp[i]):
            raise Exception("invalid data", tipp)

def _check_doubles(tipp):
    for i, zahl1 in enumerate(tipp):
        for j, zahl2 in enumerate(tipp):
            if i != j and zahl1 == zahl2:
                raise Exception("Doublette", zahl1)

def _convert_to_int(alt):
    neu = []
    for n in alt:
        neu.append(int(n))
    return neu

def read_tipp(fname):
    tipp = _read_data(fname)
    _check_size(tipp)
    _check_numbers(tipp)
    tipp = _convert_to_int(tipp)
    _check_doubles(tipp)
    return tipp

def lotto_ziehung():
    return random.sample(range(1, 50), 6)

def auswertung(tipp, ziehung):
    ergebnis = 0
    for zahl1 in tipp:
        for zahl2 in ziehung:
            if zahl1 == zahl2:
                ergebnis += 1
    return ergebnis

def main():
    try:
        tipp = read_tipp("tipp.csv")
        for n in range(1,100):
            ziehung = lotto_ziehung()
            print(n, auswertung(tipp, ziehung))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
