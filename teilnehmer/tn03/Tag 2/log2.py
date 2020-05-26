path="/home/coder/aktueller-kurs/tag_2/SampleLog.log"

with open(path) as fd:
    lines = fd.readlines()
war = []
trc = []
lol = []
for line in lines:
    line = line.strip("\n")
    aktion = line[15:22]
    if aktion == "WARNING":
       date, typ, mess = line.split("WARNING")
       war.append({"date": date,"typ": typ, "mess": messs})
       print(war)

    elif aktion == "INFO   ":
       date, typ, mess = line.split("INFO   ")
       lol.append({"date": date,"typ": typ, "mess": messs})
       print(lol)

    elif aktion == "TRACE  ":
       date, typ, mess = line.split("TRACE  ")
       trc.append({"date": date,"typ": typ, "mess": messs})
       print(trc)
