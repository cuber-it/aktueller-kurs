import my_io_2
import re

# sample log einlesen ohne "müllzeichen"

# Müll wird gekennzeichnet durch    ^ *(\d{2})? *$
# korrkte Zeilen finden             ^\d{2}/\d{2}

# Einlesen der sample log mit slurp als liste
l = []
l = my_io_2.slurp("/home/coder/aktueller-kurs/tag_1/SampleLog.log","LIST")

# Anlage einer neuen liste in der nur noch valide zeilen sind
l_valide = []
for line in l:
    if re.search(r"\d{2}/\d{2}",line):
        l_valide.append(line)
        # print(line)   
print("{} Zeilen -> {} Zeilen ".format(len(l), len(l_valide)))

# Ausgabe der validen liste mittels spit
my_io_2.spit("/home/coder/aktueller-kurs/teilnehmer/tn08/samplelog_valide.log",l_valide)
