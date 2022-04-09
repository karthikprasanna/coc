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

    'queen': [['🏹','🥷', '']],
    'queen_damaged': [['🏹','🥷', '']],
    'queen_critical': [['🏹','🥷', '']],
    'queen_attacking': [['🏹','🥷', '']],

    'wall': [['▄']],
    'wall_damaged': [['▄']],
    'wall_critical': [['▄']],

    'barbarian': [['🗡','🤺','']],
    'barbarian_damaged': [['🗡','🤺','']],
    'barbarian_critical': [['🗡','🤺','']],
    'barbarian_attacking': [['🗡','🤺','']],

    'archer': [['🏹','🤺','','']],
    'archer_damaged': [['🏹','🤺','','']],
    'archer_critical': [['🏹','🤺','','']],
    'archer_attacking': [['🏹','🤺','','']],

    'tower': [['🗼', '']],
    'tower_damaged': [['🗼', '']],
    'tower_critical': [['🗼', '']],
    'tower_attacking': [['🗼', '']],

    'balloon': [['🎈', '']],
    'balloon_damaged': [['🎈', '']],
    'balloon_critical': [['🎈', '']],
    'balloon_attacking': [['🎈', '']],

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

    'kinghealth_0': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_1': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_2': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_3': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_4': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', ' ', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_5': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', '▄', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_6': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', '▄', ' ', ' ', ' ', ' ', ' ']],
    'kinghealth_7': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', '▄', '▄', '▄', ' ', ' ', ' ']],
    'kinghealth_8': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', '▄', '▄', '▄', '▄', ' ', ' ']],
    'kinghealth_9': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', '▄', '▄', '▄', '▄', '▄', ' ']],
    'kinghealth_10': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄', '▄', '▄', '▄', '▄', '▄', '▄', '▄', '▄', '▄']],


}

def get_shape(type_name):
    '''
    returns the shape of the given name
    '''
    return SHAPES[type_name]
   
    