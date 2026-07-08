class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy
    
    def getAttributesString(self):
        return f"Attributes: {self.name} ({self.species}) - Hunger: {self.hunger}, Energy: {self.energy}"

whiskers = Pet("Whiskers", "cat", 6, 8)


# TODO: Print Whiskers' initial attributes

print("Initial", whiskers.getAttributesString())
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
whiskers.hunger -= 3
#  - Increase energy by 2
whiskers.energy += 2
# TODO: Print Whiskers' modified attributes
print("Modified", whiskers.getAttributesString())
