class Restaurant:
    """A class that models different Restaurant types"""

    # CONSTRUCTOR
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        """Initialises an instance of Restaurant class."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    # METHODS
    def describe_restaurant(self):
        """Print description of restaurant incl. name & cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food!")
        print(f"{self.number_served} customers were served today.")
    
    def open_restaurant(self):
        """Indicates that the restaurant is now open."""
        print(f"{self.restaurant_name} is open for businness.")

    def set_number_served(self, number_served):
        """Sets the number of customers served."""
        self.number_served = number_served 
        print(f"{self.number_served} customers were served today.")
    
    def increment_number_served(self, more_customers):
        """Increment the number of served customers"""
        self.number_served += more_customers
        print(f"{self.number_served} customers were served today")
    
restaurant = Restaurant("Mike's Kitchen", "italian")
restaurant.describe_restaurant()
restaurant.set_number_served(10)
restaurant.describe_restaurant()

print()

restaurant.increment_number_served(5)
restaurant.describe_restaurant()