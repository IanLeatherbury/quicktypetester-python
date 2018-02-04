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

    student1 = Student("Edward", "Gates", "0456789", {'math': 100, 'bio': 90, 'history': 80})
    print student1.math  # prints 100
    print student1.bio  # prints 90
    Then
    this
    will
    do
    the
    trick:

    class Student(object):
        def __init__(self, first_name, last_name, id, **kwargs):
            self.first_name = first_name
            self.last_name = last_name
            self.id = id
            for key, value in kwargs.iteritems():
                setattr(self, key, value)

    student1 = Student("Edward", "Gates", "0456789", {'math': 100, 'bio': 90, 'history': 80})





def someFunc(myList = []):
    for x in myList:
        print x


# someFunc(pokedex_from_json(p).pokedex)


class Pokemon(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)



{u'name': u'Bulbasaur', u'img': u'http://www.serebii.net/pokemongo/pokemon/001.png', u'spawn_chance': 0.69, u'egg': u'2 km', u'weaknesses': [u'Fire', u'Ice', u'Flying', u'Psychic'], u'weight': u'6.9 kg', u'height': u'0.71 m', u'candy_count': 25, u'avg_spawns': 69, u'num': u'001', u'candy': u'Bulbasaur Candy', u'spawn_time': u'20:00', u'next_evolution': [{u'num': u'002', u'name': u'Ivysaur'}, {u'num': u'003', u'name': u'Venusaur'}], u'multipliers': [1.58], u'type': [u'Grass', u'Poison'], u'id': 1}
{u'prev_evolution': [{u'num': u'001', u'name': u'Bulbasaur'}], u'name': u'Ivysaur', u'img': u'http://www.serebii.net/pokemongo/pokemon/002.png', u'spawn_chance': 0.042, u'egg': u'Not in Eggs', u'weaknesses': [u'Fire', u'Ice', u'Flying', u'Psychic'], u'weight': u'13.0 kg', u'height': u'0.99 m', u'candy_count': 100, u'avg_spawns': 4.2, u'num': u'002', u'candy': u'Bulbasaur Candy', u'spawn_time': u'07:00', u'next_evolution': [{u'num': u'003', u'name': u'Venusaur'}], u'multipliers': [1.2, 1.6], u'type': [u'Grass', u'Poison'], u'id': 2}
