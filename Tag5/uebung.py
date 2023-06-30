class Reader:
    def __init__(self, quelle=None):
        pass

    def read(self):
        # liest die Daten aus der Quelle
        #bereitet sie in das Rückgabeformat auf
        return [[],[],[],[]]

class CsvReader(Reader):
    # für CSV notwendige Dinge
    pass

class Writer:
    def __init__(self, target=None):
        pass

    def write(self, daten): # daten in der Form [[][][][]]
        pass

class FileWriter(Writer):
    # Für Dateiausgabe notwendige Dinge
    pass

#------------------------------------------------------
class Tabelle: # weiss nichts von Input und output, kennt sichnur mit Tabellen aus
    def __init__(self):
        pass

    # ...

    def load(self, reader_object):
        raw = reader_object.read()
        # Nach bereitung um intern zu speichern

    def dump(self, writer_object):
        # Vorbereitung der ausgabedaten
        ausgabedaten = [[],[],[]]
        writer_object.write(ausgabedaten)


 #-------------------------------------------
 # Anwendung
t = Tabelle()
t.load(CsvReader(r"E:\Workspaces\Kurse\aktueller-kurs\Tag4\uebungen\bsp.csv"))
#....
t.dump(FileWriter("table_dump.txt"))
