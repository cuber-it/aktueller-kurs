#!/usr/bin/python3
import sys
import os
print(os.environ["PATH"])

print("args", sys.argv)
for a in sys.argv[1:]:
    print(a)