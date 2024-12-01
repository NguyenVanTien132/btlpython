vertical_tile_number = 11
tile_size = 64

screen_height = vertical_tile_number * tile_size
screen_width = 1200


levels = {
    0: {
        'file_name': '../levels/level_data/level_0.tmx',
        'node_pos': (100,350),
        'node_graphics': '../graphics/overworld/0',
        'unlock': 1
        },
    1: {
        'file_name': '../levels/level_data/level_1.tmx',
        'node_pos': (225,120),
        'node_graphics': '../graphics/overworld/1',
        'unlock': 2
        },
    2: {
        'file_name': '../levels/level_data/level_2.tmx',
        'node_pos': (315,545),
        'node_graphics': '../graphics/overworld/2',
        'unlock': 3
        },
    3: {
        'file_name': '../levels/level_data/level_3.tmx',
        'node_pos': (430,250),
        'node_graphics': '../graphics/overworld/3',
        'unlock': 4
        },
    4: {
        'file_name': '../levels/level_data/level_4.tmx',
        'node_pos': (580,500),
        'node_graphics': '../graphics/overworld/4',
        'unlock': 5
        },
    5: {
        'file_name': '../levels/level_data/level_5.tmx',
        'node_pos': (710,320),
        'node_graphics':'../graphics/overworld/5',
        'unlock': 6
        },
    6: {
        'file_name': '../levels/level_data/level_6.tmx',
        'node_pos': (825,130),
        'node_graphics':'../graphics/overworld/6',
        'unlock': 7
        },
    7: {
        'file_name': '../levels/level_data/level_7.tmx',
        'node_pos': (875,570),
        'node_graphics':'../graphics/overworld/7',
        'unlock': 8
        },
    8: {
        'file_name': '../levels/level_data/level_8.tmx',
        'node_pos': (1065,300),
        'node_graphics':'../graphics/overworld/8',
        'unlock': 8
        }
    }

layer_counts = {
    "bg_palms": 24,
    "terrain": 1,
    "grass": 19,
    "crates": 27,
    "enemies": 30,
    "constraints": 30,
    "fg_palms": 24,
    "coins": 17,
    "player": 28
}