a = "a"
b = 10
e = None

try:
    e = b / a
    print(e)
# except: - ganz schlecht i.A.
# except Exception - genauso schlecht
except ZeroDivisionError as e: # - seien Sie spezifisch! - ist aber optional wenn finally vorhanden
    print("Dumm gelaufen")
    # Das Skript läuft weiter ...
    # option a: Skrit beenden: exit(1) oder sys.exit(1)
    # option b: weiterwerfen z.B. mit raise e
except TypeError as e:
    print("Was anderes dumm gelaufen")
finally: # wird IMMER!! ausgeführt - optiona, wenn except vorhanden
    print("Wird immer ausgeführt")
