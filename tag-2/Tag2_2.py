# Creating lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [1, 2]]
list_of_lists = [[0], [0, 1], [0, 1, 2]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))

# Accessing items
letters = ["a", "b", "c", "d"]
letters[0]  # "a"
letters[-1]  # "d"

# Slicing lists
letters[0:3]  # "a", "b", "c"
letters[:3]  # "a", "b", "c"
letters[0:]  # "a", "b", "c", "d"
letters[:]  # "a", "b", "c", "d"
letters[::2]  # "a", "c"
letters[::-1]  # "d", "c", "b", "a"

# Unpacking
first, second, *other = letters

# Looping over lists
for letter in letters:
    ...

for index, letter in enumerate(letters):
    ...

# Adding items
letters.append("e")
letters.insert(0, "-")

# Removing items
letters.pop()
letters.pop(0)
letters.remove("b")
del letters[0:3]

# Finding items
if "f" in letters:
    letters.index("f")

# Sorting lists
letters.sort()
letters.sort(reverse=True)

# Custom sorting
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]

items.sort(key=lambda item: item[1])