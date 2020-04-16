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
# code don't error but ony run second print on time.

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




