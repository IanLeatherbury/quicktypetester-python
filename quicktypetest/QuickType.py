import json


p = json.loads(open('pokedex.json').read())


class Pokedex(object):
    def __init__(self, pokemon):
        self.pokedex = pokemon


def pokedex_from_json(p):
    pokemon = Pokedex(**p)
    return pokemon


class Pokemon(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


def pokemon_from_json(p):
    pokemon = Pokemon(*p)
    return pokemon


print(Pokemon(**p['pokemon'][0]).candy)

