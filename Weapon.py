from Item import Item


class Weapon(Item):
    def __init__(self, name, description, weight, damage):
        self.damage = 0
        super().__init__(name, description, weight)
        self.damage = damage
