def machwas(daten):
    if len(daten) != 5:
        raise Exception("invalid length", len(daten))
    for i, n in enumerate(daten):
      daten[i] = n + 1
    return daten



try:
  ergebnis = machwas([1,2,3,4,5])
  print(ergebnis)
  wert = 1 / 0
#except Exception as e:
#    print(e)
#    print("Es geht weiter")
finally:
  print("hier geht es immer durch")
