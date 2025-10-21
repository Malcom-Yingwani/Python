# copying lists and proving that they are now different

my_pizzas = ['chicken', 'haiwan', 'bacon & avo']
friends_pizzas = my_pizzas[:]

my_pizzas.append('beef')
friends_pizzas.append('vegetarian')

print('My favorite pizzas:')
for pizza in my_pizzas:
    print(pizza)
    
print('\n')

print("My friend's favorite pizzas:")
for pizza in friends_pizzas:
    print(pizza)