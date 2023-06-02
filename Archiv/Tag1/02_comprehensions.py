# Creating a list of squares of numbers 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of even numbers from another list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# Creating a set of squares of numbers 0 to 9
squares = {x**2 for x in range(10)}
print(squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Creating a set of even numbers from another set
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
evens = {x for x in numbers if x % 2 == 0}
print(evens)  # Output: {2, 4, 6, 8, 10}

# Creating a generator that yields squares of numbers 0 to 9
squares = (x**2 for x in range(10))
for square in squares:
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

# Creating a dictionary of squares of numbers 0 to 9
squares = {x: x**2 for x in range(10)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Creating a dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # Output: {"a": 1, "b": 2, "c": 3}
