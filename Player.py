class Player():

    def __init__(self):
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
