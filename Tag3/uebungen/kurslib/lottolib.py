import json
import random

# Helper, sind hidden
def _convert(eingabe, delim=" "):
    return [int(z) for z in eingabe.split(delim)]

def _check_numbers_valid(data, min, max):
    if False in [n>=min and n<=max for n in data]:
        raise Exception("Ungültige Zahlen")
    return data

def _check_duplicates(data):
    if len(data) != len(set(data)):
        raise Exception("Doppelte Werte")
    return data

def _check_count(data, count):
    if len(data) != count:
        raise Exception(f"Falsche Anzahl {len(data)}")
    return data

# offizielle Schnittstelle
def verify(data, min=1, max=49, count=6):
    _check_count(data, count)
    _check_numbers_valid(data, min, max)
    _check_duplicates(data)
    return data

def read_tipp(prompt, delim=" "):
    return _convert(input(prompt), delim)

def ziehung(min=1, max=49, count=6):
    return random.sample(range(min, max+1), count)

def analyse(tipp, ziehung):
    treffer = list(set(tipp).intersection(set(ziehung)))
    return dict(
        tipp = tipp,
        ziehung = ziehung,
        treffer = treffer,
        gewonnen = 1 if len(treffer) >= 3 else 0
    )


def ausgabe_console(daten):
    print("Tipp:    ", daten["tipp"])
    print("Ziehung: ", daten["ziehung"])
    print("Treffer: ", daten["treffer"])
    print("Gewonnen:", "Ja" if daten["gewonnen"] == 1 else "Nein")

def ausgabe_json(dateiname, daten, **config):
    ausgabe = [
                daten
              ]
    with open(dateiname, "w") as fd:
        json.dump(ausgabe, fd, **config)
