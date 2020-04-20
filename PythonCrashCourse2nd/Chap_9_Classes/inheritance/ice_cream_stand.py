from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Model a ice cream stand restaurant"""
    def __init__(self, restaurant_name):
        """Initialize attributes of parent class.
        Then initialize attribute flavors of subclass"""
        super().__init__(restaurant_name, 'ice cream stand');
        self.flavors = ['Coffee', 'Cookies and Cream', 'Cookie dough', 'Cotton candy']

    def display_flavors(self):
        print(f"Flavors : {self.flavors}")


ice_cream = IceCreamStand('LinhTam')
ice_cream.describe_restaurant()
ice_cream.display_flavors()