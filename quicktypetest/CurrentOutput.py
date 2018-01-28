class Pokedex(object):
    def __init__(self):
        self.pokemon = pokemon

class Pokemon(object):
    def __init__(self):
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

class Evolution(object):
    def __init__(self)
        self.num = num
        self.name = name

enum Egg = NotInEggs | OmanyteCandy | The10KM | The2KM | The5KM

enum Weakness = Bug | Dark | Dragon | Electric | Fairy | Fighting | Fire | Flying | Ghost | Grass | Ground | Ice | Poison | Psychic | Rock | Steel | Water
