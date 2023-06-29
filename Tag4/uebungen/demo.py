fname = r"E:\Workspaces\Kurse\aktueller-kurs\Tag4\uebungen\schein_a.csv"

class Spielschein:
    def __init__(self, fname):
        self.fname = fname
        self.schein = [] # max 12 einzelne Tipps

    # 12 Tipps kann er speichern bzw. einen Spielschein einlesne und max 12 Tipps übernehmen
    def laden(self):
        with open(self.fname) as fd:
            daten = fd.read().splitlines()[:12] # max 12 Zeien in der Form "1,2,3,4,5,6"
        self.schein = []
        for zeile in daten:
            tipp = zeile.split(",") # aus "1,2,3,4,5,6" wird [1,2,3,4,5,6]
            self.schein.append(tipp)
        # ab hier:
        # schein => [ [ 1,2,3,4,5,6], [1,2,3,4,5,6]]
