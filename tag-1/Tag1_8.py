import re

text = [
    "2020-10-22 STATUS: Eine Meldung 4711 mit System 0815",
    "2020-11-21 INFO: STATUS was printed"
]


for zeile in text:
    m = re.search(r"^(.*) (.*?):(.*)", zeile)
    if m.group(2) == "STATUS":
        print("{} -> {}".format(m.group(1), m.group(3)))
    else:
        print("NIX")

#for zeile in text:
#    akt_zeile = zeile.split()
#    if akt_zeile[1] == "STATUS:":
#        print(zeile)
#    else:
#        print("NIX")

#for zeile in text:
#    if zeile[11:17] == "STATUS":
#        print(zeile)
#    else:
#        print("NIX")


#for zeile in text:
#    if "STATUS" in zeile:
#        print(zeile)
#    else:
#        print("Nix")