from matplotlib.pyplot import bar
from src.object import Object

class Building(Object):
    def __init__(self, x, y, h, w, type):
        super().__init__(x, y, h, w, type)
        self._hitpoints = 100
      
    def damage_building(self, damage):
        self._hitpoints -= damage
        if '_' in self._type:
            self._type = self._type.split('_')[0]


        if self._hitpoints in range(20, 50):
            self._type += '_damaged'
        elif self._hitpoints in range(1, 20):
            self._type += '_critical'
        elif self._hitpoints <= 0:
            self._type += '_destroyed'
            self._hitpoints = 0

    def attack_building(self, village, person):
        village.remove_object_from_board(self)
        self.damage_building(person._damage)


        if '_' in self._type:
            if self._type.split('_')[1] == 'destroyed':
                # remove building from the list of buildings
                village._buildings.remove(self)
                if self._type.split('_')[0] == "cannon" or self._type.split('_')[0] == "tower":
                    
                    village._defense.remove(self)
            else:
                village.write_object_on_board(self)

        else:
            village.write_object_on_board(self)
    
    def renovate_building(self):
        self._hitpoints = 100
        if '_' in self._type:
            self._type = self._type.split('_')[0]

    def is_inside_building(self, x, y):
        if(x >= self._x and x <= self._x + self._w and y >= self._y and y <= self._y + self._h):
            return True
        else:
            return False

    def is_near_building(self, person):
        ans_x = False
        for i in range(person._x, person._x + person._w + 1):
            if i in range(self._x - person._attack_range, self._x + self._w + person._attack_range + 1):
                ans_x = True
                break

        ans_y = False

        for i in range(person._y, person._y + person._h + 1):
            if i in range(self._y - person._attack_range, self._y + self._h + person._attack_range + 1):
                ans_y = True
                break

        return ans_x and ans_y

    def is_near_building_for_queen(self, queen):
        x = queen._x
        y = queen._y

        if queen._facing_direction == 'w':
            y+=8
        elif queen._facing_direction == 's':
            y-=8
        elif queen._facing_direction == 'a':
            x-=8
        elif queen._facing_direction == 'd':
            x+=8

        ans_x = False
        for i in range(x, x + queen._w + 1):
            if i in range(self._x - queen._attack_range, self._x + self._w + queen._attack_range + 1):
                ans_x = True
                break

        ans_y = False

        for i in range(y, y + queen._h + 1):
            if i in range(self._y - queen._attack_range, self._y + self._h + queen._attack_range + 1):
                ans_y = True
                break

        return ans_x and ans_y



    def get_distance_to_building(self, person):
        x_p = person._x + person._w // 2
        y_p = person._y + person._h // 2

        x_b = self._x + self._w // 2
        y_b = self._y + self._h // 2

        return ((x_p - x_b) ** 2 + (y_p - y_b) ** 2) ** 0.5
     