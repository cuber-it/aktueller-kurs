import lottolib

def play(anzahl=1):
    count = 0
    for n in range(0,anzahl):
        ziehung = lottolib.ziehung()
        ergebnis = lottolib.analyse(tipp, ziehung)
        if ergebnis["gewonnen"]:
            count += 1
            print(f"Tipp: #{n:>4}")
            lottolib.ausgabe_console(ergebnis)
    print(f"Insgesamt {count} Treffer")

tipp = lottolib.verify(lottolib.read_tipp("Bitte 6 durch Komma getrennte Zahlen 1-49: ", delim=","))
play(5000)

# für später: lottolib.ausgabe_json("Spiel6aus49.json", ergebnis, indent=4)
