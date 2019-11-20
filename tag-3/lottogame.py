import sys
import re
import random

def prepare_input_numbers(eingabe):
    if len(eingabe) != 6:
        print("Es müssen genau 6 sein")
        sys.exit(1)

    zahlen = []
    for n in eingabe:
        if re.search("^\d\d?$", n):
            zahl = int(n)
            if zahl >= 1 and zahl <= 49:
                zahlen.append(zahl)
            else:
                print("nur werte zwischen 1 und 49")
                sys.exit(2)
        else:
            print("nur zahlen zwischen 1 und 49")
            sys.exit(3)

    if len(set(zahlen)) != 6:
        print("Es sollten schon 6 unterschiedliche sein!")
        sys.exit(4)
    return zahlen

def lotto_zahlen():
    return random.sample(list(range(1, 50)), 6)


if __name__ == "__main__":
    verbose = False
    if sys.argv[1] == "-v":
        verbose = True
        del sys.argv[1]
    if len(sys.argv) != 8:
        print("usage: {} [-v] anzahl_ziehung zahl1 .. zahl6".format(sys.argv[0]))
        sys.exit(-1)
    spiele = int(sys.argv[1])
    zahlen = prepare_input_numbers(sys.argv[2:])
    zahlen.sort()

    # matches = { "0":0, "1":0, "2":0 .... }

    matches = dict(
        zip(
            [str(n) for n in range(7)],
            [0]*7
        )
    )


    for n in range(spiele):
        ziehung = lotto_zahlen()
        treffer = len(set(zahlen).intersection(set(ziehung)))
        ziehung.sort()
        if verbose:
            print("{} - {} => {}".format(zahlen, ziehung, treffer))
        matches[str(treffer)] += 1

    for k, v in matches.items():
        print("{}er = {}".format(k, v))

    sys.exit(0)