person = {
    'first_name': 'Linh',
    'last_name': 'Nguyen Van',
    'age': 27,
    'city': 'Da Nang'
}

print(person['first_name'])
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))
print(person.get('salary'))
print(person.get('status', 'married'))
