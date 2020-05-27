import os
import re
import sys

sys.path.insert(0,"/home/coder/aktueller-kurs/tag_3")

import my_io

data = my_io.slurp("/home/coder/aktueller-kurs/tag_2/SampleLog.log","LIST")
result=[]
for line in data:
    if re.search(r"^\d\d/\d\d", line):
        result.append(line)
    print(result)
my_io.spit("/home/coder/aktueller-kurs/teilnehmer/tn03/Tag 3/logout.log", result)


