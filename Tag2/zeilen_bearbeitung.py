zeile = "165767;bln90us001.lan.idg.db.de;172.21.5.12;255.255.255.128;;GS0012001657;DB_BKU;Smart-UPS_2200VA-Netz;APC;172.21.5.0;DE;10785;Berlin;Potsdamer_Platz_2;1478;Sony_Center;02;02.VT-Raum;;SL1-PL2:DB_BKU;99999999;;;BLN90US001;Chassis;;L165767;Betrieb;Netzwerk_59_Sonstige;;;;;6033;;Zusatzgeraet;;RO5464;;BLN090;18.09.2022;;Unbekannt;DB_Systel_GmbH;GS0012001657;230609;"



teile = zeile.split(";")

if teile[2] == "172.21.5.12": # wenn xx.xx.xx.xx an position 3 vorkommt
    print("Ja", teile[8])

if "172.21.5.12" in zeile: # wenn xx.xx.xx.xx irgendwo vorkommt
    print("Ja", zeile)
