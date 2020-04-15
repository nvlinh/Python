#1. Declare a list
bicycles = ['treck', 'canondale', 'redline']
print(bicycles)

#2. Accessing element in a List
print(bicycles[0])
# List are ordered collection
# Index position start at 0 not 1

# Access last item in list with index = -1
print(bicycles[-1])
print(bicycles[-2]) # result = canondale
print(bicycles[-3]) # result = treck

# Using individual Values from a List
message = f'This is first item {bicycles[0].upper()}'
print(message)

#3. Changing, Adding, and Removing elements
print('3. Changing, Adding, and Removing elements')
# Modifying elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to the end of a List
motorcycles.append('honda')
print(motorcycles)

# Inserting elements into a List
motorcycles.insert(2, 'mimi') # mimi is name of my motorbike
print(motorcycles)

# Removing elements from a List
del motorcycles[1]
print(motorcycles)

# Removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Poping item from any position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_fMotorcycles = motorcycles.pop(0)
print(motorcycles)
print(popped_fMotorcycles)

# If only delete item from a List and not use item deleted then use def function else use pop function

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'honda', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles) # result is ['honda', 'suzuki', 'ducati']
# remove() function only remove first item in a List

#4. Organizing a List

#4.1 Sorting a List permanently with the Sort() method
print('Sorting a List permanently with the Sort() method')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'Audi', 'Toyota', 'Subaru']
cars.sort()
print(cars) # resull = ['Audi', 'Subaru', 'Toyota', 'bmw']

#4.2 Sorting a list temporarily with the sorted() function
print('4.2 Sorting a list temporarily with the sorted() function')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
temporarilyListReverse = sorted(cars, reverse=True)
print(temporarilyListReverse)
print("\nHere is the original list again:")
print(cars)

#4.3 Pringting a list in reverse order
print('4.3 Pringting a list in reverse order')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#4.4 Finding the lengh of a List
print('4.4 Finding the lengh of a List')
lengh = len(cars)
print(lengh) # result = 4 => start with One 

#5. Avoid index error when working with Lists
print('5. Avoid index error when working with Lists')
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) => Out of range
motorcycles = []
#print(motorcycles[-1]) => Out of range
