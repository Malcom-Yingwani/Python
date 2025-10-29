class User:
    """Builds a user profile."""

    def __init__(self, first_name, last_name, ethnicity, phone_number):
        """Initialise a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.ethnicity = ethnicity
        self.phone_number = phone_number

    def describe_restaurant(self):
        """Summarises the user attributes."""

        print("\nThis is the summary of this user:")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Ethnicity: {self.ethnicity.title()}")
        print(f"Phone Number: {self.phone_number}")

    def greet_user(self):
        """Greets the user."""

        print(f"\nHello, {self.first_name.title()}")


me = User("malcom", "yingwani", "african", "081_407_8940")
me.greet_user()
me.describe_restaurant()

athe = User("athenkosi", "mtangayi", "african", "083_748_5442")
athe.greet_user()
athe.describe_restaurant()

benji = User("benjamin", "taylor", "white", "083_262_7229")
benji.greet_user()
benji.describe_restaurant()