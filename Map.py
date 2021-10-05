from Room import Room
from Item import Item

class Map(Room):
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

        #Room 3
        self.room3.set_room_south(self.room6)
        self.room3.set_room_west(self.room2)

        #Room 4
        self.room4.set_room_north(self.room1)
        self.room4.set_room_south(self.room7)

        #Room 5
        self.room5.set_room_south(self.room8)

        #room 6
        self.room6.set_room_north(self.room3)
        self.room6.set_room_south(self.room9)

        #Room 7
        self.room7.set_room_north(self.room4)
        self.room7.set_room_east(self.room8)

        #Room 8
        self.room8.set_room_north(self.room5)
        self.room8.set_room_east(self.room9)
        self.room8.set_room_west(self.room7)


        #Room 9
        self.room9.set_room_north(self.room6)
        self.room9.set_room_west(self.room8)


        #Items
        shovel = Item("shovel", "Rusty shovel", 10)
        flashlight = Item("flashlight", "New flashlight", 1)
        soda = Item("soda", "Expired soda", 1)

        #Room 1 Items
        self.room1.room_items.append("shovel")
        self.room1.room_items.append("flashlight")
        self.room1.room_items.append("soda")

        self.all_items = [shovel,flashlight,soda]






