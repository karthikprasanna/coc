'''
BOARD
=====

This class denotes the base class for the game board.
'''
import numpy as np
import src.colors as colors
from src.object import Object


class Board():

    def __init__(self, num_rows, num_columns):
        '''
        Initialises the required board with the length, width and the board matrix
        '''
        self._rows = num_rows
        self._columns = num_columns
        self._board = np.full((self._rows, self._columns, 2),
                              " "*50)

    def getdim(self):
        '''
        A getter function for getting the shape of the board in (rows,columns) format
        '''
        return (self._rows, self._columns)

    def write_object_on_board(self, Object):
        '''
        Draw the shape of the object onto the game board and make its type ty
        Also casterise the object onto the baord (make it one with the board)
        '''
        for i in range(Object._h):
            for j in range(Object._w):
                self.put_to_board(
                    Object._h -1 -i + Object._y, j + Object._x, Object._shape[i][j], Object._type)
    
    def remove_object_from_board(self, Object):
        '''
        Removes the object from the board
        '''
        for i in range(Object._h):
            for j in range(Object._w):
                self.remove_from_board(Object._h -1 -i + Object._y, j + Object._x)

    def put_to_board(self, X, Y, character, type):
        '''
        Prints the required ASCII character along with its COLOR at (X,Y)
        '''
        self._board[X][Y][0] = character
        self._board[X][Y][1] = type

    def remove_from_board(self, X, Y):
        '''
        Clears the (X,Y) coordinate from the board
        '''
        self.put_to_board(X, Y, " ", "grass")

    # def get_type(self, X, Y):
    #     '''
    #     Gets the type of the obstacle at (X,Y)
    #     '''
    #     if self._board[X][Y][1] in ['Normal', 'Bg1', 'Bg2']:
    #         return "Normal"
    #     return self._board[X][Y][1]

    def printxy(self, X, Y):
        '''
        Prints a single block at X,Y
        '''
        print(colors.color_text(self._board[X][Y][0], self._board[X][Y][1]), end='')

    def getxy(self, X, Y):
        '''
        Get the block element at X,Y
        '''
        return self._board[X][Y]

    # print the board in the console
    def print_board(self):
        '''
        Prints the board in the console
        '''
        for i in range(self._rows):
            for j in range(self._columns):
                self.printxy(self._rows - 1 - i, j)
            print()