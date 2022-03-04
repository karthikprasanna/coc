from king import King
from barbarian import Barbarian
import config

class Spell:
    def __init__(self, type):
        self._type = type
    
    def activate_rage_spell(self, King, Barbarians):
        for Barbarian in Barbarians:
            Barbarian._damage *= 2
            Barbarian._movement_speed *= 2
        King._damage *= 2
        King._movement_speed *= 2
    
    def activate_heal_spell(self, King, Barbarians):
        for Barbarian in Barbarians:
            Barbarian._health *= 1.5
            if Barbarian._health > config.barbarian_health:
                Barbarian._health = config.barbarian_health

        King._health *= 1.5
        if King._health > config.king_health:
            King._health = config.king_health