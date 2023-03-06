# Create a list, a tuple, and a set with the same elements
my_list = [1, 2, 3, 3, 4, 5]
my_tuple = (1, 2, 3, 3, 4, 5)
my_set = {1, 2, 3, 3, 4, 5}

# Print the elements in each data structure
print("List:")
for x in my_list:
    print(x)
print("Tuple:")
for x in my_tuple:
    print(x)
print("Set:")
for x in my_set:
    print(x)

# Access the second element in each data structure
print("Second element:")
print(my_list[1])
print(my_tuple[1])
# sets are unordered so you cannot access by index

# Check if 3 is in each data structure
print("Contains 3:")
print(3 in my_list)
print(3 in my_tuple)
print(3 in my_set)

# Add an element to each data structure
my_list.append(6)
# tuples are immutable so they cannot be modified after creation
my_set.add(6)

# Print the updated data structures
print("Updated list:", my_list)
print("Updated set:", my_set)
