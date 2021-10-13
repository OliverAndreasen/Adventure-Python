class Enemy:
    def __init__(self, name, hp, weapon, distance):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.distance = distance
        self.isAlive = True
