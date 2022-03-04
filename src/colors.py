'''
Has different colours used in the game.
'''
import colorama

COLORS = {
    'Normal': '\x1b[40;37m',
    'hut': '',
    
}

END_COLOR = '\033[m'


def color_text(text, color):
    ''' 
    Colors the text according to the given color
    The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
    '''
    if '\x1b' in color:
        return color + text + END_COLOR
    else:
        try:
            return COLORS[color] + text + END_COLOR
        except:
            return text


def get_color(type_name):
    '''
    returns the color code of the given type
    '''
    return COLORS[type_name]
