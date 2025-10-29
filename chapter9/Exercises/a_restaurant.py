# 9.1 RESTAURANT

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
        print(f"{self.restaurant_name} serves {self.cuisine_type} food!")
    
    def open_restaurant(self):
        """Indicates that the restaurant is now open."""
        print(f"{self.restaurant_name} is open for businness.")

# INSTANTIATE INSTANCE OF CLASS
restaurant_1 = Restaurant("Mike's Kichen", "Italian")

print(f"The restaurant name is: {restaurant_1.restaurant_name}")
print(f"They serve: {restaurant_1.cuisine_type}")

print("\n--- Method Calls ---")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()


# ====================================================================================
# ====================================================================================

# 9.2 THREE RESTAURANT

restaurant_2 = Restaurant("Lantern Light", "Chinese")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("KFC", "Fast Food")
restaurant_3.describe_restaurant()
        