'''
person
======

This class denotes the charcters in the game
It is the base class for king and the barbarians

It inherits from the class Object.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- constructor

It just calls the constructor of the parent class object. 

- move

Moves the hero according to the direction given
The direction can be given either in wasd or up down left right

'''

from src.object import Object
import src.config as config

class Person(Object):

    def __init__(self, x, y, h, w, type, damage, health, movement_speed):
        '''
        It just calls the constructor of the parent class object. 
        '''
        super().__init__(x, y, h, w, type)
        self._damage = damage
        self._health = health
        self._movement_speed = movement_speed

    def move(self, direction):
        '''
        Moves the person according to the direction given
        The direction can be given either in wasd or up down left right
       
        '''
        if direction in ['w', 'up']:
            if(self._y + self._h < config.screen_height):
                self._y += 1
        elif direction in ['s', 'down']:
            if(self._y > 0):
                self._y -= 1
        elif direction in ['a', 'left']:
            if(self._x > 0):
                self._x -= 1
        elif direction in ['d', 'right']:
            if(self._x + self._w < config.screen_width):
                self._x += 1
       