from src.person import Person
import src.config as config

class Queen(Person):
    def __init__(self):
        super().__init__(config.queen_initial_x, config.queen_initial_y, 1, 3, 'queen', config.queen_damage, config.queen_health, config.queen_movement_speed, config.queen_attack_range)
        self._attack_distance = config.queen_attack_distance
        self._facing_direction = 'w'

    def move(self, direction, village):
        '''
        Moves the person according to the direction given
        The direction can be given either in wasd or up down left right
       
        '''
        village.remove_object_from_board(self)
        if direction in ['w', 'up']:
            if(self._y + self._h < config.screen_height):
                if not village.is_occupied(self._x, self._y + self._movement_speed):
                    self._y += self._movement_speed
                    self._facing_direction = 'w'

        elif direction in ['s', 'down']:
            if(self._y > 0):
                if not village.is_occupied(self._x, self._y - self._movement_speed):
                  self._y -= self._movement_speed
                  self._facing_direction = 's'

        elif direction in ['a', 'left']:
            if(self._x > 0):
                if not village.is_occupied(self._x - self._movement_speed, self._y):
                  self._x -= self._movement_speed 
                  self._facing_direction = 'a'

        elif direction in ['d', 'right']:
            if(self._x + self._w < config.screen_width):
                if not village.is_occupied(self._x + self._movement_speed + self._w, self._y):
                    self._x += self._movement_speed
                    self._facing_direction = 'd'

        village.write_object_on_board(self)
    
    def attack(self, village):
        for building in village._buildings:
            if(building.is_near_building_for_queen(self)):
                building.attack_building(village, self)