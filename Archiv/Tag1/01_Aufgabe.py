log = open(r"E:\Workspaces\Kurse\aktueller-kurs\Material\Sample.log").read()
events = [zeile[14:22].strip() for zeile in log.splitlines()]

print(len(events))

def counter(daten):
    result = {}

    for x in daten:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1

    return result

r = counter(events)

print(r)
