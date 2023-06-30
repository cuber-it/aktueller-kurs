import glob
import hashlib
import os
import sys
import argparse

class FileComparer:
    def __init__(self, folders, extensions):
        self.folders = folders
        self.extensions = extensions

    def run(self):
        self.results = {}
        for folder in self.folders:
            files = [file for file in glob.glob(os.path.join(folder, "*")) if os.path.isfile(file)]
            for file in files:
                ext = os.path.splitext(file)[1][1:]
                if ext in self.extensions:
                    md5_hash = hashlib.md5()
                    with open(file, 'rb') as f:
                        for chunk in iter(lambda: f.read(4096), b""):
                            md5_hash.update(chunk)
                    self.results.setdefault(md5_hash.hexdigest(), []).append(file)
        return self

    def report(self, target=sys.stdout):
        for files in self.results.values():
            if len(files) > 1:
                print(", ".join(files), file=target)
        return self

def main():
    parser = argparse.ArgumentParser(description='Compare files in two folders.')
    parser.add_argument('folders', metavar='F', type=str, nargs='+', help='a list of folders to compare')
    parser.add_argument('--extensions', type=str, nargs='+', default=['jpg', 'mp3', 'epub'], help='a list of file extensions to compare')
    args = parser.parse_args()

    comparer = FileComparer(args.folders, args.extensions)
    comparer.run().report()

if __name__ == "__main__":
    main()
