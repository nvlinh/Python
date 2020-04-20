from storing_multiple_class_in_a_module.car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
# Above is import multiple class from a module

# Importing an Entire Module:
# from storing_multiple_class_in_a_module.car import car
# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

# Importing All Classes from a Module
# from module_name import *
# this approach it’s unclear which classes
# you’re using from the module

# Importing a Module into a Module

# Using Aliases same chap 8
