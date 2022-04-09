import src.config as config
from src.person import Person

class Balloon(Person):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 2, 'balloon', config.balloon_damage, config.balloon_health, config.balloon_movement_speed, config.balloon_attack_range)
        self._piled_up = False   

    def is_over_balloon(self, village, x, y):
    
        for balloon in village._troops:
            if balloon._type.split('_')[0] == 'balloon':
                if x in range(balloon._x, balloon._x + balloon._w) and y in range(balloon._y, balloon._y + balloon._h):
                    return True

        return False     

    def get_direction_to_building(self, building, village):
        x_p = self._x + self._w // 2
        y_p = self._y + self._h // 2

        x_b = building._x + building._w // 2
        y_b = building._y + building._h // 2

        if x_p > x_b and x_p - self._movement_speed // 2 != x_b :
            return 'a'
        elif x_p < x_b and x_p + self._movement_speed //2 != x_b :
            return 'd'
        elif y_p > y_b and y_p - self._movement_speed // 2 != y_b :
            return 's'
        elif y_p < y_b and y_p + self._movement_speed // 2 != y_b :
            return 'w'
        else:
            return None
    
    def move(self, direction, village):
        '''
        Moves the person according to the direction given
        The direction can be given either in wasd or up down left right
       
        '''
        village.remove_object_from_board(self)
        if direction in ['w', 'up']:
            if(self._y + self._h < config.screen_height):
                if not self.is_over_balloon(village, self._x, self._y + self._movement_speed):
                    self._y += self._movement_speed

        elif direction in ['s', 'down']:
            if(self._y > 0):
                if not self.is_over_balloon(village, self._x, self._y - self._movement_speed):
                  self._y -= self._movement_speed

        elif direction in ['a', 'left']:
            if(self._x > 0):
                if not self.is_over_balloon(village, self._x - self._movement_speed, self._y):
                  self._x -= self._movement_speed 

        elif direction in ['d', 'right']:
            if(self._x + self._w < config.screen_width):
                if not self.is_over_balloon(village, self._x + self._movement_speed + self._w, self._y):
                    self._x += self._movement_speed

        village.write_object_on_board(self)
        
    def attack(self, village):
        building = village.get_closest_defensive_building(self, False)

        if building is None:
            building = village.get_closest_building(self, False)
        if building != None:
            if(building.is_near_building(self)):
                building.attack_building(village, self)
            else:   
                direction = self.get_direction_to_building(building, village)
                if direction != None:
                    self.move(direction, village)
                