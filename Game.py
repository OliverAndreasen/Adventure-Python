from Map import Map
from Parser import Parser, welcome_text
from Player import Player
from RangedWeapon import RangedWeapon
from Room import Room


class Game:

    def __init__(self):
        self.kort = Map()
        self.current_room = self.kort.current_room
        self.is_running = True
        self.parser = Parser()
        self.player = Player()

    def go(self, room_name):
        self.current_room = room_name

    def get_item(self, input_name):
        i = 0
        for find_item in self.kort.all_items:
            if input_name == find_item.name:
                item = self.kort.all_items[i]
                return item
            elif i == len(self.kort.all_items):
                return "item not found"
            else:
                i = i + 1

    def get_enemy(self, enemy_name):
        i = 0
        for enemy in self.kort.all_enemies:
            if enemy.name == enemy_name:
                enemy = self.kort.all_enemies[i]
                return enemy
            elif i == len(self.kort.all_enemies):
                return "enemy not found"
            else:
                i = i + 1

    def get_closest_enemy(self):
        closet_room_enemies = list()
        for enemy_name in self.current_room.room_enemies:
            enemy = self.get_enemy(enemy_name)
            closet_room_enemies.append(enemy.distance)

        closet_enemy = min(closet_room_enemies)
        index = closet_room_enemies.index(closet_enemy)
        enemy_name = self.current_room.room_enemies[index]

        return enemy_name

    def run(self):
        parser = self.parser
        player = self.player
        welcome_text()
        print("you are in room " + self.current_room.name)

        while True:
            parser.current_room = self.current_room
            player.current_room = self.current_room
            user_input = input("write your command").lower()
            parser.user_input = user_input
            command = parser.command()
            item_name = parser.attribute()

            match command:
                case "go":
                    if isinstance(parser.set_direction(), Room):
                        self.go(parser.set_direction())
                        print(self.current_room.description)

                    else:
                        print("you cannot go that way")

                case "take":
                    if self.current_room.check_room_item(item_name):
                        item = self.get_item(item_name)
                        if player.check_player_weight(item.weight):
                            player.take(item_name)
                            player.player_weight = player.player_weight + item.weight
                            print("you took the " + item_name)

                        else:
                            print("you cant carry any more items")

                    else:
                        print("no such item to take")

                case "drop":
                    if player.check_player_item(item_name):
                        item = self.get_item(item_name)
                        player.player_weight = player.player_weight - item.weight
                        player.drop(item_name)
                        print("you dropped the " + item_name)

                    else:
                        if item_name:
                            print(str(item_name) + " does not exist in your inventory")

                        else:
                            print("to drop you have to write drop 'item name'")

                case "inv":
                    if player.player_items:
                        print("current inventory weight: " + str(player.player_weight))
                        print("max inventory weight: " + str(player.player_max_weight))
                        print("Inventory:")
                        print(player.player_items)

                    else:
                        print("you have no items in your inventory")

                case "look":
                    if self.current_room.room_items:
                        print("Items in this room:")
                        print(self.current_room.room_items)

                    else:
                        print("no items in this room")

                case "equip":
                    item = self.get_item(item_name)
                    if player.check_player_item(item_name):
                        print(player.equip_weapon(item))

                case "eat":
                    item = self.get_item(item_name)
                    print(player.eat(item))

                case "attack":
                    if player.check_if_weapon_equipped() is False:
                        print("you have to equip a weapon first!")

                    else:
                        if not self.current_room.room_enemies == []:
                            enemy_name = item_name
                            if not enemy_name:
                                enemy_name = self.get_closest_enemy()

                            enemy = self.get_enemy(enemy_name)
                            player_weapon = self.get_item(player.equipped_weapon)
                            damage = player_weapon.damage
                            if isinstance(player_weapon, RangedWeapon):
                                if player_weapon.ammo <= 0:
                                    print("you tried to attack but has no ammo")
                                    damage = 0

                                else:
                                    player_weapon.ammo = player_weapon.ammo - 1

                            print("you approached " + enemy.name + " it has " + str(enemy.hp) + " hp")
                            print("you attacked " + enemy.name + " and dealt " + str(damage) + " damage")
                            enemy.hp = enemy.hp - damage

                            if enemy.hp <= 0:
                                enemy.isAlive = False

                            if enemy.isAlive:
                                enemy_damage = enemy.weapon.damage
                                if isinstance(enemy.weapon, RangedWeapon):
                                    if enemy.weapon.ammo <= 0:
                                        print("the enemy tried to attack but has no ammo")
                                        enemy_damage = 0

                                    else:
                                        enemy.weapon.ammo = enemy.weapon.ammo - 1

                                player.player_current_hp = player.player_current_hp - enemy_damage
                                print("the enemy attacked you and dealt  " + str(
                                    enemy_damage) + " damage your hp is now: " + str(
                                    player.player_current_hp))

                                if player.player_current_hp <= 0:
                                    self.current_room = self.kort.current_room

                                    player.unequip_weapon()
                                    print("you died and lost all your items")
                                    print(self.current_room.description)

                                    for item_name in player.player_items:
                                        item = self.get_item(item_name)
                                        self.current_room.room_items.append(item.name)

                                    player.player_items.clear()
                                    player.player_current_hp = player.player_max_hp

                            else:
                                print("the enemy died !")
                                print("they dropped their weapon : " + enemy.weapon.description)
                                self.current_room.room_items.append(enemy.weapon.name)
                                self.current_room.room_enemies.remove(enemy.name)

                        else:
                            print("no enemies to attack")

                case "u":
                    print(player.unequip_weapon())

                case _:
                    if command:
                        print("wrong command try again")
