import re

text = "mein Name ist Willi Watz und meine email ist willi.watz-schulze-extern@firma.com"
muster = r"([a-z]+)\.([a-z]+(-([a-z]+))?)-extern@firma\.com"

m = re.search(muster, text)
print(m[0])
print(m[1])
print(m[2])
print(m[3])
print(m[4])