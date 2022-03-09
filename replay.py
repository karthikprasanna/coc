import os
import src.config as config
from src.village import Village
from src.barbarians import Barbarians
from src.king import King
import time

def get_user_input(file_obj, session_ID):
    '''
    get the user input from the log file
    '''
    for line in file_obj:
        if line.split(' ')[0] == session_ID:
            user_input = line.split(' ')[1]
            return user_input
        
    return "Invalid"

if __name__ == '__main__':

    king = King()

    barbarians = Barbarians(10)

    village = Village()

    village.construct_village(king, barbarians)

    prev_time = time.time()

    config.session_ID = input('Enter session ID: ')
    
    f = open('./replays/logs.txt', 'r')

    user_input = get_user_input(f, config.session_ID)

    if user_input == "Invalid":
        print("the session ID is invalid")
        print(config.session_ID)
        exit(0)

    for key in user_input:
        if time.time() - prev_time > 0.5:
            prev_time = time.time()
            config.clock = not config.clock

        os.system('clear')

        village.print_board()

        if config.game_over:
            print()
            print(config.game_result)
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

        if key == 'q':
            config.game_over = True
        elif key in ['w', 's', 'a', 'd']:
            if king._health > 0:
                king.move(key, village)
        elif key in ['k', 'o', 'l']:
            if not barbarians._is_spawning:
                village.spawn(key, barbarians)
        elif key == 'm':
            if king._health > 0:
                king.attack(village)
            
        time.sleep(config.FRAME_TIME)
        