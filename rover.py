# Mars Rover
from position import Position


class Grid(object):
    def __init__(self, coordinates, rovers):
        self.coordinates = [0, 0], coordinates
        self.rovers = rovers


class Rover(object):
    commands = {"L": "Left", "R": "Right", "M": "Move forward"}
    directions = {"N": 1, "S": 3, "E": 2, "W": 4}
    heading = directions["N"]
    x = 0
    y = 0
# Initialize plateau, or grid, for Rover

    def __init__(self, x, y, position, heading, commands):
        self.heading = heading
        self.commands = commands
        self.position = Position()
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinates of Rover is {self.x},{self.y}. {self.position}. Heading of Rover is {self.heading}. Commands of rover are {self.commands}"
        # Initial position of Rover

    @classmethod
    def set_position(cls, position, heading, coordinate_x=0, coordinate_y=0):
        cls.position = Position()
        cls.heading = heading
        cls.coordinate_x = coordinate_x
        cls.coordinate_y = coordinate_y

    def moveForward(self, x, y, direction):
        self.x = Position(x)
        self.y = Position(y)
        for dirs in direction:
            if dirs == "N":
                y += 1
            elif dirs == "S":
                y -= 1
            elif dirs == "W":
                x -= 1
            elif dirs == "E":
                x += 1
            else:
                raise ValueError("That's not a valid direction")

    def rotate_rover(self, command):
        self.command = command

        if command == "L":
            self.heading = self.turn_rover_left()
        elif command == "R":
            self.heading = self.turn_rover_right()
        else:
            print('Command is not a turn')

    def turn_rover_left(self):
        if self.heading-1 < self.directions["N"]:
            return self.directions["W"]
        else:
            return self.heading-1

    def turn_rover_right(self):
        if self.heading+1 > self.directions["W"]:
            return self.directions["N"]
        else:
            return self.heading+1


def readfile():
    try:
        f = open("input.txt", "r")
        li = []
        if f.mode == "r":
            for line in f:
                li.append(line.replace("\n", ""))
        f.close()
        if len(li) > 0:
            return li
    except:
        raise TypeError("Nothing to show")


r = Rover(0, 0, (Position()), "N", "LMLMLMLMM")

print(r)
r.moveForward(1, 2, "S")
print(r)
r.moveForward(1, 2, "N")
print(r)
readfile()
# r.rotate_rover("L")
