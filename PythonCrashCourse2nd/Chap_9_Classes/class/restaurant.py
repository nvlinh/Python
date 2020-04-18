class Restaurant:
    """Model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print restaurant information"""
        print(f"{self.restaurant_name.title()} "
              f"is {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Print status of restaurant"""
        print(f"{self.restaurant_name} is open now.")


restaurant_qn = Restaurant('Bien Dong', 'sea food')
restaurant_qn.describe_restaurant()
restaurant_qn.open_restaurant()
