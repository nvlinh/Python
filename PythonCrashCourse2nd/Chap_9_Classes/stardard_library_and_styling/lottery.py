from random import choice

result = ('1', '2', '3','4', '5', 'iPhone 11', 'iPhone 11 Pro',
          'iPhone 11 Pro Max', 'iPhone 12 Pro', 'iPhone 12 Pro Max')

for number in range(5):
    print(choice(result))

my_ticket = '1'
count_time_random = 0

while True:
    count_time_random += 1
    if my_ticket == choice(result):
        print(f"{count_time_random} time to loop run to give a winning ticket.")
        break
