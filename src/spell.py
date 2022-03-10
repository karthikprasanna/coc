import config

class Spell:
    def __init__(self, type):
        self._type = type
    
    def activate_rage_spell(self, village):
        for troop in village._troops:
            troop._damage *= 2
            troop._movement_speed *= 2
    
    def activate_heal_spell(self, village):
        for troop in village._troops:
            troop._health *= 1.5

            if troop._health > config.troop_max_health:
                troop._health = config.troop_max_health