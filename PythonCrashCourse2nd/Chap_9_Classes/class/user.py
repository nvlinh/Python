class User:
    """Model a user"""
    def __init__(self, first_name, last_name, **profile):
        """Initialize several attributes of a user as first_name,
         last_name, and several other attributes"""
        profile['first_name'] = first_name
        profile['last_name'] = last_name
        self.profile = profile

    def describe_user(self):
        """Print user profile"""
        print(self.profile)

    def greet_user(self):
        """Greeting with a user"""
        print(f"Hello {self.profile['first_name'].title()}  {self.profile['last_name'].title()}")


user_0 = User('linh', 'nguyen',
              color='white', languages=['Java', 'Python'])
user_0.describe_user()
user_0.greet_user()


