import re

# Vier Zahlen mit jeweils 1 bis 3 Ziffern, getrennt durch Punkte.
ip_muster = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# Logdatei öffnen und zeilenweise lesen.
with open("/home/ucuber/Workspace/kurse/kurse/aktueller-kurs/materialien/small_sample.log", "r", encoding="utf-8") as logdatei:
    znr = 0
    for zeile in logdatei:
        znr += 1
        # Nur Zeilen ausgeben, die mindestens ein IPv4-Muster enthalten.
        if re.search(ip_muster, zeile):
            print(znr, zeile, end="")
