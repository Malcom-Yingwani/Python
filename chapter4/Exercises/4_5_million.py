# printing and basic stats with the range 1 - 1_000_000

numbers = list(range(1, 1_000_00))

for number in numbers:
    print(number)

print(f'Min = {min(numbers)}\nMax = {max(numbers)}\nSum = {sum(numbers)}')
