# Trinkgeldrechner

#  Aufgabe: Rechnungsbetrag, Prozentsatz und Personenzahl einlesen. Trinkgeld,
#  Gesamtsumme und Anteil pro Person ausgeben (auf 2 Nachkommastellen).
#  Eingabe: 42.50 / 10 / 3
#  Ausgabe: Trinkgeld: 4.25 EUR | Gesamt: 46.75 EUR | pro Person: 15.58 EUR

betrag = float(input("Betrag:").replace(",", "."))
prozentsatz = float(input("Prozent:")) / 100
personen = int(input("Personenzahl"))

if personen == 0:
    print("Falsche Personenzahl: ", personen)
    exit()

trinkgeld = betrag * prozentsatz
zahlbetrag = betrag + trinkgeld
pro_person = zahlbetrag / personen

print(f"{betrag:.2f} + {trinkgeld:.2f} = {zahlbetrag:.2f} d.i {pro_person:.2f} pro Person")
