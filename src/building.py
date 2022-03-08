from src.object import Object

class Building(Object):
    def __init__(self, x, y, h, w, type):
        super().__init__(x, y, h, w, type)
        self._hitpoints = 3
      
    def damage_building(self):
        if(self._hitpoints > 0):
            self._hitpoints -= 1
        if(self._hitpoints == 0):
            # destroty the building
            pass
    
    def renovate_building(self):
        self._hitpoints = 3


     