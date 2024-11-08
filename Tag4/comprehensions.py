werte = list(range(1, 100))

odd = []
for v in werte:
    if v % 2 != 0:
        odd.append(v)

print(odd)

# List- Comprehension - erzeugt Liste
even = [v for v in werte if v % 2 == 0]

print(even)

# Dict-Comprhension - erzeugt dict

even_squares = {f'Wert_von_{x}': x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)
print(even_squares.keys())
print(even_squares.values())




