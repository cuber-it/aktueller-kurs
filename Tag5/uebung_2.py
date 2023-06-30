import os
import sys

class FileComparer:
    def __init__(self, folder_a, folder_b, extensions):
        pass

    def run(self):
        pass

    def report(self):
        pass


folder_a = "..."
folder_b = "..."

comparer = FileComparer(folder_a, folder_b, ['jpg', 'mp3'])
comparer.run()
comparer.report()

# Die Klasse Comparer sammelt alle Dateien in den beiden Foldern ein
# die genannten Dateiendungen werden dabei berücksichtigt
# dann werden die Dateien verglichen (Inhaltlich)
# Hinweis: um die Dateien zu vergleiche müssen sie nicht deren Inhalte direkt vergleichen
#          es reicht einen Kennwert zu ermitteln, der einmalig ist, z.B. MD5hash
#          Dateien mit gleichem md5hash sind inhaltlich gleich!
# der Bericht gibt alle Dateien aus, die in a und b doppelt sind
