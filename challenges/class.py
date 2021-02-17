class PartyAnimal:
    x = 0

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)



s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains', an)

#PartyAnimal.party(an)