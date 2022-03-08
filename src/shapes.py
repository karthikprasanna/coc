'''
contains the shpes of different objects
'''
SHAPES = {
    'hut': [['🛖']],
    'king': [['🗡','🥷']],
    'wall': [['▄']],
    'barbarian': [['🗡','🤺']],
    'townhall': [
        ['ℿ', '—', '—', 'ℿ'],
        ['‖', 'ℿ', 'ℿ', '‖'],
        ['‖', 'ℿ', 'ℿ', '‖']
    ],
    'cannon': [['📣', '']],

    # 'king': [
    #     [' ', '▄', ' '],
    #     ['\\', '|', '/'],
    #     [' ', '|', ' '],
    #     ['/', ' ','\\']
    # ],

    # 'barbarian': [
    #     [' ', '▄', ' '],
    #     ['/', '|', '\\'],
    # ]
}

def get_shape(type_name):
    '''
    returns the shape of the given name
    '''
    return SHAPES[type_name]
   
    