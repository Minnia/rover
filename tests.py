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


class PlateauTest(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_init(self):
        self.assertEqual(self.plateau.width, 5)
        self.assertEqual(self.plateau.height, 5)

    def test_repr(self):
        self.assertTrue(repr(self.plateau), "5,5")


class PositionTest(unittest.TestCase):
    def setUp(self):
        self.position = Position(0, 0)

    def test_init(self):
        self.assertEqual(self.position.x, 0)
        self.assertEqual(self.position.y, 0)

    def test_repr(self):
        self.assertTrue(repr(self.position), "Position of Rover is 0,0")


if __name__ == "__main__":
    unittest.main()
