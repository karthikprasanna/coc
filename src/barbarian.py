from distutils.command import config
from person import Person

class Barbarian(Person):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, 'barbarian', config.barbarian_damage, config.barbarian_health, config.brbarian_movement_speed)

    def attack(self):
        pass