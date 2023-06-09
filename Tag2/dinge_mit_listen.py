log_path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\Sample.log"

with open(log_path) as fd:
    raw = fd.read().splitlines()

daten_1 = []
for line in raw:
    if "INFO" in line:
        daten_1.append(line.split(maxsplit=3))

# List Comprehension = Abkürzung für den Code im Stil wie oben
daten_2 = [line.split(maxsplit=3) for line in raw if "INFO" in line]

print(daten_1 == daten_2)
print(daten_1[5])
print(daten_2[5])
