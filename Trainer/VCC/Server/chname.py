#!/usr/bin/env python3
import os
import sys

for dir, subdirs, files in os.walk(sys.argv[1]):
	for file in files:
		path = os.path.join(dir, file)
		if file[-4:] == ".txt":
			newpath = path[:-4]
			print(file, newpath)
			os.rename(path, newpath)

