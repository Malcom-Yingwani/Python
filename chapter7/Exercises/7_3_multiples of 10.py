# Multiples of 10
number = int(input("Input a number you'd like to check: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")