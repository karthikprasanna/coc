'''
king
====

This class denotes the king who is controlled by the player.
He is small; he is cute.


It inherits from person class.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Initialises the person with the characteristics of a king


'''

from src.person import Person
import src.config as config

class King(Person):

    def __init__(self):
        '''
        Initialises the person with the characteristics of a king
        '''
        super().__init__(config.king_initial_x, config.king_initial_y, 1, 2, 'king', config.king_damage, config.king_health, config.king_movement_speed, config.king_attack_range)

    def attack(self, village):
        for building in village._buildings:
            if(building.is_near_building(self)):
                village.remove_object_from_board(building)
                self.change_type('king_attacking', village)
                building.damage_building(self._damage)


                if '_' in building._type:
                    if building._type.split('_')[1] == 'destroyed':
                        # remove building from the list of buildings
                        village._buildings.remove(building)
                    else:
                        village.write_object_on_board(building)

                else:
                    village.write_object_on_board(building)

                break

