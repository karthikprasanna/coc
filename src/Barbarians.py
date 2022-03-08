from src.barbarian import Barbarian

class Barbarians(Barbarian):
    def __init__(x, y, amount):
        super().__init__(x, y, amount, 'barbarians')

    def attack(self):
        pass