import pprint

text = "2020-10-22 STATUS: Eine Meldung 4711 mit System 0815"

print(text[0])
print(text[-1])
print(text[11:17])
print(text.split())
print(text.split(":"))
pprint.pprint(text.split())
