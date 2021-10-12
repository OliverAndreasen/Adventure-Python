from Item import Item


class Food(Item):
    def __init__(self, name, description, weight, hp):
        super().__init__(name, description, weight)
        self.hp = hp
