#!usr/bin/python3
path = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"

Wort = None

with open(path) as file_handle:
    zeilen = []
    
    for zeile in file_handle:
        while Wort != "Exit":
            Wort = input("Welches Wort möchten Sie suchen? ")
            #if Wort in zeilen:
            zeilen.append(zeile.strip())
            print(zeilen)

















#i = 0 
#Wort = input("Nach welchem Wort wollen sie suchen?")
#Li = []
#Wort = None

#with open(path) as fd:
#    zeilen = fd.readlines()

#for zeile in zeilen:
 #   zeile = zeile.strip("\n")
    #Li.append(zeile.split(";"))
 #   while Wort != "Exit":
 #       Wort = input("Wort eingeben: ")
  #      for Wort in zeile:
   #         print(zeile)
    #        break



