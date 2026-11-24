# Tag 3 – Dictionaries: Grundlagen
# Ein Dictionary ordnet eindeutigen, hashbaren Schlüsseln Werte zu.

person = {"name": "Anna", "alter": 30}
print("Name:", person["name"])
print("Fehlendes Feld:", person.get("beruf"))
print("Mit Standardwert:", person.get("beruf", "unbekannt"))

person["beruf"] = "Entwicklerin"
person["alter"] = 31
print("Nach dem Ändern:", person)

# in prüft die Schlüssel, nicht die Werte.
print("Schlüssel name vorhanden:", "name" in person)
print("Wert Anna als Schlüssel vorhanden:", "Anna" in person)

beruf = person.pop("beruf")
print("Entfernter Beruf:", beruf)
print("Verbleibende Paare:", person)
print("Anzahl:", len(person))

try:
    print(person["beruf"])
except KeyError:
    print("Der Schlüssel beruf fehlt.")
