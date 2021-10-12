class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.room_north = ""
        self.room_east = ""
        self.room_south = ""
        self.room_west = ""
        self.room_items = list()
        self.room_enemies = list()


    def set_room_north(self, room):
        self.room_north = room

    def set_room_east(self, room):
        self.room_east = room

    def set_room_south(self, room):
        self.room_south = room

    def set_room_west(self, room):
        self.room_west = room

    def check_room_item(self, name):
        if name in self.room_items:
            return True
        else:
            return False

    def get_room_item(self, name):
        if name in self.room_items:
            return name
        else:
            return False

    def get_room_enemey(self, enemy_name):
        if enemy_name in self.room_enemies:
            return enemy_name
        else:
            return False


