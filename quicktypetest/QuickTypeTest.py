# To parse this JSON data, 'import json' then do:
#
#     using QuickType;
#
#     var data = Pokedex.FromJson(jsonString);

import json

p = json.loads(open('resources/pokedex.json').read())

from PokeDex import f

print(f('') + "wee")

#
# class User(object):
#     def __init__(self, name, username):
#         self.name = name
#         self.username = username
#
# j = json.loads(json_string)
# u = User(**j)
#
# print "Object: " + u.name

