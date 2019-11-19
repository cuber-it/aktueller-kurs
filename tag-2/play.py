import sys
import re

eingabe = sys.argv[1:]

if len(eingabe) != 6:
    print("Es müssen genau 6 sein")
    sys.exit(1)

zahlen = []
for n in eingabe:
    if re.search("^\d\d?$", n):
        zahl = int(n)
        if zahl >= 1 and zahl <= 49:
            zahlen.append(zahl)
        else:
            print("nur werte zwischen 1 und 49")
            sys.exit(2)
    else:
        print("nur zahlen zwischen 1 und 49")
        sys.exit(3)

#if len(set(zahlen)) != 6:
#    print("Es sollten schon 6 unterschiedliche sein!")
#    sys.exit(4)

for i1, z1 in enumerate(zahlen):
    for i2, z2 in enumerate(zahlen):
        if i1 != i2 and z1 == z2:
            print("Keine doppelten!")
            sys.exit(4)

print(zahlen)
sys.exit(0)