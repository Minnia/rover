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

    def __init__(self, plateau, x, y, heading, commands):
        self.x = x
        self.y = y
        self.plateau = Plateau(5, 5)
        self.heading = Rover.directions[heading]
        self.commands = commands


# Represent Rover in a nicer way


    def __repr__(self):
        return f"Plateau: {self.plateau}. Position X: {self.x}. Position Y: {self.y}. Heading: {self.heading}. Commands: {self.commands}"

# Initial position of Rover

    def set_position(self, position, heading, coordinate_x, coordinate_y):
        self.position = position
        self.heading = heading
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

# Set Rover to either 'väderstreck' and move the Rover forward
    def moveForward(self, x, y, heading, commands):
        self.x = x
        self.y = y
        self.heading = Rover.directions[heading]
        self.commands = commands

        for c in commands:
            # North
            if heading == "N" and y < 5:
                if c == "M":
                    y += 1
                elif c == "L":
                    self.heading = self.turn_rover_left()
                elif c == "R":
                    self.heading = self.turn_rover_right()

            elif heading == "S" and y > 0:
                if c == "M":
                    y -= 1
                elif c == "L":
                    self.heading = self.turn_rover_left()

                elif c == "R":
                    self.heading = self.turn_rover_right()

            elif heading == "W" and x > 0:
                if c == "M":
                    x -= 1
                elif c == "L":
                    self.heading = self.turn_rover_left()

                elif c == "R":
                    self.heading = self.turn_rover_right()

                    # East
            elif heading == "E" and x < 5:
                if c == "M":
                    x += 1
                elif c == "L":
                    self.heading = self.turn_rover_left()
                elif c == "R":
                    self.heading = self.turn_rover_right()
            else:
                print(x, y)
                raise ValueError("That's not a valid direction")
            print(x, y, heading, "done")

    def turn_rover_left(self):
        if self.headings-1 < self.directions["N"]:
            return self.directions["W"]
        else:
            return self.headings-1

    def turn_rover_right(self):
        if self.headings+1 > self.directions["W"]:
            return self.directions["N"]
        else:
            return self.headings+1


r = Rover((Plateau(5, 5)), 0, 0, "N", "LMLMLMLMM")

print(r)
r.moveForward(1, 2, "N", "LMLMLMLMM")
print(r)
