"""Referenzlösung: Worthäufigkeiten ohne Satzzeichen auswerten."""

from collections import Counter
import re

text = """Python ist toll. Python ist einfach, und Python macht Spass!
Listen, Dicts und Sets sind toll."""

woerter = re.findall(r"[a-zäöüß]+", text.casefold())
haeufigkeit = Counter(woerter)

# Bei Gleichstand bewahrt most_common() die Reihenfolge des ersten Auftretens.
for nummer, (wort, anzahl) in enumerate(haeufigkeit.most_common(3), start=1):
    print(f"{nummer}. {wort} ({anzahl} x)")
