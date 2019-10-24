import os.path
import os
import glob

fname = os.path.join("a", "b", "c")
print(fname)
print(os.path.isdir(r"C:\\"))

print(glob.glob("c:\\*"))

rootDir = 'c:\\'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)