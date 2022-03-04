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

from person import Person
import config

class King(Person):

    def __init__(self):
        '''
        Initialises the person with the characteristics of a king
        '''
        super().__init__(config.king_initial_x, config.king_initial_y, 1, 2, 'king', config.king_damage, config.king_health, config.king_movement_speed)

    def attack(self):
        pass