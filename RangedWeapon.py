from Weapon import Weapon


class RangedWeapon(Weapon):
    def __init__(self, name, description, weight, damage, ammo):
        super().__init__(name, description, weight, damage)
        self.ammo = ammo
