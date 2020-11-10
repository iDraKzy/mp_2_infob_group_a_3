def check_submarines_life(submarines_list):
    """Checks if all submarines's life are different of 0

    Parameters
    ----------
    submarines_list: The list of submarines (list)

    Returns
    -------
    submarines_alive: Wether the submarines are alive (bool)
    
    """

    submarines_alive = False
    submarines_index = 0

    while not submarines_alive and submarines_index < len(submarines_list):
        print(submarines_list[submarines_index]['life'])
        if submarines_list[submarines_index]['life'] != 0:
            submarines_alive = True
        submarines_index += 1

    return submarines_alive

submarines_list = [
    {
        "position_x": 1,
        "position_y": 2,
        "life": 0,
        "direction_x": 0,
        "direction_y": -1
    }, 
    {
        "position_x": 1,
        "position_y": 2,
        "life": 0,
        "direction_x": 0,
        "direction_y": -1
    },
    {
        "position_x": 1,
        "position_y": 2,
        "life": 0,
        "direction_x": 0,
        "direction_y": -1
    }
]

print(check_submarines_life(submarines_list))
