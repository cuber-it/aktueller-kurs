print("|dez|x||dez|x||dez|x||dez|x|")

for zahl in range(32, 56):
    for spalte in range(4):
        dez = zahl + spalte * 24
        zeichen = chr(dez) if dez < 127 else "DEL"
        print(f"|{dez:3}|{zeichen:^3}|", end="")
    print()
