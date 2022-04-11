import os
from src.input import input_to, Get
import src.config as config
from src.village import Village
from src.barbarians import Barbarians
from src.archers import Archers
from src.balloons import Balloons
from src.king import King
from src.queen import Queen
import time

if __name__ == '__main__':

    choose_king = input('Type 1 to choose a king or 2 to choose a queen: ')
    if choose_king == '1':
        king = King()
    elif choose_king == '2':
        king = Queen()
    else:
        print('Invalid input')
        exit()

    num_barbarians = input('Enter number of barbarians: ')
    num_archers = input('Enter number of archers: ')
    num_balloons = input('Enter number of balloons: ')

    barbarians = Barbarians(int(num_barbarians))
    archers = Archers(int(num_archers))
    balloons = Balloons(int(num_balloons))

    village = Village(config.level)

    village.construct_village(king)

    prev_time = time.time()
    
    while True:
        if time.time() - prev_time > 0.1:
            prev_time = time.time()
            config.clock = not config.clock

        os.system('clear')

        village.reconstruct_village()
        village.print_board()

        if config.game_over:
            print(config.game_result)
            if config.game_result == 'Victory' and config.level < 3:
                play = input('Do you want to play the next level (y/n): ')
                if play == 'y':

                    config.level += 1

                    config.game_over = False

                    config.game_result = " "*10


                    num_barbarians = input('Enter number of barbarians: ')
                    num_archers = input('Enter number of archers: ')
                    num_balloons = input('Enter number of balloons: ')

                    barbarians = Barbarians(int(num_barbarians))
                    archers = Archers(int(num_archers))
                    balloons = Balloons(int(num_balloons))

                    village = Village(config.level)

                    village.construct_village(king)

                    prev_time = time.time()

                    continue
                elif play == 'n':
                    break
                else:
                    print('Invalid input')
                    break
            break

        if config.clock:
            config.can_attack = True
            if config.can_defend:
                village.activate_defense()
                config.can_defend = False
            if village.is_village_destroyed():
                config.game_result = "Victory"
                config.game_over = True
            elif village.is_troops_lost(barbarians, archers, balloons):
                config.game_result = "Defeat"
                config.game_over = True

        if not config.clock:
            config.can_defend = True
            if config.can_attack:
                village.activate_attack()
                config.can_attack = False

        key = input_to(Get())


        if key == 'q':
            config.game_over = True
        elif key in ['w', 's', 'a', 'd']:
            if king._health > 0:
                king.move(key, village)
        elif key in ['k', 'o', 'l']:
            if not barbarians._is_spawning:
                village.spawn(key, barbarians)
        elif key in ['f', 't', 'g']:
            if not archers._is_spawning:
                village.spawn(key, archers)
        elif key in ['h', 'u', 'j']:
            if not balloons._is_spawning:
                village.spawn(key, balloons)
        elif key == ' ':
            if king._health > 0:
                king.attack(village)
        
            
        time.sleep(config.FRAME_TIME)
        