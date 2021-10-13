from Weapon import Weapon


class MeleeWeapon(Weapon):
    def __init__(self, name, description, weight, damage):
        super().__init__(name, description, weight, damage)
