log_path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\Sample.log"

with open(log_path) as fd:
    raw = fd.read().splitlines()

daten = []
for line in raw:
    words = line.split(maxsplit=3)
    daten.append(words)

for nr, zeile in enumerate(daten):
    if ":" in zeile[2]:
        bearbeitet = zeile[2].split(":", 1)
        repariert = zeile[:2] + [bearbeitet[0]] + [" ".join([":", bearbeitet[-1], zeile[-1]])]
        daten[nr] = repariert

for nr, zeile in enumerate(daten):
    print(f"{nr:>5} - {zeile}")

event_count = {}
for zeile in daten:
    event = zeile[2]
    #if event not in event_count:
    #    event_count[event] = 0
    #event_count[event] += 1

    event_count[event] = event_count.get(event, 0) + 1

for key, value in event_count.items():
    print(key, value)
