# NUMERICAL LISTS
#Using range() functions

# Using range to make list of numbers
numbers = list(range(1, 6))
print(numbers)

print('\n')
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print('\n')
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)


print(squares)
print('\n')
# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f'Min = {min(digits)}')
print(f'Max = {sum(digits)}')
print(f'Sum = {sum(digits)}')

# List Comprehension
print('\n')
squares = [value**2 for value in range(1, 11)]
print(squares)
