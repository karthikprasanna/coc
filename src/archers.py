from src.archer import Archer

class Archers():
    def __init__(self, amount):
            self._amount = amount
            self._is_spawning = False
            self._spawning_point = [0,0]
            self._archers = []
    
    def create_unit(self, x, y):
        archer = Archer(x, y)
        self._archers.append(archer)
        return archer

    