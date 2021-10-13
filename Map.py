from Enemy import Enemy
from Food import Food
from Item import Item
from Room import Room
from RangedWeapon import RangedWeapon
from MeleeWeapon import MeleeWeapon


class Map:
    def __init__(self):
        self.room1 = Room("Room1", "Jeg er rum 1")
        self.room2 = Room("Room2", "Jeg er rum 2")
        self.room3 = Room("Room3", "Jeg er rum 3")
        self.room4 = Room("Room4", "Jeg er rum 4")
        self.room5 = Room("Room5", "Jeg er rum 5")
        self.room6 = Room("Room6", "Jeg er rum 6")
        self.room7 = Room("Room7", "Jeg er rum 7")
        self.room8 = Room("Room8", "Jeg er rum 8")
        self.room9 = Room("Room9", "Jeg er rum 9")
        self.current_room = self.room1
        self.all_items = list()

        # Room 1
        self.room1.set_room_east(self.room2)
        self.room1.set_room_south(self.room4)
        # Room 2
        self.room2.set_room_west(self.room1)
        self.room2.set_room_east(self.room3)

        # Room 3
        self.room3.set_room_south(self.room6)
        self.room3.set_room_west(self.room2)

        # Room 4
        self.room4.set_room_north(self.room1)
        self.room4.set_room_south(self.room7)

        # Room 5
        self.room5.set_room_south(self.room8)

        # room 6
        self.room6.set_room_north(self.room3)
        self.room6.set_room_south(self.room9)

        # Room 7
        self.room7.set_room_north(self.room4)
        self.room7.set_room_east(self.room8)

        # Room 8
        self.room8.set_room_north(self.room5)
        self.room8.set_room_east(self.room9)
        self.room8.set_room_west(self.room7)

        # Room 9
        self.room9.set_room_north(self.room6)
        self.room9.set_room_west(self.room8)

        # Items
        shovel = Item("shovel", "Rusty shovel", 3)
        flashlight = Item("flashlight", "New flashlight", 2)
        soda = Item("soda", "Expired soda", 1)
        sock = Item("sock", "Smelly sock", 1)

        # Weapons
        sword = MeleeWeapon("sword", "Long sword", 5, 50)
        knife = MeleeWeapon("knife", "small knife", 1, 5)
        wallet = RangedWeapon("wallet", "gabens wallet", 1, 20, 1)

        # Food
        apple = Food("apple", "red apple", 1, 20)
        onion = Food("onion", "old onion", 1, 5)

        # Enemies
        goblin = Enemy("goblin", 60, knife, 10)
        gaben = Enemy("gaben", 150, wallet, 5)

        # Room 1 items
        self.room1.room_items.append("shovel")
        self.room1.room_items.append("flashlight")
        self.room1.room_items.append("soda")
        self.room1.room_items.append("sword")

        # Room 1 enemies 
        self.room1.room_enemies.append("goblin")
        self.room1.room_enemies.append("gaben")

        # Room 1 food
        self.room1.room_items.append("apple")

        # Room 2 food
        self.room2.room_items.append("onion")

        # Room 7 items
        self.room7.room_items.append("sock")

        # All items
        self.all_items = [shovel, flashlight, soda, sock, sword, apple, onion, knife, wallet]

        # All enemies
        self.all_enemies = [goblin, gaben]
