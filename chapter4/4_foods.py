# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # [:] creates a slice from beginning to end. An exact copy

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\n')

my_foods.append('chocolate')
print(f'My favorite foods are \n{my_foods}')
print(f'\nMy friends favourite foods are : \n{friend_foods}')
