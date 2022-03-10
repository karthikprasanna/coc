import src.config as config
from src.person import Person

class Barbarian(Person):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 3, 'barbarian', config.barbarian_damage, config.barbarian_health, config.barbarian_movement_speed, config.barbarian_attack_range)
        self._piled_up = False

    def is_over_barbarian(self, x, y, village):
        x_inside = False
        y_inside = False

        for barbarian in village._troops:
            if barbarian._type.split('_')[0] == 'barbarian':
                for i in range(self._x, self._x + self._w ):
                    if i in range(barbarian._x, barbarian._x + barbarian._w):
                        x_inside = True
                        break
                for i in range(self._y, self._y + self._h):
                    if i in range(barbarian._y, barbarian._y + barbarian._h):
                        y_inside = True
                        break
                
                if x_inside and y_inside:
                    return True
        
        return False
        

    def attack(self, village):
        building = village.get_closest_building(self, False)

        if building != None:
            if(building.is_near_building(self)):
                building.attack_building(village, self)

            direction = building.get_direction_to_building(self, village)
            if direction != None:
                self.move(direction, village)
            else:
                building = building.get_blocking_wall(self, village)
                if building != None:
                    building.attack_building(village, self)