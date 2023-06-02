# Define a function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to create a new list of even numbers
even_numbers = list(filter(is_even, numbers))

# Print the new list
print(even_numbers)

#--------------------------------------------
# Define a function to square a number
def square(number):
    return number ** 2

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to create a new list of squared numbers
squared_numbers = list(map(square, numbers))

# Print the new list
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
