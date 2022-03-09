'''
Has different colours used in the game.
'''
from colorama import Fore, Back, Style

COLORS = {
    'Normal': '\x1b[40;37m',
    'townhall': '\x1b[40;37m',
    'townhall_damaged': '\x1b[41;37m',
    'townhall_critical': '\x1b[43;37m',

    'hut': '\x1b[40;37m',
    'hut_damaged': '\x1b[41;37m',
    'hut_critical': '\x1b[43;37m',

    'king': '\x1b[40;37m',
    'king_attacking': '\x1b[40;37m',
    'king_damaged': '\x1b[41;37m',
    'king_critical': '\x1b[43;37m',

    'barbarian': '\x1b[40;37m',
    'barbarian_attacking': '\x1b[40;37m',
    'barbarian_damaged': '\x1b[41;37m',
    'barbarian_critical': '\x1b[43;37m',

    'cannon': '\x1b[40;37m',
    'cannon_attacking': '\x1b[40;37m',
    'cannon_damaged': '\x1b[41;37m',
    'cannon_critical': '\x1b[43;37m',

    'wall': '\x1b[40;37m',
    'wall_damaged': '\x1b[41;37m',
    'wall_critical': '\x1b[43;37m',
    
    'grass': '\x1b[42;37m',
    'debug': '\x1b[42;37m'
    
}

END_COLOR = '\033[m' # reset the color to default


def color_text(text, type):
    ''' 
    Colors the text according to the given color
    The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
    '''
    color = get_color(type)
    try:
        if '\x1b' in color:
            return color + text + END_COLOR
        else:
            return color + text
    except:
        return text


def get_color(type_name):
    '''
    returns the color code of the given type
    '''

    return COLORS[type_name]
