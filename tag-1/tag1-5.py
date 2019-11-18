import re

text = "mein Name ist Willi Watz und meine email ist willi.watz-schulze-extern@firma.com"
muster = r"([a-z0-9]+)\.([a-z0-9]+(-([a-z0-9]+))?)-extern@firma\.com"

m = re.search(muster, text, re.IGNORECASE)

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))