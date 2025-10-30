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
        
class IceCreamStand(Restaurant):
    """A child class that models an ice cream stand"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialise attributes of the parent class.
        Then initilise attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["cookies and cream", "chocolate", "vanilla", "choc mint"]
        
    def display_flavours(self):
        """Displays the avaialble flavours."""
        
        print("These are the delicious flavours we have to offer:")
        for flavour in self.flavours:
            print(flavour.title())
            
my_ice_cream = IceCreamStand("The Best Cream",  "dairy")
my_ice_cream.open_restaurant()
my_ice_cream.describe_restaurant()
my_ice_cream.display_flavours()