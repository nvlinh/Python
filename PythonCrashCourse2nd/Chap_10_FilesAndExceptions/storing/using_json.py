import json

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

file_path = 'user.json'
with open(file_path, 'w') as js:
    json.dump(users, js)

with open(file_path, 'r') as js:
    users_2 = json.load(js)
    print(users_2['lin'])

