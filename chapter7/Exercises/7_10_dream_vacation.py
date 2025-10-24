prompt = "\nEnter 'quit' to exit the poll"
prompt += "\nIf you could visit one place in the world, where would you go? "
dream_vacations = []

while prompt:
   poll = input(prompt)
   
   if poll == 'quit':
      break
   else:
      dream_vacations.append(poll)


print("\nPeoples dream vacations:")
for vacation in dream_vacations:
   print(vacation.title())