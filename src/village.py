from src.board import Board
import src.config as config
from src.townhall import Townhall
from src.hut import Hut
from src.cannon import Cannon
from src.wall import Wall
from src.barbarian import Barbarian
from src.bottombar import Bottombar

class Village(Board):
    def __init__(self):
        super().__init__(config.screen_height, config.screen_width)
        self._buildings = []
        self._troops = []
        self._defense = []


    def generate_background(self):
        '''
        generate a background filled with grass
        '''
        for i in range(self._rows):
            for j in range(self._columns):
                self.put_to_board(i, j, ' ', 'grass')  

    # construct the town hall in the village
    def construct_townhall(self):
        townhall = Townhall()
        self._buildings.append(townhall)
        self.write_object_on_board(townhall)

    def construct_hut(self):
        hut1 = Hut(config.hut1_x, config.hut1_y)
        self.write_object_on_board(hut1)       

        hut2 = Hut(config.hut2_x, config.hut2_y)
        self.write_object_on_board(hut2)

        hut3 = Hut(config.hut3_x, config.hut3_y)
        self.write_object_on_board(hut3)

        hut4 = Hut(config.hut4_x, config.hut4_y)
        self.write_object_on_board(hut4)

        hut5 = Hut(config.hut5_x, config.hut5_y)
        self.write_object_on_board(hut5)

        self._buildings.append(hut1)
        self._buildings.append(hut2)
        self._buildings.append(hut3)
        self._buildings.append(hut4)
        self._buildings.append(hut5)

    def construct_cannon(self):
        cannon1 = Cannon(config.cannon1_x, config.cannon1_y, config.cannon1_damage, config.cannon1_range)
        self.write_object_on_board(cannon1)

        cannon2 = Cannon(config.cannon2_x, config.cannon2_y, config.cannon2_damage, config.cannon2_range)
        self.write_object_on_board(cannon2)

        self._buildings.append(cannon1)
        self._buildings.append(cannon2)

        self._defense.append(cannon1)
        self._defense.append(cannon2)

    def construct_wall(self):
        for i in range(config.wall_a_x - 5, config.wall_b_x + 5):
            wall = Wall(i, config.wall_a_y - 5)
            self._buildings.append(wall)
            self.write_object_on_board(wall)

        for i in range(config.wall_b_y - 5, config.wall_c_y + 5):
            wall = Wall(config.wall_b_x + 5, i)
            self._buildings.append(wall)
            self.write_object_on_board(wall)

        for i in range(config.wall_d_x - 5, config.wall_c_x + 5):
            wall = Wall(i, config.wall_c_y + 5)
            self._buildings.append(wall)
            self.write_object_on_board(wall)

        for i in range(config.wall_a_y - 5, config.wall_d_y + 5):
            wall = Wall(config.wall_d_x - 5, i)
            self._buildings.append(wall)
            self.write_object_on_board(wall)

    def deploy_king(self, king):
        self._troops.append(king)
        self.write_object_on_board(king) 

    def spawn(self, controller, barbarians):
        barbarians._is_spawning = True
        barbarians._spawning_point = config.spawning_point[controller]
        for i in range(barbarians._amount):
            barbarians._barbarians.append(Barbarian(barbarians._spawning_point[0], barbarians._spawning_point[1]))
            self._troops.append(barbarians._barbarians[i])
            self.write_object_on_board(barbarians._barbarians[i])

    def is_occupied(self, x, y):
        if self._board[y][x][0] == ' ':
            return False
        else:
            return True

    def get_wall(self, x, y):
        for building in self._buildings:
            if building._type.split('_')[0] == 'wall':
                if building._x == x and building._y == y:
                    return building
        return None
        

    def activate_defense(self):
        for cannon in self._defense:
            for troop in self._troops:
                if cannon.is_in_attacking_range(troop):
                    cannon.attack(self, troop)
                    break

    def get_closest_building(self, person, include_wall=True):
        '''
        get the closest building to the person
        '''
        closest_building = None
        closest_distance = config.screen_height + config.screen_width
        for building in self._buildings:
            if building._type.split('_')[0] == 'wall' and include_wall == False:
                continue
            distance =  building.get_distance_to_building(person)
            if distance < closest_distance:
                closest_distance = distance
                closest_building = building
        return closest_building

    def is_over_barbarian(self, x, y):
    
        for barbarian in self._troops:
            if barbarian._type.split('_')[0] == 'barbarian':
                if x in range(barbarian._x, barbarian._x + barbarian._w) and y in range(barbarian._y, barbarian._y + barbarian._h):
                    return True

        return False

    def activate_attack(self):
        for troop in self._troops:
            if troop._type.split('_')[0] == 'barbarian':
                troop.attack(self)

    def is_village_destroyed(self):
        for building in self._buildings:
            if building._type.split('_')[0] != 'wall':
                return False
            
        return True

    def is_troops_lost(self, barbarians):
        if len(self._troops) == 0 and barbarians._is_spawning:
            return True
        else:
            return False
            

    # write the village on the board    
    def construct_village(self, king, barbarians):
        self.generate_background()
        self.construct_townhall()
        self.construct_cannon()
        self.construct_hut()
        self.construct_wall()
        self.deploy_king(king)