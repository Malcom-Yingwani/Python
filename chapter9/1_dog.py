# CLASSES

# CREATING THR DOG CLASS
class Dog:
    """A simple attempt to model a dog"""

    # CONSTRUCTOR
    def __init__(self, name, age): 
        """Initialise name and age attributes."""
        self.name = name 
        self.age = age
    
    #METHODS
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    
# INSTANCIATE DOG OBJECT
# my_dog = Dog("Will", 7)


# print(f"My dog's age name is {my_dog.name}")
# print(f"My dog's age {my_dog.age}")

# # CALLING METHODS
# my_dog.sit()
# my_dog.roll_over()

# CREATING MULTIPLE INSTANCES

my_dog = Dog("Will", 6)
your_dog = Dog("Lucy", 7)

print(f"My dog's name is {my_dog.name}")
print(f"Your dog's name is {your_dog.name}")

print(f"My dog's age is {my_dog.age}")
print(f"Your dog's age is {your_dog.age}")

my_dog.sit()
your_dog.sit()

my_dog.roll_over()
your_dog.roll_over()