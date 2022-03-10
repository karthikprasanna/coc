import src.config as config

class Spell:
    def __init__(self):
        self._is_rage_spell_cast = False
        self._is_heal_spell_cast = False
    
    def activate_rage_spell(self, village):
        for troop in village._troops:
            troop._damage *= 2
            troop._movement_speed *= 2
    
    def activate_heal_spell(self, village):
        for troop in village._troops:
            troop._health *= 1.5

            if troop._health > config.troop_max_health:
                troop._health = config.troop_max_health

        if '_' in troop._type:
            troop._type = troop._type.split('_')[0]
            
        if troop._health in range(20, 50):
            troop.change_type(troop._type + '_damaged')
        elif troop._health in range(1, 20):
            troop.change_type(troop._type + '_critical')
        elif troop._health <= 0:
            troop.change_type(troop._type + '_destroyed')
            troop._health = 0