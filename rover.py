# Mars Rover
from position import Position
from plateau import Plateau


class Rover(object):
    commands = {
        "L": "Left",
        "R": "Right",
        "M": "Move forward"
    }
    directions = {
        "N": 1,
        "E": 2,
        "S": 3,
        "W": 4
    }
    headings = directions["N"]
    x = 0
    y = 0

# Initialize Rover

    def __init__(self, x, y, heading, commands):
        self.x = x
        self.y = y
        self.heading = Rover.directions[heading]
        self.commands = commands

# Represent Rover in a nicer way. It is uninitialized but can be initialized
    # def __repr__(self):
    #     return f"Plateau: {self.plateau}. Position X: {self.x}. Position Y: {self.y}. Heading: {self.heading}. Commands: {self.commands}"

# Set Rover to either 'väderstreck' and move the Rover forward
    def moveRover(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = Rover.directions[heading]
        for c in self.commands:
            # North
            if c == "M":
                if self.heading == Rover.directions["N"] and y < 5:
                    y += 1
                elif self.heading == Rover.directions["S"] and y > 0:
                    y -= 1
                elif self.heading == Rover.directions["E"] and x < 5:
                    x += 1
                elif self.heading == Rover.directions["W"] and x > 0:
                    x -= 1
            elif c == "L":
                self.heading = self.turn_rover_left(
                    self.heading)
            elif c == "R":
                self.heading = self.turn_rover_right(self.heading)
            else:
                print("failure", self.heading, x, y, c)
        print(x, y, heading)

    def turn_rover_left(self, heading):
        if self.heading - 1 < self.directions["N"]:
            return self.directions["W"]
        else:
            return self.heading - 1

    def turn_rover_right(self, heading):
        if self.heading + 1 > self.directions["W"]:
            return self.directions["N"]
        else:
            return self.heading + 1


r = Rover(0, 0, "N", "LMLMLMLMM")

r.moveRover(1, 2, "N")

r1 = Rover(0, 0, "N", "MMRMMRMRRM")
r1.moveRover(3, 3, "E")
