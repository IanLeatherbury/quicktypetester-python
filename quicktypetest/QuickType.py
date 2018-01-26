class PokeDex(object):
    def __init__(self, pokemon):
        self.pokedex = pokemon


def from_json(p):
    pokemon = PokeDex(**p)
    return pokemon
