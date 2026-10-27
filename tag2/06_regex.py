# Tag 2 – Regex (Anriss): Suche mit Mustern
#
# Regex = "Regular Expressions". Eine kompakte Sprache, um Muster
# in Texten zu beschreiben – z. B. "alle Postleitzahlen",
# "alle E-Mails", "alle Zahlen". In Python im Modul "re".

import re

# --- re.search: erstes Vorkommen ---
# Liefert ein Match-Objekt oder None.

text = "Mein Geburtstag ist am 15.05.1980 in Berlin."
treffer = re.search(r"\d\d\.\d\d\.\d\d\d\d", text)
if treffer:
    print(f"Datum gefunden: {treffer.group()}")

# r"..."  = "raw string", damit \d nicht als Python-Escape interpretiert wird.

# --- re.findall: alle Treffer als Liste ---
text = "Telefon: 030-12345, Mobil: 0171-9876543"
nummern = re.findall(r"\d+", text)
print(nummern)            # ['030', '12345', '0171', '9876543']
# (\+\d{2}|0)-?(\d{2,5})-(\d{4,8}) - findet auch mit Ländervorwahl!

# --- Wichtigste Bausteine ---
#
#   .       beliebiges Zeichen (außer \n)
#   \d      eine Ziffer (0-9)
#   \w      Buchstabe, Ziffer, _
#   \s      Whitespace
#   [abc]   eines der Zeichen a, b, c
#   [a-z]   Bereich
#   ^  $    Anfang / Ende
#   \b      Wortgrenze
#
# Quantifizierer (für das Zeichen davor):
#
#   *       0 oder mehr
#   +       1 oder mehr
#   ?       0 oder 1
#   {n}     genau n
#   {n,m}   n bis m

# --- Beispiele ---

# deutsche Postleitzahl: genau 5 Ziffern
plz = re.search(r"\b\d{5}\b", "Wir wohnen in 10115 Berlin")
print(plz.group() if plz else "keine PLZ")

# E-Mails (sehr vereinfacht!)
emails = re.findall(r"\S+@\S+\.\S+", "Kontakt: max@uc-it.de oder admin@example.org")
print(emails)

# --- re.sub: ersetzen ---
zensiert = re.sub(r"\d", "*", "PIN: 1234")
print(zensiert)           # 'PIN: ****'

# alle Nicht-Ziffern entfernen
print(re.sub(r"\D", "", "Tel: 030-12 34 567"))   # '0301234567'

# --- Achtung ---
# "Echte" Validierung von E-Mails, IBANs etc. mit Regex ist ein
# Wespennest. Für einfache Suche/Extraktion super – für strikte
# Validierung lieber spezialisierte Bibliotheken.
