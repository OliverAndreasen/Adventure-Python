from Weapon import Weapon


class Player:

    def __init__(self):
        self.equipped_weapon = None
        self.player_items = list()
        self.current_room = ""
        self.player_max_weight = 10
        self.player_weight = 0

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
            return True;

    def equip_weapon(self, item):
        if not self.check_if_weapon_equipped():
            if isinstance(item, Weapon):
                self.equipped_weapon = item.item_name
                return item.item_name + " is now equipped"
            else:
                return item.item_name + " is not a weapon"
        else:
            return "You already have a weapon equipped"
