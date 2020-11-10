def initialize_submarines(nb_submarines):
    """Initialize the data structure for the game

    Parameters
    ----------
    nb_submarines: Amount of submarines to create (int)

    Returns
    -------
    submarines_list: list of dictionaries (list)
    """

def update_position(submarines_list):
    """Update the direction and current position of submarines

    Parameters
    ----------
    submarines_list: The list of the submarines (list)

    Returns
    -------
    updated_submarines_list: The updated list of submarines (list)
    
    """

def check_submarines_life(submarines_list):
    """Checks if all submarines's life are different of 0

    Parameters
    ----------
    submarines_list: The list of submarines (list)

    Returns
    -------
    submarines_alive: Wether the submarines are alive (bool)
    
    """

def update_target(target_x, target_y):
    """Updates the current target of the player using the accelorometer of the microbit

    Parameters
    ----------
    target_x: Current target on the x axis (int)
    target_y: Current target on the y axis (int)

    Returns
    -------
    updated_target_x: New target on the x axis (int)
    updated_target_y: New target on the y axis (int)
    
    """

def fire(target_x, target_y, submarines_list):
    """
    
    """

def sonar(submarines_list):
    """
    
    """



submarines_list = [
    {
        'position_x': 1,
        'position_y': 1,
        'life': 2,
        'direction_x': -1,
        'direction_y': 0
    },
    {
        'position_x': 4,
        'position_y': 3,
        'life': 1,
        'direction_x': 0,
        'direction_y': 1
    }
]