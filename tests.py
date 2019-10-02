import unittest
from rover import Rover
from position import Position
from plateau import Plateau


class RoverTests(unittest.TestCase):
    def setUp(self):
        # Initialize new rover with set of instructions including
        # x,y,position,heading,commands
        self.rover = Rover(0, 0, "N", "LMLMLMLMM")

    def test_init(self):
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.heading, 1)
        self.assertEqual(self.rover.commands, "LMLMLMLMM")

    def test_move_rover(self):
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.heading, 1)

    def test_turn_rover_left(self):
        self.assertEqual(self.rover.heading, 1)

    def test_turn_rover_right(self):
        self.assertEqual(self.rover.heading, 1)


if __name__ == "__main__":
    unittest.main()
