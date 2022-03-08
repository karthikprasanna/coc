from src.board import Board
import src.config as config
from src.townhall import Townhall
from src.hut import Hut
from src.cannon import Cannon
from src.wall import Wall
from src.king import King

class Village(Board):
    def __init__(self):
        super().__init__(config.screen_height, config.screen_width)


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

    def construct_cannon(self):
        cannon1 = Cannon(config.cannon1_x, config.cannon1_y, config.cannon1_damage, config.cannon1_range)
        self.write_object_on_board(cannon1)

        cannon2 = Cannon(config.cannon2_x, config.cannon2_y, config.cannon2_damage, config.cannon2_range)
        self.write_object_on_board(cannon2)

    def construct_wall(self):
        for i in range(config.wall_a_x - 5, config.wall_b_x + 5):
            wall = Wall(i, config.wall_a_y - 5)
            self.write_object_on_board(wall)

        for i in range(config.wall_b_y - 5, config.wall_c_y + 5):
            wall = Wall(config.wall_b_x + 5, i)
            self.write_object_on_board(wall)

        for i in range(config.wall_d_x - 5, config.wall_c_x + 5):
            wall = Wall(i, config.wall_c_y + 5)
            self.write_object_on_board(wall)

        for i in range(config.wall_a_y - 5, config.wall_d_y + 5):
            wall = Wall(config.wall_d_x - 5, i)
            self.write_object_on_board(wall)

    def deploy_king(self, King):
          self.write_object_on_board(King)  

    # write the village on the board    
    def construct_village(self, King):
        self.generate_background()
        self.construct_townhall()
        self.construct_cannon()
        self.construct_hut()
        self.construct_wall()
        self.deploy_king(King)