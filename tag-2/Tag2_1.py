import re

#text = "mein Name ist Willi Watz und meine email ist willi.watz-schulze-extern@firma.com"
#text = "mein Name ist Ulrich Cuber und meine email ist ulrich.cuber-extern@firma.com"
text = "meine Name ist ... und meine email ist herbert.walter.meier-extern@firma.com"
muster = r"([a-z]+)\.([a-z]+(-([a-z]+))?)-extern@firma\.com"

m = re.search(muster, text, re.IGNORECASE)

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))