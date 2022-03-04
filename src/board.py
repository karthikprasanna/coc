'''
BOARD
=====

This class denotes the base class for the game board.
'''
import numpy as np
import colors


class Board():

    def __init__(self, rows, columns):
        '''
        Initialises the required board with the length, width and the board matrix
        '''
        self._rows = rows
        self._columns = columns
        self._board = np.full((self._rows, self._columns, 2),
                              ' '*10)

    def getdim(self):
        '''
        A getter function for getting the shape of the board in (rows,columns) format
        '''
        return (self._rows, self._columns)

    def put_to_board(self, X, Y, ASCII, COLOR):
        '''
        Prints the required ASCII character along with its COLOR at (X,Y)
        '''
        self._board[X][Y][0] = ASCII
        self._board[X][Y][1] = COLOR

    def remove_from_board(self, X, Y):
        '''
        Clears the (X,Y) coordinate from the board
        '''
        self.put_to_board(X, Y, " ", "Normal")

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
