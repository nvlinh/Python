#1. Looping through an entire list
foods = ['fish', 'meat', 'egg']
for food in foods:
	print(food)

#2. Avoid identation error
print('2. Avoid identation error')
#2.1 Forgetting to ident
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
#print(magician) => IndentationError
	print(magician)

#2.2 Forgetting to indent additional lines
print('Forgetting to indent additional lines\n')
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
# code don't error but ony run second print one time.

#2.3 Indenting unnecessarily
message = "Hi"
 #print(message) => IndentationError: unexpected indent

# 2.4 Indenting unnecessarily after the loop
print('\n 2.4 Indenting unnecessarily after the loop \n')
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")

 print("Thank you everyone, that was a great magic show!") # in for loop becase have indent in the left

# 2.5 Forgetting the colon
#for magician in magicians

# 3. Making numberical lists
print('\n 3. Making numberical lists \n')

# 3.1 Using the range() function
for value in range(1,6):
	print(value) #print 1,2,3,4,5

for value in range (6):
	print(value) #print 0,1,2,3,4,5

# 3.2 Using range() to making a list of number
print('\n 3.2 Using range() to making a list of number \n')
numbers = list(range(1,11))
print(numbers)

numbers = list(range(1,11,2))
print(numbers) 

# 3.3 Simple statistics with a list of numbers
print('\n 3.3 Simple statistics with a list of numbers\n')
digits = [1,2,3,4,5,6,7,8,9,10]
print(max(digits))
print(min(digits))
print(sum(digits))

# 3.4 List comprehensions
print('\n3.4 List comprehensions\n')
squares = [value**2 for value in range(1,11)]
print(squares)

#4 Working with part of a list
print('\n4 Working with part of a list:\n')
# 4.1 Slicing a List
numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
print(numbers[0:3])
print(numbers[1:4])
print(numbers[:4])
print(numbers[2:])
print(numbers[-3:])
print(numbers[:-3])

# 4.2 Looping through a slice
print('4.2 Looping through a slice:\n')
players = ['linh', 'tam', 'tinh', 'tien']
print('Here are the first three player on my team')
for player in players[:3]:
	print(player)

# 4.3 Copying a List
print(' 4.3 Copying a List:\n')
my_foods = ['rice', 'fish', 'meat', 'egg']
my_wife_foods = my_foods[:] 
my_foods.append('coffee')
my_wife_foods.append('pizza')
print(f'My foods : {my_foods}')
print(f'My wife foods {my_wife_foods}')

# 5 Tuples
print('5. Tuples\n')
# An immutable list is called tuple
#5.1 Defining a Tuple
print('5.1 Defining a Tuple\n')
firstTuple = (1,2,3)
print(firstTuple[0])
#firstTuple[1] =2 #TypeError: 'tuple' object does not support item assignment
#defining one element
secondTuple = (4,)
for item in secondTuple:
	print(item)
# Writing over a Tuple
firstTuple = (4,5,6,7)

# 6. Styling your code
# A bit about PEP8 : indentation, line length, blank line
# https://www.python.org/dev/peps/pep-0008/ 





