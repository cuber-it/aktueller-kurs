# Tag 1 – f-Strings (formatierte Strings)
#
# Mit f"..." lassen sich Werte direkt in einen Text einsetzen.

name = "Ulrich"
alter = 42

# Variablen einsetzen
print(f"Hallo {name}, du bist {alter} Jahre alt.")

# Auch Ausdrücke sind erlaubt
print(f"Nächstes Jahr bist du {alter + 1}.")

# Zahlen formatieren
preis = 3.14159
print(f"Preis: {preis:.2f} EUR")        # zwei Nachkommastellen -> 3.14
print(f"Mit Vorzeichen: {preis:+.2f}")

# Breite / Auffüllen (für tabellarische Ausgaben)
print(f"|{'Name':<10}|{'Alter':>5}|")
print(f"|{name:<10}|{alter:>5}|")

# Hinweis: vor f-Strings gab es % und .format() –
# du wirst sie in altem Code sehen, wir verwenden f-Strings.
