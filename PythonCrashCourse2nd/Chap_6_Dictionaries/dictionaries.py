# A simple dictionaries
linh = {'food': 'egg', 'numbers': 30}
print(f"Linh want to have {linh['food']}, with numbers are {linh['numbers']}.")

# A dictionary in Python is a collection of key-value pair.
# A key is connected to a value and you can access the value via key
# A key's value can be a number, string, list or dictionary
# You can use any object that you can created a Python
# as a value in a dictionary

linh = {'food': 'egg', 'food': 'meat'}
print(linh['food'])  # result is meat. Why?
print(linh)  # result = {'food': 'meat'}
linh['Food'] = 'fish'
print(linh)

# accessing values in a dictionary via key
# Adding new key-value pairs
print(linh)
linh['numbers'] = 40
linh['learning'] = ['Python', 'Vue.js']
linh['dictionary'] = {'key1': 1, 'key2': 'string', 'key3': ['a', 'b'],
                      2 : [2, ['1', '2']], 'key5': {'1'}}
# linh[[1, 2]] = 2  # result is typeError : unashable type : 'list'
linh[(1, 2)] = 2  # key is tuple is OK
# linh[{"ke1": 1}] = 3  # result is typeError: unhashable type: 'dict'
print(linh)
# As of Python 3.7, dictionaries retain the order in which they were defined.
# When you print a dictionary or loop through its elements,
# you will see the elements in the same
# order in which they were added to the dictionary.

# Starting with a empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values in a dictionary
print('Modifying values in a dictionary\n')
alien_0['color'] = 'blue'
print(alien_0)

# Removing a key-value pair in a dictionary
del alien_0['color']
print(alien_0)
# Note: be aware that the deleted key-value pair is removed permanently

# Using get() to access values
print('Using get() to access values:\n')
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  # KeyError: 'points'
print(alien_0.get('points', 'Key not exist'))
value = alien_0.get('point')
print(value)  # value = None, it's mean 'no value exists'

# Looping through a dictionary
for key, value in alien_0.items():
    print(f'\nKey: {key}, value: {value}')
# Looping through all keys in a dictionary
for key in alien_0.keys():
    print(f'Key : {key}')
# Lopping through a dictionary's key in a particular order
favorite_number = {
    'linh': 13,
    'linhSame': 13,
    'tam': 50,
    'an': 100,
    'luong': 1_000_000_000,
    'thuc': 1_000_000_000_000
}
for name in sorted(favorite_number.keys()):
    print(f'Name : {name}')
# Looping through all values in a dictionary
print('\nLooping through all values in a dictionary:')
for value in favorite_number.values():
    print(f'Value: {value}')
# Currently have two values are '13'
# It's fine with a small number, but with a large number of respondents.
# We can chosen without repetition, we can use a set.
# Set is a collection in which each item must be unique
print('\nUsing Set collection:')
for value in set(favorite_number.values()):
    print(f'Value: {value}')

# Can build a Set directly using braces and separating the elements with commas
set_languages = {'java', 'python', 'java script', 'java', 'Java'}
print(set_languages)

# 3. Nesting
print('\n3. Nesting')
# 3.1 A list of dictionaries
print('\n3.1 A list of dictionaries:')
student_0 = {'name': 'linh', 'class': '1A'}
student_1 = {'name': 'tam', 'class': '1B'}
student_2 = {'name': 'tinh', 'class': '1C'}
students = [student_0, student_1, student_2]
for student in students:
    print(student)

print("\nAuto create a list with length = 30")
students = []
for number in range(30):
    new_student = {'name': 'linh', 'class': '1A'}
    students.append(new_student)
# Print fist three students
for student in students[:3]:
    print(student)
# Print length of students
print(f"Student's length: {len(students)}")

# 3.2 A list in a dictionary
print('\n3.2 A list in a dictionary:')
favorite_languages = {
    'linh': ['java', 'python', 'java script'],
    'tam': ['java script'],
    'anh': ['java'],
    'hao': ['python', 'php'],
    'loc': ['c']
}
for name in favorite_languages.keys():
    print(f"{name}'s favorite languages :")
    if len(favorite_languages.get(name)) > 1:
        for language in favorite_languages.get(name):
            print(f'\t-{language}')
    else:
        print(f'\t-{favorite_languages.get(name)}')

# 3.3 A dictionary in a dictionary
users = {
    'lin': {
        'first': 'linh',
        'last': 'nguyen van',
        'address': '16 ha huy giap, da nang'
    },
    'tamTit': {
        'first': 'tam',
        'last': 'dao thi thien',
        'address': '16 ha huy giap, da nang'
    },
    'someOne': {
        'first': 'some',
        'last': 'one',
        'address': '18 ha huy giap, da nang'
    }
    }
for user_name, user_info in users.items():
    print(f"\nUser name is : {user_name}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    print(f"\t{full_name}")
    print(f"\t{user_info['address'].title()}")

