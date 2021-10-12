from Map import Map
from Room import Room
from Parser import Parser
from Player import Player
from Food import Food


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
        for enemy_name in self.kort.all_enemies:
            if enemy_name == enemy_name.enemy.name:
                enemy = self.kort.all_enemies[i]
                return enemy
            elif i == len(self.kort.all_enemies):
                return "enemy not found"
            else:
                i = i + 1

    def run(self):
        parser = self.parser
        player = self.player

        parser.welcome_text()
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

                    if(player.attack):
                        damage = player.equipped_weapon.damage

                    else:


                case _:
                    if command:
                        print("wrong command try again")
