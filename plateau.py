class Plateau(object):
    minimum_width_plateau = 0
    minimum_height_plateau = 0

    def __init__(self, width, height, min_width, min_height):
        self.min_width = min_width
        self.min_height = min_height
        self.minimum_width_plateau = min_width
        self.minimum_height_plateau = min_height

    def move(self, position):
        return self.minimum_width_plateau <= position.x <= self.min_width and self.minimum_height_plateau <= position.y <= self.min_height
