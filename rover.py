# Mars Rover
from position import Position
from plateau import Plateau


class Rover(object):
    commands = {"L": "Left", "R": "Right",
                "M": "Move forward"}
    directions = {"N": 1, "S": 3, "E": 2, "W": 4}
    heading = directions["N"]
    x = 0
    y = 0

# Initialize Rover

    def __init__(self, position, plateau, heading, commands):
        self.heading = Rover.heading
        self.commands = commands
        self.position = Position()
        self.plateau = Plateau(2, 2)

# Represent Rover in a nicer way
    def __repr__(self):
        return f"Coordinates of Rover is {self.x},{self.y}. Heading is {self.heading}. Commands: {self.commands}. Position of rover are {self.position}. Plateau: {self.plateau}"

# Initial position of Rover

    def set_position(self, position, heading, coordinate_x=0, coordinate_y=0):
        self.position = Position()
        self.heading = heading
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

# Set Rover to either 'väderstreck' and move the Rover forward
    def moveForward(self, x, y, direction):
        self.x = Position(x)
        self.y = Position(y)
        self.direction = Rover.heading
        for dirs in Rover.directions:
            # North
            if dirs == "N" and y < 5:
                for c in Rover.commands:
                    if c == "M":
                        y += 1
            elif dirs == "S" and y > 0:
                for c in Rover.commands:
                    if c == "M":
                        y -= 1
            elif dirs == "W" and x > 0:
                for c in Rover.commands:
                    if c == "L":
                        x -= 1
                        self.heading = self.turn_rover_left()
                    elif c == "R":
                        x += 1
                        self.heading = self.turn_rover_right()
                        # East
            elif dirs == "E" and x > 0:
                for c in Rover.commands:
                    x -= 1
                    if c == "L":
                        self.heading = self.turn_rover_left()
                    elif c == "R":
                        x += 1
                        self.heading = self.turn_rover_right()
            else:
                raise ValueError("That's not a valid direction")

            # elif dirs == "S" and y > 0:
            #     y -= 1
            # elif dirs == "W" and x > 0:
            #     x -= 1
            # elif dirs == "E" and x > 0:
            #     x += 1
            # else:
            #     raise ValueError("That's not a valid direction")

    # def rotate_rover(self, command):
    #     self.command = command

    #     if command == "L":
    #         self.heading = self.turn_rover_left()
    #     elif command == "R":
    #         self.heading = self.turn_rover_right()
    #     else:
    #         print('Command is not a turn')

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


# def readfile():
#     try:
#         f = open("input.txt", "r")
#         li = []
#         if f.mode == "r":
#             for line in f:
#                 li.append(line.replace("\n", ""))
#         f.close()
#         if len(li) > 0:
#             return li
#     except:
#         raise TypeError("Nothing to show")


# r = Rover((Position())), "N", "LMLMLMLMM", (Plateau(2, 2)))
r1 = Rover((Position()), "S", "LM", (Plateau(3, 4)))
# print(r)
print(r1)
# r.moveForward(2, 2, 1)


# r.rotate_rover("L")
