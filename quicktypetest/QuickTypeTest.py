# To parse this JSON data, add a new class to your project named "QuickType" then:
#
#     from QuickType import from_json
#
#     data = from_json(json_string)

import json
from QuickType import pokedex_from_json

p = json.loads(open('resources/pokedex.json', encoding='latin1').read())

dex = pokedex_from_json(p)[0].avg_spawns

print(dex)
print(type(dex))



