# Schritt 1: Ermittelt im Wertebreich von 32 bis 127 den dazu korrespondierenden Buchstaben und geb das aus
#
# Schritt 2: gebt das als Tabelle der Form aus:
#
# ----------------------------------------
# Code|Zeichen||Code|Zeichen||Code|Zeichen
#  32 | SPACE || 33 |   !   || 34 |  "
#  35 ............................
#  .........................|| 127 | DEL

# Lösung 1:
for i in range(32, 128):
      zeichen = chr(i)
      if i == 32:
        zeichen = "<SPACE>"
      elif i == 127:
        zeichen = "<DEL>"
      print(f"{i:3}: {zeichen}")

# Lösung 2:
print("=" * 51)
print(f" {'Code':>4} | {'Zeichen':^7} ||"
      f" {'Code':>4} | {'Zeichen':^7} ||"
      f" {'Code':>4} | {'Zeichen':^7}")
print("-" * 52)

for i in range(32, 128, 3):
   c1, c2, c3 = i, i+1, i+2

   z1 = "<SPACE>" if c1 == 32 else chr(c1)
   z2 = chr(c2)
   z3 = "<DEL>" if c3 == 127 else chr(c3)

   print(f" {c1:4} | {z1:^7} || {c2:4} | {z2:^7} || {c3:4} | {z3:^7}")
print("-" * 51)
