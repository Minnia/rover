import unittest
from rover import Rover
from rover import Grid
from position import Position
from plateau import Plateau


class RoverTests(unittest.TestCase):
    def setup(self):
        # Initialize new rover with set of instructions including
        # x,y,position,heading,commands
        self.rover = Rover(5, 5, (1, 2), "N", "LMLMLMLMM")

    def test_init(self):
        self.assertEqual(self.rover.x, 5)
        self.assertEqual(self.rover.y, 5)
        self.assertEqual(self.rover.position, (1, 2))
        self.assertEqual(self.rover.heading, "N")
        self.assertEqual(self.rover.commands, "LMLMLMLMM")

    def test_repr(self):
        self.assertEqual(repr(
            self.rover), f"Coordinates of Rover is {self.rover.x},{self.rover.y}. {self.rover.position}. Heading of rover is {self.rover.heading}. Commands of rover are {self.rover.commands}")


if __name__ == "__main__":
    unittest.main()
