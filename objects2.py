class PartyAnimal:
    x = 0

    def __init__(self):  # init is the constructor
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):  # the destructor part runs before the destruction happens
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42  # by pointing "an" to something other than the PartyAnimal class, we destroy the object
print('an contains', an)

# in object oriented programming, a contructor in a class is a special block of statements called when an object is created
# you can have many copies of class objects called instances, with their own copy of instance variables
