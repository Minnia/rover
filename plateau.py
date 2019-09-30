class Plateau(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{self.width},{self.height}"


p = Plateau(5, 5)
# print(p)
