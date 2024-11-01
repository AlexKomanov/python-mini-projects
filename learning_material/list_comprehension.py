# Syntax:
# new_list = [expression for item in iterable if condition]

# Using a regular loop
# numbers = [1, 2, 3, 4, 5]
# numbers_squares = []
# for number in numbers:
#     numbers_squares.append(number ** 2)
# print(f"{numbers_squares = }")
#
# # Using map function
# numbers = [1, 2, 3, 4, 5]
# numbers_squares = list(map(lambda x: x ** 2, numbers))
# print(f"Lambda + Map: {numbers_squares}")  # Output: [1, 4, 9, 16, 25]
#
# # Using List Comprehension
# numbers = [1, 2, 3, 4, 5]
# #       [expression for item in iterable if condition]
# squares = [number ** 2 for number in numbers]
# print(f"List Comprehension: {squares}")  # Output: [1, 4, 9, 16, 25]

# words = ["hello", "world", "python"]
# uppercased = [word.upper() for word in words]
# print(uppercased)  # Output ['HELLO', 'WORLD', 'PYTHON']


# If condition - filtering

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)  # Output [2, 4, 6]
#
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output [2, 4, 6]
#
# numbers = [1, 2, 3, 4, 5, 6]
# #               [expression for item in iterable if condition]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)  # Output [2, 4, 6]

# If Else condition - manipulation

numbers = [1, 2, 3, 4, 5, 6]
modified_numbers = []
for x in numbers:
    if x % 2 == 0:
        modified_numbers.append(x * 2)
    else:
        modified_numbers.append(None)

print(modified_numbers)

numbers = [1, 2, 3, 4, 5, 6]

modified_numbers = list(map(lambda i: i * 2 if i % 2 == 0 else None, numbers))

print(modified_numbers)

numbers = [1, 2, 3, 4, 5, 6]
      #        [expression for item in iterable if condition]
modified_numbers = [x * 2 if x % 2 == 0 else None for x in numbers]

# If without Else -> triggers error: # SyntaxError: expected 'else' after 'if' expression
# modified_numbers = [x * 2 if x % 2 == 0 for x in numbers]

print(modified_numbers)  # Output [None, 4, None, 8, None, 12]
