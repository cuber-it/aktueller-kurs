#!/usr/bin/env python3
import random

def read_tippschein(fname: str) -> list:
    """
    Liest einen Tippschein ein

    Parameter:
        fname - Dateiname

    Rückgabe:
        Liste von Strings
    """
    result = []
    with open(fname) as fd:
        result = fd.read().splitlines()
    return result

def check_tipp(tipp: list) -> list:
    """
    Prüft einen Tipp auf Validität
    """
    neuer_tipp = []
    if len(tipp) != 6:
        raise Exception(f"Anzahl Felder stimmt nicht: {len(tipp)}")
    for zahl in tipp:
        try:
            zahl = int(zahl)
            if zahl < 1 or zahl > 49:
                raise ValueError()
            if zahl in neuer_tipp:
                raise Exception(f"Doubletten im Tipp: {zahl}")
            neuer_tipp.append(zahl)
        except ValueError as e:
            raise Exception(f"Ungültiger Feldwert: {zahl}")
    return neuer_tipp

def prepare_tippschein(tippschein: list) -> list:
    """
    Bereitet Tippschein für Ziehung vor
    Prüft dass Tipps valide sind

    Parameter:
        tippschein - max. 12 Tipps

    Return:
        Die aufbereiteten Tipps im Tippschein

    """
    neuer_tippschein = []
    if len(tippschein) > 12:
        raise Exception("Tippschein hat mehr als 12 Tipps")
    for tipp in tippschein:
        tipp = tipp.split(",")
        tipp = check_tipp(tipp)
        neuer_tippschein.append(tipp)
    return neuer_tippschein

def ziehung():
    return random.sample(range(1,50),6)

def vergleicher(tipp, ziehung):
    return len(set(tipp).intersection(set(ziehung)))

def spiel(lottoschein):
    result = []

    aktuelle_zahlen = ziehung()

    for tipp in lottoschein:
        result.append(vergleicher(tipp, aktuelle_zahlen))

    return aktuelle_zahlen, result

def bericht(ziehung, lottoschein, treffer):
    print("Lottoziehung: ", ziehung)
    print("-"*40)
    for i in range(0, len(lottoschein)):
        print("Tipp: ", lottoschein[i], " - Treffer: ", treffer[i])

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) != 2:
        print(f"usage: {os.path.basename(sys.argv[0])} tippschein_datei")
        exit(1)

    # E ingabe
    tippschein = read_tippschein(sys.argv[1])
    tippschein = prepare_tippschein(tippschein)

    # V erarbeitung
    aktuelle_zahlen, ergebnisse = spiel(tippschein)

    # A usgabe
    bericht(aktuelle_zahlen, tippschein, ergebnisse)