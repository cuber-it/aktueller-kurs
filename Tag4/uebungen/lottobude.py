fname = "schein_a.csv"

# optional für Spielschein
class Tipp:
    pass

# 2.
class Spielschein:
    def __init__(self, fname):
        pass

    # 12 Tipps kann er speichern bzw. einen Spielschein einlesne und max 12 Tipps übernehmen
    def load(self):
        pass

    # für alle Tipps muss geprüft werden, ob sie valide sind
    def pruefen(self):
        pass

    # für alle Tipps die Ziehungsergebnisse vergleichen
    #def auswerten(self, ziehungs_ergebnis):
    #    pass

    def __str__(self):
        pass

# 1.
class Ziehung:
    def spielen(self):
        pass

    def auswerten(self, schein):
        pass

# 3.
class Bericht:
    def __init__(self, schein, ziehung):
        pass

    def asugeben(self):
        pass

#---------------------------------------------------------------------------------
schein = Spielschein(fname)
schein.laden()
schein.pruefen()

ziehung = Ziehung()
ziehung.spielen()

# schein.auswerten(ziehung)
ziehung.auswerten(schein)

Bericht(schein, ziehung).ausgeben()
