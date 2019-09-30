# Mars Rover
from position import Position
from plateau import Plateau


class Rover(object):
    commands = {"L": "Left", "R": "Right",
                "M": "Move forward"}
    directions = {"N": 1, "S": 3, "E": 2, "W": 4}
    headings = directions["N"]
    x = 0
    y = 0

# Initialize Rover

    def __init__(self, position, plateau, heading, commands):
        self.position = Position()
        self.plateau = Plateau(3, 3)
        self.heading = heading
        self.commands = commands
        print(self.directions["N"])


# Represent Rover in a nicer way


    def __repr__(self):
        return f"Position: {self.position}. Plateau: {self.plateau}. Heading: {self.heading}. Commands: {self.commands}"

# Initial position of Rover

    def set_position(self, position, heading, coordinate_x=0, coordinate_y=0):
        self.position = Position()
        self.heading = heading
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

# Set Rover to either 'väderstreck' and move the Rover forward
    def moveForward(self, x, y, direction, commands):
        self.x = Position(x)
        self.y = Position(y)
        self.direction = Rover.directions
        self.commands = commands
        for dirs in Rover.directions:
            for c in commands:
                # North
                if dirs == "N" and y < 5:
                    if c == "M":
                        y += 1
                    elif c == "L":
                        self.heading = self.turn_rover_left()
                    elif c == "R":
                        self.heading = self.turn_rover_right()
                elif dirs == "S" and y > 0:
                    if c == "M":
                        y -= 1
                    elif c == "L":
                        self.heading = self.turn_rover_left()
                    elif c == "R":
                        self.heading = self.turn_rover_right()
                elif dirs == "W" and x > 0:
                    if c == "M":
                        x -= 1
                    elif c == "L":
                        self.heading = self.turn_rover_left()
                    elif c == "R":
                        self.heading = self.turn_rover_right()
                        # East
                elif dirs == "E" and x > 0:
                    if c == "M":
                        x += 1
                    elif c == "L":
                        self.heading = self.turn_rover_left()
                    elif c == "R":
                        self.heading = self.turn_rover_right()
                else:
                    raise ValueError("That's not a valid direction")
                print(x, y, commands)

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


r = Rover((Position()), (Plateau(2, 2)), 1, "RM")
r.moveForward(2, 2, 2, "MMR")
print(r)


# r.moveForward(2, 2, 1)


# r.rotate_rover("L")
