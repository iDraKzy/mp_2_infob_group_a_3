import microbit
from random import randint


def initialize_submarines(nb_submarines, submarines_life):
    """Initialize the data structure for the game

    Parameters
    ----------
    nb_submarines: Amount of submarines to create (int)
    submarines_life: Life to give to the submarines (int)

    Returns
    -------
    submarines_list: list of dictionaries (list)
    """

def update_position(submarines_list):
    """Update the direction and current position of submarines

    Parameters
    ----------
    submarines_list: The list of the submarines (list)
    
    """

    for submarine in submarines_list:
        if randint(1, 10) == 1:
            random_direction = randint(0, 4)
            if random_direction == 0:
                submarine['direction_x'] = 0
                submarine['direction_y'] = 0
            elif random_direction == 1:
                submarine['direction_x'] = 0
                submarine['direction_y'] = -1
            elif random_direction == 2:
                submarine['direction_x'] = 0
                submarine['direction_y'] = 1
            elif random_direction == 3:
                submarine['direction_x'] = 1
                submarine['direction_y'] = 0
            else:
                submarine['direction_x'] = -1
                submarine['direction_y'] = 0
        
        submarine['position_x'] = submarine['position_x'] + submarine['direction_x']
        submarine['position_y'] = submarine['position_y'] + submarine['direction_y']

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

def fire(order, target_x, target_y, submarines_list):
    """Checks if a submarine exist on the coordinates of the target and removes a life if it was

    Parameters
    ----------
    target_x: Current target on the x axis (int)
    target_y: Current target on the y axis (int)
    submarines_list: List of all submarines (list)

    Returns
    -------
    updated_submarines_list: Updated list of all submarines (list)
    
    """

def sonar(submarines_list):
    """Turn on a pixel of the screen on the position of each submarines

    Parameters
    ----------
    submarines_list: List of all submarines (list)
    
    """




# settings
target_x = 2
target_y = 2
nb_submarines = 4
submarine_life = 2

# create board and place submarines
submarines_list = initialize_submarines(nb_submarines)
# submarines_list = [
#     {
#         'position_x': 1,
#         'position_y': 1,
#         'life': 2,
#         'direction_x': -1,
#         'direction_y': 0
#     },
#     {
#         'position_x': 4,
#         'position_y': 3,
#         'life': 1,
#         'direction_x': 0,
#         'direction_y': 1
#     }
# ]

# show where target is right now
microbit.display.set_pixel(target_x, target_y, 9)
    
# loop until game is over
game_is_over = False
while not game_is_over:
    # loop until an action is chosen (fire or sonar)
    order = ''
    while order == '':
        # check if a button is pressed, the micro:bit is moved, etc.
        if microbit.button_a.is_pressed():
            order = 'fire'
        elif microbit.button_b.is_pressed():
            order = 'sonar'
        else:
            target_x, target_y = update_target(target_x, target_y)
         
        # wait a few milliseconds before checking again
        microbit.sleep(500)
   
    # execute order (fire or sonar)
    if order == 'fire':
        fire(target_x, target_y, submarines_list)
    elif order == 'sonar':
        sonar(submarines_list)
    
    # wait a few seconds and clear screen
    microbit.sleep(2500)
    microbit.display.clear()
    
    # check if game is not over
    game_is_over = not check_submarines_life(submarines_list) #To Modify
    
    if not game_is_over:
	    # update position of submarines
	    pass
	    
	    # update direction of submarines
	    pass

# tell that the game is over
microbit.display.scroll("Game over, you win", delay=100)