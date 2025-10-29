class User:
    """Builds a user profile."""

    def __init__(self, first_name, last_name, ethnicity, phone_number, login_attempts = 0):
        """Initialise a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.ethnicity = ethnicity
        self.phone_number = phone_number
        self.login_attempts = login_attempts

    def describe_restaurant(self):
        """Summarises the user attributes."""

        print("\nThis is the summary of this user:")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Ethnicity: {self.ethnicity.title()}")
        print(f"Phone Number: {self.phone_number}")
        print(f"This user has made: {self.login_attempts} login attempts.")

    def greet_user(self):
        """Greets the user."""

        print(f"\nHello, {self.first_name.title()}")

    def increment_login(self):
        """Increments login attempts by 1"""

        self.login_attempts += 1
        print(f"\n{self.login_attempts} login attempts.")

    def reset_attempts(self):
        """Resets login attempts to zero."""
        
        self.login_attempts = 0
        print(f"\n{self.login_attempts} login attempts")
    
me = User("malcom", "yingwani", "african", "081_407_8940")
me.greet_user()
me.describe_restaurant()

me.increment_login()
me.increment_login()
me.increment_login()
me.describe_restaurant()
me.reset_attempts()
me.describe_restaurant()