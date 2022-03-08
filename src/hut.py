from src.building import Building

class Hut(Building):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, 'hut')
        