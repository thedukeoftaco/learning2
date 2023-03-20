# inheritance (subclasses)
# when we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class
# and then add out own little bit to make our new class
# another form of store and reuse
# write once - reuse many times
# the new class (child) has all the capabilities of the old class (parent) - and then some more

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):  # means that FF inherits everything from PA
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
