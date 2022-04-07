from src.balloon import Balloon

class Balloons():
    def __init__(self, amount):
            self._amount = amount
            self._is_spawning = False
            self._spawning_point = [0,0]
            self._balloons = []
    
    def create_unit(self, x, y):
        balloon = Balloon(x, y)
        self._balloons.append(balloon)
        return balloon
