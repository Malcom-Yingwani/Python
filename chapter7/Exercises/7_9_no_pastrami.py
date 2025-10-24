sandwich_orders = ['PB & J', 'pastrami', 'grilled cheese','pastrami' ,'polony', 'chicken & mayo', 'eggs & mayo', 'pastrami']
finished_sandwiches = []

print("Sorry we're out of Pastrami Sandwiches")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print()
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich.title()} sandwich is ready")
    finished_sandwiches.append(sandwich)


print("\nSandwiches made:")
for ready in finished_sandwiches:
    print(ready.title())