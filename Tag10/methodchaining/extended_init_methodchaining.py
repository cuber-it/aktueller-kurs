import init_methodchaining as im

class ExtendedDaten(im.Daten):
    pass

d1 = ExtendedDaten().init_texte("a", "b")
d2 = ExtendedDaten().init_werte(1, 2)
d3 = ExtendedDaten().init_texte("a", "b").init_werte(1, 2)
d4 = ExtendedDaten().init_texte("a").init_werte(1)
d5 = ExtendedDaten().init(1, 1, 1, "a", "b").init_werte(55).init_float(1.1, 1.2, 1.3)

print(d1.values())
print(d2.values())
print(d3.values())
print(d4.values())
print(d5.values())
