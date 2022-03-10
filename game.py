import os
from src.input import input_to, Get
import src.config as config
from src.village import Village
from src.barbarians import Barbarians
from src.king import King
import time


if __name__ == '__main__':

    king = King()

    barbarians = Barbarians(50)

    village = Village()

    village.construct_village(king, barbarians)

    prev_time = time.time()

    config.session_ID = prev_time
    
    # add the session ID to the log file
    f = open('./replays/logs.txt', 'a')
    f.write(str(config.session_ID) + ' ')

    user_input = []
    counter = []

    while True:
        if time.time() - prev_time > 0.5:
            prev_time = time.time()
            config.clock = not config.clock
        counter.append(config.clock)

        os.system('clear')

        village.print_board()

        if config.game_over:
            print(config.game_result)
            print("your session ID is: " + str(config.session_ID))
            user_input.append('n')
            for ch in user_input:
                f.write(str(ch))
            f.write(' ')
            for c in counter:
                if c:
                    f.write("1")
                else:
                    f.write("0")
            f.write("\n")
            f.close()
            break

        if config.clock:
            village.activate_defense()
            if village.is_village_destroyed():
                config.game_result = "Victory"
                config.game_over = True
            elif village.is_troops_lost(barbarians):
                config.game_result = "Defeat"
                config.game_over = True

        if not config.clock:
            if barbarians._is_spawning:
                village.activate_attack()

        key = input_to(Get())

        if key != ' ':
            user_input.append(key)
        else:
            user_input.append('m')

        if key == 'q':
            config.game_over = True
        elif key in ['w', 's', 'a', 'd']:
            if king._health > 0:
                king.move(key, village)
        elif key in ['k', 'o', 'l']:
            if not barbarians._is_spawning:
                village.spawn(key, barbarians)
        elif key == ' ':
            if king._health > 0:
                king.attack(village)
            
        time.sleep(config.FRAME_TIME)
        