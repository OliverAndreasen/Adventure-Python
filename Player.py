from Food import Food
from Weapon import Weapon


class Player:

    def __init__(self):
        self.equipped_weapon = None
        self.player_items = list()
        self.current_room = ""
        self.player_max_weight = 100
        self.player_weight = 0
        self.player_current_hp = 100
        self.player_max_hp = 100

    def take(self, item_name):
        self.player_items.append(item_name)
        self.current_room.room_items.remove(item_name)

    def drop(self, item_name):
        self.player_items.remove(item_name)
        self.current_room.room_items.append(item_name)

    def check_player_item(self, item_name):
        for find_item in self.player_items:
            i = 0
            if item_name == find_item:
                return True
            elif i == len(self.player_items):
                return False
            else:
                i = i + 1

    def check_player_weight(self, item_weight):
        if self.player_weight + item_weight <= self.player_max_weight:
            return True
        else:
            return False

    def check_if_weapon_equipped(self):
        if self.equipped_weapon is None:
            return False
        else:
            return True

    def equip_weapon(self, item):
        if not self.check_if_weapon_equipped():
            if issubclass(item.__class__, Weapon):
                self.equipped_weapon = item.name
                return item.name + " is now equipped"
            else:
                return item.name + " is not a weapon"
        else:
            return "You already have a weapon equipped"

    def unequip_weapon(self):
        if self.equipped_weapon is None:
            print("you dont have a weapon equipped")
        else:
            print("you uneqipped your weapon: " + self.equipped_weapon)
            self.equipped_weapon = None

    def eat(self, item):
        if isinstance(item, Food):
            if self.check_player_item(item.name):
                hp = item.hp
                item_placement = "inv"
            elif self.current_room.check_room_item(item.name):
                hp = item.hp
                item_placement = "room"
            else:
                return "food not found"

            if self.player_current_hp < self.player_max_hp:
                current_health = self.player_current_hp + hp
                if current_health >= self.player_max_hp:
                    self.player_current_hp = self.player_max_hp
                    healed = current_health - self.player_max_hp
                    if item_placement == "inv":
                        self.player_items.remove(item.name)
                    elif item_placement == "room":
                        self.current_room.room_items.remove(item.name)

                    return "you healed " + str(healed)
                else:
                    self.player_current_hp = self.player_current_hp + hp
                    healed = hp
                    if item_placement == "inv":
                        self.player_items.remove(item.name)
                    elif item_placement == "room":
                        self.current_room.room_items.remove(item.name)
                    return "you healed " + str(healed)
            else:
                return "you are already full health"
        else:
            return "you cant eat that"

    def attack(self):
        if self.check_if_weapon_equipped():
            return True
        else:
            return False
