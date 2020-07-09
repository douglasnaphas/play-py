# What is the implicit first arg in static methods?

# What is the implicit first arg in instance methods?

# What if I want to access the class within an instance method?

class Dinosaur:
    kingdom = "animalia"
    phylum = "chordata"
    status = "least concern"
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def say_name(self):
        print('my name is ' + self.name)
    
    @classmethod
    def say_kingdom(cls):
        print('Dinosaurs are in kingdom ' + cls.kingdom)
    
    @staticmethod
    def rawr():
        print('RAWR')
    
    @classmethod
    def make_extinct(cls):
        cls.status = 'extinct'
    
    @classmethod
    def say_status(cls):
        print('Dinosaurs have status ' + cls.status)

d1 = Dinosaur('dug', 'slowasaurus')
d2 = Dinosaur('ra', 'deinonychus')
d1.say_kingdom()
d2.say_kingdom()
Dinosaur.say_kingdom()
Dinosaur.rawr()
d1.rawr()
print('******')
Dinosaur.make_extinct()
Dinosaur.say_status()
print("******")
d1.say_name()
d2.say_name()
