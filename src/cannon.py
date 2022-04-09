from src.building import Building

class Cannon(Building):
    def __init__(self, x, y, damage, range):
        super().__init__(x, y, 1, 2, 'cannon')
        self._damage = damage
        self._range = range
        self._is_shooting = False

    def is_in_attacking_range(self, troop):
        ans_x = False
        for i in range(troop._x, troop._x + troop._w + 1):
            if i in range(self._x - self._range, self._x + self._w + self._range):
                ans_x = True
                break

        ans_y = False

        for i in range(troop._y, troop._y + troop._h + 1):
            if i in range(self._y - self._range, self._y + self._h + self._range + 1):
                ans_y = True
                break

        return ans_x and ans_y

    def attack(self, village):
        for troop in village._troops:
            if troop._type.split('_')[0] != 'balloon':
                if self.is_in_attacking_range(troop):
                    village.remove_object_from_board(troop)
                    troop.damage_person(self._damage)
                
                    if '_' in troop._type:
                        if troop._type.split('_')[1] == 'destroyed':
                            # remove troop from the list of troops
                            village._troops.remove(troop)
                        else:
                            village.write_object_on_board(troop)
                    else:
                        village.write_object_on_board(troop)
                    break


