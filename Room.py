class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.room_north = ""
        self.room_east = ""
        self.room_south = ""
        self.room_west = ""
        self.room_items = list()

    def set_room_north(self, room):
        self.room_north = room

    def set_room_east(self, room):
        self.room_east = room

    def set_room_south(self, room):
        self.room_south = room

    def set_room_west(self, room):
         self.room_west = room

    def check_room_item(self, item_name):

        if item_name in self.room_items:
            return item_name
        else:
            return None



