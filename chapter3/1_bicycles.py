# Lists

bicycles = ['trek', 'cannodale', 'redline', 'specialised']
print(bicycles)

# Accesing elements in a list
print(bicycles[0].title())
print(f"Second element in list: {bicycles[1].upper()}") 

print("\n")
print(f"Last element: {bicycles[-1].title()} ")
print(f"Second last element: {bicycles[-2].title()}")

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)