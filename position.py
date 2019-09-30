class Position:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# What does this mean?

    def __repr__(self):
        return f"Position of Rover is {self.x},{self.y}"
