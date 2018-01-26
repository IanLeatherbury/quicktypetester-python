# To parse this JSON data, add a new class to your project named "QuickType" then:
#
#     from QuickType import data
#
#     var data = Pokedex.FromJson(jsonString);
import json
from QuickType import test

p = json.loads(open('resources/pokedex.json').read())

data = test("", p)

print(data.pokedex[0])



