import json


# p = json.loads(open('pokedex.json').read())

class Pokedex(object):
    def __init__(self, pokemon):
        self.pokemon = pokemon


class Pokemon(object):
    def __init__(self,
                 prev_evolution="value",
                 name="",
                 img="value",
                 spawn_chance="value",
                 egg="value",
                 weaknesses="value",
                 weight="value",
                 height="value",
                 candy_count="value",
                 avg_spawns="value",
                 num="value",
                 candy="value",
                 spawn_time="value",
                 next_evolution="value",
                 multipliers="value",
                 type="value",
                 id="value"):
        self.prev_evolution = prev_evolution
        self.name = name
        self.img = img
        self.spawn_chance = spawn_chance
        self.egg = egg
        self.weaknesses = weaknesses
        self.weight = weight
        self.height = height
        self.candy_count = candy_count
        self.avg_spawns = avg_spawns
        self.num = num
        self.candy = candy
        self.spawn_time = spawn_time
        self.next_evolution = next_evolution
        self.multipliers = multipliers
        self.type = type
        self.id = id


def pokedex_from_json(p):
    return [Pokemon(**x) for x in p['pokemon']]


