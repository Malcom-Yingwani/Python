# Numeriacal Comparisons

age = 18
print(f'Is the person below 21 yesrs of age?: {age == 18}')

age= 26
print(f'\n is the person above 21 years of age?: {age > 21}')
print(f'Is the person atleast 21 years of age?: {age >= 21}')

print('\n')

# Checking multiple conditions
# 1. Using and
age_0 = 22
age_1 = 18

admision = age_0 >=21 and age_1 >= 21
print(f'Can they be admitted? {admision}')

# 2. Using or
age_0 = 22
age_1 = 18

admision = age_0 >=21 or age_1 >= 21
print(f'Can they be admitted? {admision}')

print('\n')
# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f'Did they request mushrooms?:{'mushrooms' in requested_toppings}')
print(f'Did they request pepperoni? {'pepperoni' in requested_toppings}')

print('\n')
# Checking whether a valie is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")



