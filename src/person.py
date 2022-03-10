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

    def __init__(self, x, y, h, w, type, damage, health, movement_speed, attack_range):
        '''
        It just calls the constructor of the parent class object. 
        '''
        super().__init__(x, y, h, w, type)
        self._damage = damage
        self._health = health
        self._movement_speed = movement_speed
        self._attack_range = attack_range

    def attack(self, village):
        for building in village._buildings:
            if(building.is_near_building(self)):
                building.attack_building(village, self)

                break

    def move(self, direction, village):
        '''
        Moves the person according to the direction given
        The direction can be given either in wasd or up down left right
       
        '''
        village.remove_object_from_board(self)
        if direction in ['w', 'up']:
            if(self._y + self._h < config.screen_height):
                if not village.is_occupied(self._x, self._y + self._movement_speed):
                    self._y += self._movement_speed

        elif direction in ['s', 'down']:
            if(self._y > 0):
                if not village.is_occupied(self._x, self._y - self._movement_speed):
                  self._y -= self._movement_speed

        elif direction in ['a', 'left']:
            if(self._x > 0):
                if not village.is_occupied(self._x - self._movement_speed, self._y):
                  self._x -= self._movement_speed 

        elif direction in ['d', 'right']:
            if(self._x + self._w < config.screen_width):
                if not village.is_occupied(self._x + self._movement_speed + self._w, self._y):
                    self._x += self._movement_speed

        village.write_object_on_board(self)

    def damage_person(self, damage):
        '''
        Damages the person by the given amount
        '''
        self._health -= damage

        if '_' in self._type:
            self._type = self._type.split('_')[0]
            
        if self._health in range(20, 50):
            self._type += '_damaged'
        elif self._health in range(1, 20):
            self._type += '_critical'
        elif self._health <= 0:
            self._type += '_destroyed'
            self._health = 0


       