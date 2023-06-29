fname = r"E:\Workspaces\Kurse\aktueller-kurs\Tag4\uebungen\schein_a.csv"

# optional für Spielschein
class Tipp:
    pass

# 2.
MIN_TREFFER = 3
MAX_TIPP_PER_SCHEIN = 12

class Spielschein:
    def __init__(self, fname):
        self.fname = fname
        self.schein = []
        self.pruef_ergebnis = []
        self.ergebnis = []

    # 12 Tipps kann er speichern bzw. einen Spielschein einlesne und max 12 Tipps übernehmen
    def laden(self):
        with open(self.fname) as fd:
            self.schein = [line.split(",") for line in fd.read().splitlines()[:MAX_TIPP_PER_SCHEIN]]
        return self

    def _check_count(self, zahlen):
        if len(zahlen) != 6:
            raise ValueError(f"Anzahl stimmt nicht: {len(zahlen)}")

    def _check_for_values(self, zahlen):
        for zahl in zahlen:
            if zahl < 1 or zahl > 49:
                raise ValueError(f"Zahlenwert stimmt nicht: {zahl}")

    def _check_for_duplicates(self, zahlen):
        for zahl in zahlen:
            if zahlen.count(zahl) > 1:
                raise ValueError(f"Dopplter Wert: {zahl}")

    # für alle Tipps muss geprüft werden, ob sie valide sind
    def pruefen(self):
        geprueft = []
        self.pruef_ergebnis = []
        for line in self.schein:
            try:
                # Anzahl stimmt?
                self._check_count(line)
                # Typumwandlung als erstes!
                zahlen = [int(zahl) for zahl in line]
                self._check_for_values(zahlen)
                self._check_for_duplicates(zahlen)
                geprueft.append(zahlen)
                self.pruef_ergebnis.append((line, "ok"))
            except ValueError as e:
                self.pruef_ergebnis.append((line, e.args))
        self.schein = geprueft

    # für alle Tipps die Ziehungsergebnisse vergleichen
    def auswerten(self, ziehungs_ergebnis):
        self.ergebnis = []
        for tipp in self.schein:
            treffer = len(list(set(tipp).intersection(set(ziehungs_ergebnis))))
            if  treffer >= MIN_TREFFER:
                self.ergebnis.append((treffer, tipp))

    def __str__(self):
        s = ""
        for tipp in self.schein:
            s += str(tipp) + "\n"
        return s


import random

class Ziehung:
    ziehungs_ergebnis = []

    def spielen(self):
        self.ziehungs_ergebnis = random.sample(range(1, 50), 6)

    def __str__(self): # wird durch die Funktin str() aufgerufen
        return str(self.ziehungs_ergebnis)

# 3.
class Bericht:
    def __init__(self, schein, ziehung):
        self.schein = schein.ergebnis
        self.ziehung = ziehung.ziehungs_ergebnis

    def ausgeben(self):
        print("Ziehung: ", self.ziehung)
        for tipp in self.schein:
            print(tipp[1], "ergab", tipp[0], "Richtige")

#---------------------------------------------------------------------------------
schein = Spielschein(fname)
schein.laden()
schein.pruefen()
print(schein)
print(schein.pruef_ergebnis)

ziehung = Ziehung()
ziehung.spielen()
print(ziehung)

schein.auswerten(ziehung.ziehungs_ergebnis)

Bericht(schein, ziehung).ausgeben()
