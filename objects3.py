class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):  # "z" is a parameter that we define in lines 12 and 15
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
