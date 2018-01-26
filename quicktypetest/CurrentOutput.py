class Pokedex(object):
    def __init__(self,
    pokemon: List<Pokemon>

class Pokemon(object):
    def __init__(self,
    id: Int
    num: String
    name: String
    img: String
    type: List<String>
    height: String
    weight: String
    candy: String
    candyCount: Maybe<Int>
    egg: Egg
    spawnChance: Double
    avgSpawns: Double
    spawnTime: String
    multipliers: Maybe<List<Double>>
    weaknesses: List<Weakness>
    nextEvolution: Maybe<List<Evolution>>
    prevEvolution: Maybe<List<Evolution>>

class Evolution(object):
    def __init__(self,
    num: String
    name: String

enum Egg = NotInEggs | OmanyteCandy | The10KM | The2KM | The5KM

enum Weakness = Bug | Dark | Dragon | Electric | Fairy | Fighting | Fire | Flying | Ghost | Grass | Ground | Ice | Poison | Psychic | Rock | Steel | Water
