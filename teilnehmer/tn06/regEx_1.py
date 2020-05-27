import os
import re
import sys

# korrekte Zeilen finden ^\d{2}/\d{2}

sys.path.insert(0,"/home/coder/aktueller-kurs/tag_3/")
import my_io

def read_log(logfile):
    return my_io.slurp(logfile, "LIST")

def clean_log(data):
    result = []
    for line in data:
        if re.search(r"^\d{2}/\d{2}", line):
            result.append(line)
    return result
    #return [line for line in data if re.search(r"^\d{2}/\d{2}", line)] #alternative

def write_log(logfile,data):
    my_io.spit(logfile,data)

if __name__ == "__main__":
    path = "/home/coder/aktueller-kurs/tag_2"
    file = "SampleLog.log"

    data = read_log(os.path.join(path,file))
    data = clean_log(data)
    write_log(os.path.join(path, "CleanData.log"),data)


