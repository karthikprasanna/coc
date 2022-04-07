import src.config as config
from src.person import Person

class Archer(Person):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 4, 'archer', config.archer_damage, config.archer_health, config.archer_movement_speed, config.archer_attack_range)
        self._piled_up = False        

    def is_over_archer(self, village, x, y):
    
        for archer in village._troops:
            if archer._type.split('_')[0] == 'archer':
                if x in range(archer._x, archer._x + archer._w) and y in range(archer._y, archer._y + archer._h):
                    return True

        return False

    def get_direction_to_building(self, building, village):
        x_p = self._x + self._w // 2
        y_p = self._y + self._h // 2

        x_b = building._x + building._w // 2
        y_b = building._y + building._h // 2

        if x_p > x_b and x_p - self._movement_speed // 2 != x_b and (not village.is_occupied(self._x - 1, self._y) or self.is_over_archer(village, self._x - 1, self._y)):
            return 'a'
        elif x_p < x_b and x_p + self._movement_speed //2 != x_b and (not village.is_occupied(self._x + self._w, y_p) or self.is_over_archer(village, self._x + self._w, y_p)):
            return 'd'
        elif y_p > y_b and y_p - self._movement_speed // 2 != y_b and (not village.is_occupied(self._x, self._y - 1) or self.is_over_archer(village, self._x, self._y - 1)):
            return 's'
        elif y_p < y_b and y_p + self._movement_speed // 2 != y_b and (not village.is_occupied(self._x, self._y + self._h) or self.is_over_archer(village, self._x, self._y + self._h)):
            return 'w'
        else:
            return None
        
    def get_blocking_wall(self, building, village):
        x_p = self._x + self._w // 2
        y_p = self._y + self._h // 2

        x_b = building._x + building._w // 2
        y_b = building._y + building._h // 2

        if x_p > x_b and (village.is_occupied(self._x - 1, self._y) and not self.is_over_archer(village, self._x - 1, self._y)):
            return village.get_wall(self._x - 1, self._y)
        elif x_p < x_b and (village.is_occupied(self._x + self._w, y_p) and not self.is_over_archer(village, self._x + self._w, y_p)):
            return village.get_wall(self._x + self._w, y_p)
        elif y_p > y_b and (village.is_occupied(self._x, self._y - 1) and not self.is_over_archer(village, self._x, self._y - 1)):
            return village.get_wall(self._x, self._y - 1)
        elif y_p < y_b and (village.is_occupied(self._x, self._y + self._h) and not self.is_over_archer(village, self._x, self._y + self._h)):
            return village.get_wall(self._x, self._y + self._h)
        else:
            return None

    def attack(self, village):
        building = village.get_closest_building(self, False)

        if building != None:
            if(building.is_near_building(self)):
                building.attack_building(village, self)
            else:   
                direction = self.get_direction_to_building(building, village)
                if direction != None:
                    self.move(direction, village)
                else:
                    building = self.get_blocking_wall(building, village)
                    if building != None:
                        building.attack_building(village, self)