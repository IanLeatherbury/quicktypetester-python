import json


p = json.loads(open('pokedex.json').read())


class Pokedex(object):
    def __init__(self, pokemon):
        self.pokedex = pokemon


def pokedex_from_json(p):
    pokemon = Pokedex(**p)
    return pokemon


def someFunc(myList = []):
    for x in myList:
        print x


someFunc(pokedex_from_json(p).pokedex)


class Pokemon(object):
    def __init__(self, prev_evolution,
                 name,
                 img,
                 spawn_chance,
                 egg,
                 weaknesses,
                 weight,
                 height,
                 candy_count,
                 avg_spawns,
                 num,
                 candy,
                 spawn_time,
                 next_evolution,
                 multipliers,
                 type,
                 id):
        self.prev_evolution = prev_evolution,
        self.name = name,
        self.img = img,
        self.spawn_chance = spawn_chance,
        self.egg = egg,
        self.weaknesses = weaknesses,
        self.weight = weight,
        self.height = height,
        self.candy_count = candy_count,
        self.avg_spawns = avg_spawns,
        self.num = num,
        self.candy = candy,
        self.spawn_time = spawn_time,
        self.next_evolution = next_evolution,
        self.multipliers = multipliers,
        self.type = type,
        self.id = id


def pokemon_from_json(p):
    pokemon = Pokemon(*p)
    return pokemon


t = pokemon_from_json(pokedex_from_json(p).pokedex[10])

print(t.avg_spawns)
