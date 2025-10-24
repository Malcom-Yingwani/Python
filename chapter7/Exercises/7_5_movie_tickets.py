prompt = "\nEnter'quit' if you do not wish to proceed"
prompt += "\nPlease enter your age: "


while True:
    age = int(input(prompt))

    if age == 'quit':
        break
    elif age < 3:
        print("\nYour ticket is free")
    elif age <= 12:
        print("\nYour ticket is $10.")
    elif age > 12:
        print("\nYour ticket is $15") 

