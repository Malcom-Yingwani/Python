# Pizza toppings, using user input to 'quit'

topping = input("What toppings would you like on your pizza? ")

while topping != 'quit':
    print(f"We'll add {topping} to your pizza")
    topping = input("What toppings would you like on your pizza? ")
    
