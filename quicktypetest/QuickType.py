import json


# p = json.loads(open('pokedex.json').read())

class Evolution(object):
    def __init__(self,
            num: str,
            name: str,
        ):
        self.num = num
        self.name = name

class Pokemon(object):
    def __init__(self,
            id: int,
            num: str,
            name: str,
            img: str,
            type: list<str>,
            height: str,
            weight: str,
            candy: str,
            candyCount: int,
            egg: Egg,
            spawnChance: float,
            avgSpawns: float,
            spawnTime: str,
            multipliers: Maybe<list<float>>,
            weaknesses: list<Weakness>,
            nextEvolution: list<Evolution>,
            prevEvolution: list<Evolution>,
        ):
        self.id = id
        self.num = num
        self.name = name
        self.img = img
        self.type = type
        self.height = height
        self.weight = weight
        self.candy = candy
        self.candyCount = candyCount
        self.egg = egg
        self.spawnChance = spawnChance
        self.avgSpawns = avgSpawns
        self.spawnTime = spawnTime
        self.multipliers = multipliers
        self.weaknesses = weaknesses
        self.nextEvolution = nextEvolution
        self.prevEvolution = prevEvolution

class Pokedex(object):
    def __init__(self,
            pokemon: list<Pokemon>,
        ):
        self.pokemon = pokemon

# Need to emit proper class: Pokedex.Pokemon[0].name
def pokedex_from_json(p):
    return [Pokemon(**x) for x in p['pokemon']]


