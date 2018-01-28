import json

######## Json parsing example 1 ########
json_string = '{"first_name": "Ian", "second_name":"Leatherbury"}'

parsed_json = json.loads(json_string)

print(parsed_json['first_name'])

######## Json parsing example 2 ########
d = {
    'first_name': 'Ian',
    'second_name': 'Leatherbury',
    'titles': ['Manager', 'Developer'],
}

p = json.loads(open('resources/pokedex.json').read())

print(json.dumps(p))






######## Json parsing example 3 ########
class User(object):

    def __init__(self, first_name, second_name):
        self.name = second_name
        self.username = second_name


j = json.loads(json_string)
u = User(**j)

print "Object: " + u.name






######## Json parsing example 4 ########
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print x.name, x.hometown.name, x.hometown.id