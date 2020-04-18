# Defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello")


greet_user()


# Passing information to a function
def greet_user(name):
    """Display a simple greeting."""
    print(f"Hello {name.title()}")


greet_user('linh')


# Arguments and parameters
# The variable name in the definition of greet_user() is an example of a
# parameter, a piece of information the function needs to do its job.
# The value 'linh' in greet_user('linh') is an example of an argument.

# Passing arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('dog', 'mundo')
# Multiple function calls
describe_pet('cat', 'meo')
describe_pet('chicken', 'ga luoc')
# Keyword arguments
describe_pet(pet_name='milu', animal_type='dog')


# Default value
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='mundo')
describe_pet('mundo')


# Return value
# return a simple type


def get_formatted_name(first_name, last_name, middle_name=''):
    """return a full name, formatted"""
    full_name = "";
    if middle_name:
        full_name = f"{first_name} {last_name} {middle_name}".title()
    else:
        full_name = f"{first_name} {last_name}".title()
    return full_name


formatted_name = get_formatted_name('linh', 'nguyen', 'van')
print(formatted_name)
formatted_name = get_formatted_name('linh', 'nguyen')
print(formatted_name)


# Return a dictionary


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person


person_1 = build_person('linh', 'nguyen')
print(person_1)
person_2 = build_person('linh', 'nguyen', 27)
print(person_2)


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person


person_1 = build_person('linh', 'nguyen')
print(person_1)
person_2 = build_person('linh', 'nguyen', 27)
print(person_2)

# Using a function with a while loop
while True:
    print("Please tell me your name.")
    print("enter 'q' at any time to quit")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)

# Passing a List
print('\n Passing a List:')


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)  # Result = [],
# it's different with Java. Todo consider Python memory
print(completed_models)

# Preventing function from modifying a list
print("\nPreventing function from modifying a list")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
# Note:
# consider about time and memory when take a copy, when working with large lists

# 4. Passing a arbitrary number of arguments
print("\n4. Passing a arbitrary number of arguments")


def select_foods(*foods):
    """Show all foods are required"""
    print(foods)
    for food in foods:
        print(food)


select_foods("meat")
select_foods("meat", 'meat', 'egg', 'fish')
# *foods tells Python to make an empty tuple called toppings
# and pack whatever values it receives into this tuple

# Using arbitrary keyword arguments
print("\nUsing arbitrary keyword arguments")


def build_profile(first_name, last_name, **user_ino):
    """Build a dictionary of an user information"""
    user_ino['first_name'] = first_name
    user_ino['last_name'] = last_name
    return user_ino


user_profile = build_profile('linh', 'nguyen',
                             age=27, country='Viet Nam')
print(user_profile)
