import os
import sys
import glob
import hashlib
import argparse

class FileComparer:
    def __init__(self, folders, extensions):
        self.folders = folders
        self.extensions = extensions

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

def main():
    parser = argparse.ArgumentParser(description='Compare files in two folders.')
    parser.add_argument('folders', metavar='F', type=str, nargs='+', help='list of folders to compare')
    parser.add_argument('--extensions', type=str, nargs='+', default=['jpg', 'mp3', 'epub'], help='list of file extensions to compare')
    args = parser.parse_args()

    comparer = FileComparer(args.folders, args.extensions)
    comparer.run()
    comparer.report()

if __name__ == "__main__":
    main()

# Aufruf auf der Kommandozeile: python script.py folder_a folder_b --extensions jpg mp3 epub
