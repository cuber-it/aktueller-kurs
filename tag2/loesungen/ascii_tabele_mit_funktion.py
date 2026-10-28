def display_ASCII(i):
    if i == 32:
        return "<SPACE>"
    elif i == 127:
        return "<DEL>"
    else:
        return chr(i)

"""
# Schritt 1
print("ASCII-Tabelle")
for i in range(32, 128):
    print(f"{i:>3} {display_ASCII(i)}")
"""

# Schritt 2
print("\nASCII-Tabelle mit 3 Spalten:")
print(f"{'Code':>3} {'Zeichen':^7} {'Code':>3} {'Zeichen':^7} {'Code':>3} {'Zeichen':^7}")
for start in range(32, 128, 3):
    a = start
    b = start + 1
    c = start + 2
    print(f"{a:>3} {display_ASCII(a):^7} {b:>3} {display_ASCII(b):^7} {c:>3} {display_ASCII(c):^7}")
