# Tag 1 – Variablen
#
# Eine Variable ist ein Name für einen Wert.
# Python ist dynamisch typisiert: derselbe Name darf
# später auf einen Wert eines anderen Typs zeigen.

# Zuweisung mit "="
name = "Ulrich"
alter = 42
groesse = 1.83
ist_dozent = True

print("Werte:", name, alter, groesse, ist_dozent)

# Mehrere Zuweisungen auf einmal
a, b, c = 1, 2, 3

print(a, b, c)

# Werte ändern (auch der Typ darf wechseln)
zahl = 10
print(zahl)

zahl = "jetzt ein Text"
print(zahl)

# Mit type() lässt sich der aktuelle Typ prüfen
print(type(name))
print(type(alter))
print(type(zahl))

# Konvention: snake_case für Variablennamen
mein_lieblings_essen = "Pasta"
print(mein_lieblings_essen)

# Konvention: "Konstante Werte"
# statt pi = 3.14 => PI = 3.14, bleibt aber  veränderbar! Konvention
PI = 3.14
print(PI, type(PI))

PI = "Willi" # !!!! AUTSCH! KONVENTION beachten
print(PI)

