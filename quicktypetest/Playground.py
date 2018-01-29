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