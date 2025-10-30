# Module for restaurant class
class Restaurant:
    """A class that models different Restaurant types"""

    # CONSTRUCTOR
    def __init__(self, restaurant_name, cuisine_type):
        """Initialises an instance of Restaurant class."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # METHODS
    def describe_restaurant(self):
        """Print description of restaurant incl. name & cuisine type."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} foods!")
    
    def open_restaurant(self):
        """Indicates that the restaurant is now open."""
        print(f"{self.restaurant_name} is open for businness.")