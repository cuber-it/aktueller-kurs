import os
import sys

# simuliert gewissermassen pythonpath
my_lib = r"E:\Workspaces\Kurse\aktueller-kurs\Tag3\lottobude"
sys.path.append(my_lib)
print(sys.path)

import lottoengine
import file_reader as reader
import writer

if __name__ == "__main__":
    lotto = lottoengine.LottoEngine()
    reader = reader.Reader("daten.txt")
    for n in range(0, 10):
        lotto.read(reader).play().write(writer.Writer(f"Spiel {n+1}"))
