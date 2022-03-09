'''
contains the shpes of different objects
'''
SHAPES = {
    'hut': [['🛖']],
    'hut_damaged': [['🛖']],
    'hut_critical': [['🛖']],

    'king': [['🗡','🥷']],
    'king_damaged': [['🗡','🥷']],
    'king_critical': [['🗡','🥷']],
    'king_attacking': [['🗡','🥷']],

    'wall': [['▄']],
    'wall_damaged': [['▄']],
    'wall_critical': [['▄']],

    'barbarian': [['🗡','🤺','']],
    'barbarian_damaged': [['🗡','🤺','']],
    'barbarian_critical': [['🗡','🤺','']],
    'barbarian_attacking': [['🗡','🤺','']],

    'townhall': [
        ['ℿ', '—', '—', 'ℿ'],
        ['‖', 'ℿ', 'ℿ', '‖'],
        ['‖', 'ℿ', 'ℿ', '‖']
    ],
    'townhall_damaged': [
        ['ℿ', '—', '—', 'ℿ'],
        ['‖', 'ℿ', 'ℿ', '‖'],
        ['‖', 'ℿ', 'ℿ', '‖']
    ],
    'townhall_critical': [
        ['ℿ', '—', '—', 'ℿ'],
        ['‖', 'ℿ', 'ℿ', '‖'],
        ['‖', 'ℿ', 'ℿ', '‖']
    ],

    'cannon': [['📣', '']],
    'cannon_damaged': [['📣', '']],
    'cannon_critical': [['📣', '']],
    'cannon_attacking': [['🔥', '']],
}

def get_shape(type_name):
    '''
    returns the shape of the given name
    '''
    return SHAPES[type_name]
   
    