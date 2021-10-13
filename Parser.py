def welcome_text():
    print("welcome to the game")
    print("to move between rooms type go followed by a direction")
    print("you can go 'north', 'east', 'south', 'west'")
    print("you can take items by typing take 'item name'")
    print("you can drop items by typing drop 'item name'")
    print("you can look for items in the room by typing 'look'")
    print("you can view your inventory by typing 'inv'")


class Parser:

    def __init__(self):
        self.user_input = ""
        self.current_room = ""

    def set_user_input(self, user_input):
        user_input = self.user_input = user_input
        return user_input

    def set_current_room(self, current_room):
        self.current_room = current_room
        return current_room

    def direction_validation(self):
        direction = self.attribute()
        if direction == "n" or direction == "north":
            return "north"
        elif direction == "e" or direction == "east":
            return "east"
        elif direction == "s" or direction == "south":
            return "south"
        elif direction == "w" or direction == "west":
            return "west"
        else:
            return "not a direction"

    def command(self):
        try:
            result = self.user_input.split(None, 1)
            return result[0]
        except IndexError:
            print("write a command")

    def attribute(self):
        try:
            result = self.user_input.split(None, 1)
            return result[1]
        except:
            return False

    def set_direction(self):
        direction = self.direction_validation()
        if direction == "north":
            return self.current_room.room_north
        if direction == "east":
            return self.current_room.room_east
        if direction == "south":
            return self.current_room.room_south
        if direction == "west":
            return self.current_room.room_west
