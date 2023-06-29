class DataSet:
    def __init__(self):
        self._daten = dict()

    def set(self, field, value):
        self._daten[field] = value
        return self

    def get(self, field):
        return self._daten.get(field, None)

    def __str__(self):
        return str(self._daten)

tabelle= []
for n in range(0, 3):
    tabelle.append(DataSet())

tabelle[-1].set("Name", "Willi")
print(tabelle[-1].get("Name"))
print(tabelle[-1])

# print(tabelle[-1]._daten) # Nein, nicht machen, da "hidden"!!
