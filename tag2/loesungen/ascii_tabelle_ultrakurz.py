for zahl in range(32, 56): # 32-128/Zeich 127 inkl. mit 4 Spalten: start: 32, Ende 128 - 3 * 24
    print(
        f"|{zahl:3}|{chr(zahl)}|" # von 32 - 56
        f"|{zahl + 24:3}|{chr(zahl + 24)}|" # 32 + 24 - 56 + 24
        f"|{zahl + 48:3}|{chr(zahl + 48)}|" # 32 + 2 * 24 - 56 + 2 * 24
        f"|{zahl + 72:3}|{chr(zahl + 72)}|" # 32 + 3 * 24 - 56 + 3 * 24
    )
