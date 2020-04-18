# How the input() function work
message = input("What is your name?")
print(message)
age = input("How old are you?")
age = int(age)
if age > 18:
    print('> 18')
# The modulo operator (%)
number = input("In put a number")
number = int(number)
if number%2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
# Introduction while loop
number = 1
while number <= 5:
    print(number)
    number += 1
# Using input letter or flag to quit ,Using break to exit loop, Using continue
# in a loop Using while loop with lists and dictionaries

# Note: A for loop is effective for looping through a list,
# but you shouldn’t modify  a list inside a for loop because
#  Python will have trouble keeping track of the items in the list.
# To modify a list as you work through it, use a while loop.
# Using while loop with lists and dictionaries allows you to collect,
# store, and  organize lots of input to examine and report on later.

# Moving items from one list to another
print('\nMoving items from one list to another')
names = ['Linh', 'Loan', 'Long', 'Luong', 'Lan', 'Toan', 'Nhon', 'Huy', 'Tam']
print(names)
names_start_with_l = []
while names:
    name = names.pop()
    if name.startswith('L'):
        names_start_with_l.append(name)
print(names_start_with_l)

names = ['Linh', 'Loan', 'Long', 'Luong', 'Lan', 'Toan', 'Nhon', 'Huy', 'Tam']
names_start_with_l = [name for name in names if name.startswith('L')]
names.clear()
print(names_start_with_l)

# Removing all instance of specific values from a list
print('\nRemoving all instance of specific values from a list')
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling dictionary with input
print('\nFilling dictionary with input')
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
