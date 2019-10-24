d = {
    "Name": "Watz",
    "Vorname": "Willi",
    "Strasse": "Weg 1"
}

print(d["Name"])
print(d.keys())
print(d.values())

d["Ort"] = "Watzingen"

print(d.keys())
print(d.values())

d = {
    "Name" : [ "Meier", "Schulze", "Lehmann"]
}

print(d.keys())
print(d.values())
print(d["Name"][-1])

d = [
    { "Name": "Meier"},
    { "Name": "Schulze"},
    { "Name": "Lehmann"}
]