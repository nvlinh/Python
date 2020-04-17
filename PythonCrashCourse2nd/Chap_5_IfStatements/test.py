languages = ['Python', 'Java', 'JavaScript', 'Scala']
for language in languages:
    if language == 'Python':
        print(language.upper())
    else:
        print(language.lower())
# 1. Condition test
# condition == compare the value
a = 'Python'
a == 'python'  # False
a.lower() == 'python'  # True
# Checking for inequality
a != 'python'
# Number comparisons
age = 18
age == 27
age != 42
age < 20
age <= 20
age > 16
age >= 16

# Checking multiple condition
age_1 = 10
age_2 = 20
age_1 > 10 and age_2 > 20
age_1 <= 10 or age_2 <= 20

# Checking whether a value is in a List
foods = ['fish', 'meat', 'egg', 'milk']
print('fish' in foods)
print('Fish' in foods)

# Checking whether a value is not in a List
if 'pizza' not in foods:
    print(f'Pizza not in {foods}')

# Boolean expressions
isValid = True
isValid = False

# 2. If statement
if 1 == 1:
    print(True)
else:
    print(False)

if 1 < 2:
    print()
elif 1 == 2:
    print()
elif 1 > 3:
    print()
# Not need else in end of if elif statement, use elif for easy read

# 3. Using if statements with List
# Checking for special items
colors = ['red', 'blue', 'green']
for color in colors:
    if color == 'blue':
        print(f'Sorry, we out of the {color} color!')
    else:
        print(f'Color {color} is added.')
print('Finished making your color.')

# Checking that a List is not empty
print('Checking that a List is not empty:\n')
colors = []
for color in colors:
    print(color)

if colors:
    print('Not run here')
    for color in colors:
        print(color)
else:
    print('Colors are empty.')

# Using multiple lists
print('Using multiple lists:\n')
job_require_skills = ['python', 'mysql', 'vue.js', 'django', 'jquery', 'mongodb', 'NLP']
my_skills = ['java', 'mysql', 'spring']
for my_skill in my_skills:
    if my_skill in job_require_skills:
        print(f"It's OK. We are need skill {my_skill}")
    else:
        print(f"Sorry, we don't use your skill {my_skill} to work")
# Exercise checking user name
current_users = ['Linh', 'Tam', 'Loc', 'Anh', 'Hao', 'Nhat']
new_users = ['LINH', 'LinH', 'linh', 'tam', 'TAM', 'Tinh']
copy_lower_current_users = [current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in copy_lower_current_users:
        print(f'{new_user} is exist.')
    else:
        print(f"Don't exist username: {new_user}")
