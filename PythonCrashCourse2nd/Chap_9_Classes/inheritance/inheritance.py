# 1. The __init__() method for a subclass

import car


class ElectricCar(car.Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_electric_car = ElectricCar('Vinfast', 'Lux', 2020)
print(my_electric_car.get_descriptive_name())

# 2. Defining attributes and methods for the subclass
print("\n2. Defining attributes and methods for the subclass")


class ElectricCar(car.Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """"Initialize attributes of parent class.
        Then initialize attributes specific to an electrical car.
        """
        super().__init__(make, model, year)
        self.battery_size = 50

    def describe_battery(self):
        print(f"Battery is {self.battery_size} kmh.")


my_electric_car = ElectricCar('Vinfast', 'Lux SA Plux', 2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()

# 3. Overriding methods form the parent class
# same with java

# 4. Instances as attributes


class Battery:
    def __init__(self):
        self.battery_size = 150

    def describe_battery(self):
        print(f"Battery is {self.battery_size} kmh.")


class ElectricCar(car.Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """"Initialize attributes of parent class.
        Then initialize attributes specific to an electrical car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_electric_car = ElectricCar('Vinfast', 'Lux SA Plux', 2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
