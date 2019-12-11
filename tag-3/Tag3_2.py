import sys
#print(sys.path)

import Incr

i = Incr.Incr(1000)

for n in range(200):
    i.calc()

i.show()