import sys

dateiname = sys.argv[1]
anzahl = int(sys.argv[2])

text = []
with open(dateiname) as fd:
    text = fd.readlines()

print(text[-1 * anzahl])