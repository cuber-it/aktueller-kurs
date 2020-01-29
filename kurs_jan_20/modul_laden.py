import sys
import lottobude
print(dir())
lottobude.main()


#try:
#    tipp = lottobude.read_tipp("tipp.csv")
#    for n in range(1, 100):
#        ziehung = lottobude.lotto_ziehung()
#        print(n, lottobude.auswertung(tipp, ziehung))
#except Exception as e:
#    print(e)