class Parser():

    def set_user_input(self, input):
        input = self.user_input = input
        return input

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
        result = self.user_input.split(None, 1)
        return result[0]

    def attribute(self):
        try:
            result = self.user_input.split(None, 1)
            return result[1]
        except:
            return False
            print("not a valid input try again")

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
