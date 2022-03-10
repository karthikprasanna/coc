'''
obj
===

This class denotes any object, be it an obstacle or a person, that can be rasterised on the board, or can be directly printed to the screen

This is a base class, from which all the game assets are inherited

Data Members
-------------

- x

denotes the starting x coordinate of the object
Note that x axis is the horizontal axis and y axis is the vertical axis
The Board assumes the cartesian co-ordinate system

- y

denotes the starting y coordinate of the object

- h

denotes the height of the object along the x (horizontal) axis

- w

denotes the width of the object along the y (horizontal) axis

- shape

denotes the 2D matrix of ASCII characters to fill the h x w width

- type

denotes the type of the object; used later for painting the board.
Responsible for handling colors and the collisions

Member Functions
-----------------

- Constructor

Just assigns the parameters to its 'protected' variables

- write_self_on_board

Draw the shape of the object onto the game board and make its type ty
Also casterise the object onto the baord (make it one with the board)

- print_direct

Prints the object directly on the screen without disturbing the board

- destroy_self

Destroys itself from the board.

- change_type

Change the type of the object (used for changing the colors of the object mid-game)

- get_coord

Gets the coordinates of the current object in (x,y) format

- get_dim

Gets the dimensions of the current object in (h,w) format

'''
import src.shapes as shapes
import src.colors as colors

class Object:
    def __init__(self, x, y, h, w, type):
        '''
        assigns the parameters to its 'protected' variables
        '''
        self._x = x
        self._y = y
        self._h = h
        self._w = w
        self._type = type
        self._shape = shapes.get_shape(type)
        self._color = colors.get_color(type)
       

    # def print_direct(self):
    #     '''
    #     Prints the object directly on the screen without disturbing the board
    #     '''
    #     print('\033[s')  # save position
    #     for i in range(self._h):
    #         for j in range(self._w):
    #             print('\033['+str(self._x+i+1)+';' +
    #                   str(self._y-j+self._h)+'H'+color_text(self._shape[i][j], self._type), end="")
    #     print('\033[u')  # restore position

    # def destroy_self(self, Board):
    #     '''
    #     Destroys itself from the board.
    #     '''
    #     for i in range(self._h):
    #         for j in range(self._w):
    #             Board.remove_from_board(i+self._x, j+self._y)

    def change_type(self, new_type, village = None):
        '''
        Change the type of the object (used for changing the colors of the object mid-game)
        '''
        if village != None:
            village.remove_object_from_board(self)
            self._type = new_type
            self._shape = shapes.get_shape(new_type)
            village.write_object_on_board(self)
        else:
            self._type = new_type
            self._shape = shapes.get_shape(new_type)

    def get_coord(self):
        '''
        Gets the coordinates of the current object in (x,y) format
        '''
        return (self._x, self._y)

    def get_dim(self):
        '''
        Gets the dimensions of the current object in (h,w) format
        '''
        return (self._h, self._w)
