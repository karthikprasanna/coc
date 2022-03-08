import os
from sqlalchemy import true
from src.input import input_to, Get
import src.config as config
from src.village import Village
from src.king import King
import time


if __name__ == '__main__':

    king = King()

    # Initialise the gameboard
    village = Village()


    while true:
        os.system('clear')

        village.construct_village(king)

        village.print_board()

        key = input_to(Get())
        
        if key == 'q':
            break
        elif key in ['w', 's', 'a', 'd', 'up', 'down', 'left', 'right']:
            king.move(key)

        time.sleep(config.FRAME_TIME)
        





