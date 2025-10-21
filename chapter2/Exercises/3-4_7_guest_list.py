# 3-4 Invite list
guests = ['dave', 'ramon', 'jim', 'james', 'isabela', 'mcain']
print(f'{guests[0]}, you are invited')
print(f'{guests[1]}, you are invited')
print(f'{guests[2]}, you are invited')
print(f'{guests[3]}, you are invited')
print(f'{guests[4]}, you are invited')
print(f'{guests[5]}, you are invited')

# 3-5 Changing guest
print('\n')
print(f'{guests[5]}, cannot come')
guests[5] = 'taylor'
print(f'{guests[5]}, you are invited')

# 3-6 Adding more guests
print(f'\nI found a bigger table!')
guests.insert(0, 'jane')
guests.insert(4, 'ben')
guests.append('dekard')
print(f'{guests[0]}, you are invited')
print(f'{guests[1]}, you are invited')
print(f'{guests[2]}, you are invited')
print(f'{guests[3]}, you are invited')
print(f'{guests[4]}, you are invited')
print(f'{guests[5]}, you are invited')
print(f'{guests[6]}, you are invited')
print(f'{guests[7]}, you are invited')
print(f'{guests[8]}, you are invited')


# 3-7 shrinking guest list
print('\n')
print('unfortunately, I can only invite six people')
print(f'{guests.pop()}, removed')
print(f'{guests.pop()}, removed')
del guests[4]
print('ben, removed')
print(guests)



