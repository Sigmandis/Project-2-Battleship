class Ship:



    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hit_points = size
        self.coordinates = []
        self.horizontal = None

    def __str__(self):
        return self.name

    def sunk(self):
        if self.hit_points <= 0:
            return True

    def damage(self):
        self.hit_points -= 1
