# To parse this JSON data, add a new class to your project named "QuickType" then:
#
#     from QuickType import from_json
#
#     data = from_json(json_string)

import json
from QuickType import from_json

p = json.loads(open('resources/pokedex.json', encoding='latin1').read())

dex = from_json(p)[0].avg_spawns

d = json.dump(p)
print(dex)
print(type(dex))



