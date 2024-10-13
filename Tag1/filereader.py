#!/usr/bin/env python3
import sys

#fd = None
#
#try:
#    fd = open(sys.argv[1])
#    inhalt = fd.read()
#finally:
#    if not fd is None:
#        fd.close()

# Eingabe aka slurp
with open(sys.argv[1]) as fd:
    inhalt = fd.read();

# Verarbeitung
print(inhalt[:100])

# Ausgabe aka spit
with open(sys.argv[1] + ".bak", 'w') as fd:
    fd.write(inhalt)