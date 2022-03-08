from src.building import Building

class Cannon(Building):
    def __init__(self, x, y, damage, range):
        super().__init__(x, y, 1, 2, 'cannon')
        self._damage = damage
        self._range = range
        self._is_shooting = False

    def shoot(self):
        self._is_shooting = True
        self.type = "cannon-shooting"

    def unshoot(self):
        self._is_shooting = False
        self.type = "cannon" 
