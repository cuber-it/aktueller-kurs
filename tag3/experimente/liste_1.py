# Experiment – Eine Liste kann unterschiedliche Typen enthalten
# Bei der inneren Liste ist ein weiterer Zugriffsschritt erforderlich.

werte = [4711, "Text", 12.34, ["Apfel", "Birne"]]
for wert in werte:
    print(type(wert).__name__, wert)
    if isinstance(wert, list):
        for eintrag in wert:
            print("  Inneres Element:", eintrag)
