topping = "\nEnter 'quit' to stop ordering"
topping += "\nWhat toppings would you like on your pizza? "

still_ordering = True

while still_ordering:
    order = input(topping)
    if order == 'quit':
        still_ordering = False
    else:
        print(f"We'll add {order} to your pizza")
        
    