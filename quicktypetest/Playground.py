

    student1 = Student("Edward", "Gates", "0456789", {'math': 100, 'bio': 90, 'history': 80})
    print student1.math  # prints 100
    print student1.bio  # prints 90
    

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