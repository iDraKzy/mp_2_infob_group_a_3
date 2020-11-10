submarines_list = [
    {
        "position_x": 1,
        "position_y": 2,
        "life": 0,
        "direction_x": -1,
        "direction_y": 0
    },
    {
        "position_x": 1,
        "position_y": 2,
        "life": 1,
        "direction_x": -1,
        "direction_y": 0
    },
    {
        "position_x": 1,
        "position_y": 2,
        "life": 2,
        "direction_x": -1,
        "direction_y": 0
    },
    {
        "position_x": 1,
        "position_y": 2,
        "life": 0,
        "direction_x": -1,
        "direction_y": 0
    }
]

for submarine in submarines_list:
    if submarine['life'] != 0:
        print('False')
    elif submarine['life'] == 0:
        print('True')