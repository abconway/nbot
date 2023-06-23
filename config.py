logout_button = (578, 14) # (897, 288)
# out of battle
p1_status = (96, 446) # (415,  720)
p2_status = (222, 446) # (541,  720)
p3_status = (348, 446) # (667,  720)
# in battle
p1_status = (254, 426)
p2_status = (406, 426)
p3_status = (558, 426)
battle_icon = (22, 300)

config = {
    'icon_sizes':{
        '32x32': {
            'battle_icon': {
                'width': 28,
                'height': 28,
                'global_offset': (-556, 286),
            },
            'command_word': {
                'width': 96,
                'height': 14,
                'global_offset': (-402, 282),
            },
            'numbers': {
                'width': 14,
                'height': 14,
            },
            'party_icon': {
                'width': 32,
                'height': 32,
                'global_offset': (-186, 430),
            },
            'status': {
                'hp1_offset': (0, 0),
                'hp2_offset': (14, 0),
                'hp3_offset': (28, 0),
                'mp1_offset': (0, 16),
                'mp2_offset': (14, 16),
                'mp3_offset': (28, 16),
                'global_offset': {
                    'in_battle': {
                        'p1': (-324, 412),
                        'p2': (-172, 412),
                        'p3': (-20, 412),
                    },
                    'out_of_battle': {
                        'p1': (-482, 432),
                        'p2': (-356, 432),
                        'p3': (-230, 432),
                    },
                },
            },
        },
    },
    'numbers': {
        '0': (0, 0, 14, 14),
        '1': (14, 0, 28, 14),
        '2': (28, 0, 42, 14),
        '3': (42, 0, 56, 14),
        '4': (56, 0, 70, 14),
        '5': (70, 0, 84, 14),
        '6': (84, 0, 98, 14),
        '7': (98, 0, 112, 14),
        '8': (112, 0, 126, 14),
        '9': (126, 0, 140, 14),
    },
}