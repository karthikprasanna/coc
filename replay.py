import os
import src.config as config
from src.village import Village
from src.barbarians import Barbarians
from src.king import King
import time
from src.spell import Spell
from src.bottombar import Bottombar


def get_session(file_obj, session_ID):
    '''
    get the user input from the log file
    '''
    for line in file_obj:
        if line.split(' ')[0] == session_ID:
            user_input = line.split(' ')[1]
            counter = line.split(' ')[2]
            num_barbarians = int(line.split(' ')[3])
            return user_input, counter, num_barbarians
        
    return "Invalid", "", 0


if __name__ == '__main__':

    config.session_ID = input('Enter session ID: ')

    f = open('./replays/logs.txt', 'r')

    user_input, counter, num_barbarians = get_session(f, config.session_ID)

    king = King()

    barbarians = Barbarians(num_barbarians)

    spell = Spell()

    village = Village()

    bar = Bottombar(10, 'kinghealth_10')

    village.construct_village(king, barbarians)
    
    if user_input == "Invalid":
        print("the session ID is invalid")
        exit(0)

    for key in user_input:
        if counter[0] == '1':
            config.clock = True
        else:
            config.clock = False
        counter = counter[1:]

        os.system('clear')

        village.print_board()

        if config.game_over:
            print()
            print(config.game_result)
            f.close()
            break

        if config.clock:
            village.activate_defense()
            bar.update_progress(int(king._health / 10), village)
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
        elif key == 'r':
            if not spell._is_rage_spell_cast:
                spell._is_rage_spell_cast = True
                spell.activate_rage_spell(village)
        elif key == 'h':
            if not spell._is_heal_spell_cast:
                spell._is_heal_spell_cast = True
                spell.activate_heal_spell(village)
            
        time.sleep(config.FRAME_TIME)
        