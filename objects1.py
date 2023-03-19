# classes = like templates -- dog
# method or message = a defined capability of a class (a function) -- bark()
# field or attribute = a bit of data in a class -- length
# objects = a particular instance of a class -- lassie
    # so I could make my cards into objects with a "card" class?
# instances are actual objects created at runtime

class PartyAnimal:
    x = 0

    def party(self):  # this function only exists within the class
        self.x = self.x + 1  # "self" is an alias of "an"
        print("So far", self.x)

an = PartyAnimal  # this part constucts a PartyAnimal object and stores in "an"

an.party()  # tell the object to run the party() code within it
an.party()  # these essentially say "PartyAnimal.party(an)
an.party()

# for the example of "x.sort", the "." syntax is asking python to look at the functions which that object is able to
# perform. if you use x = list() and dir(x), you will see all the defined functions of the list class. you can dir one
# of you created classes to see what it do
