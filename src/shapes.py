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

    'kinghealth0': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', ' '*10]],
    'kinghealth1': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*1, ' '*9]],
    'kinghealth2': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*2, ' '*8]],
    'kinghealth3': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*3, ' '*7]],
    'kinghealth4': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*4, ' '*6]],
    'kinghealth5': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*5, ' '*5]],
    'kinghealth6': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*6, ' '*4]],
    'kinghealth7': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*7, ' '*3]],
    'kinghealth8': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*8, ' '*2]],
    'kinghealth9': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*9, ' '*1]],
    'kinghealth10': [['k', 'i', 'n', 'g', '\'', 's', ' ', 'h', 'e', 'a', 'l', 't', 'h', ':', ' ', '▄'*10]],

}

def get_shape(type_name):
    '''
    returns the shape of the given name
    '''
    return SHAPES[type_name]
   
    