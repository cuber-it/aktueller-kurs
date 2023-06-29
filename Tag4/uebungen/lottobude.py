fname = "schein_a.csv"

# optional für Spielschein
class Tipp:
    pass

# 2.
class Spielschein:
    pass

# 1.
class Ziehung:
    pass

# 3.
class Bericht:
    pass

schein = Spielschein(fname)
schein.laden()
schein.pruefen()

ziehung = Ziehung()
ziehung.spielen()

schein.auswerten(ziehung)

Bericht(schein, ziehung).ausgeben()
