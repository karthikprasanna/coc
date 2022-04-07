from src.barbarian import Barbarian

class Barbarians():
    def __init__(self, amount):
            self._amount = amount
            self._is_spawning = False
            self._spawning_point = [0,0]
            self._barbarians = []

    def create_unit(self, x, y):
        barbarian = Barbarian(x, y)
        self._barbarians.append(barbarian)
        return barbarian

    



