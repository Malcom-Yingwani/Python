# Restaurant seating
reservation = input("How many people will be joining you for dinner? ")
reservation = int(reservation)

if reservation > 8:
    print("You'll need to wait for a table.")
else:
    print("Your table is ready.")