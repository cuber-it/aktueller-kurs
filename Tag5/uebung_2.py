import os
import sys
import glob
import hashlib

class FileComparer:
    def __init__(self, folder_a, folder_b, extensions):
        self.folders = [folder_a, folder_b]
        self.extensions = extensions
        self.results = {}

    def _getfiles(self, folder):
        files = []
        allfiles = glob.glob(os.path.join(folder, "*"))
        for f in allfiles:
            if os.path.isfile(f):
                files.append(f)
        return files


    def run(self):
        self.results = {}
        for folder in self.folders:
            for file in self._getfiles(folder):
                ext = os.path.splitext(file)[1]

                if ext[1:] in self.extensions:
                    path = os.path.join(folder, file)
                    md5 = hashlib.md5(open(path ,'rb').read()).hexdigest()
                    if not md5 in self.results:
                        self.results[md5] = []
                    self.results[md5].append(path)


    def report(self):
        for key, value in self.results.items():
            if len(value) > 1:
                print(value)


folder_a = r"S:\20_hugendubel"
folder_b = r"S:\00_all_epub"

comparer = FileComparer(folder_a, folder_b, ['jpg', 'mp3', 'epub'])
comparer.run()
comparer.report()

# Die Klasse Comparer sammelt alle Dateien in den beiden Foldern ein
# die genannten Dateiendungen werden dabei berücksichtigt
# dann werden die Dateien verglichen (Inhaltlich)
# Hinweis: um die Dateien zu vergleiche müssen sie nicht deren Inhalte direkt vergleichen
#          es reicht einen Kennwert zu ermitteln, der einmalig ist, z.B. MD5hash
#          Dateien mit gleichem md5hash sind inhaltlich gleich!
# der Bericht gibt alle Dateien aus, die in a und b doppelt sind
# Fundestellen_in_A, Fundstellen_in_B
# dateiname in folder_a, dateiname infolder_b