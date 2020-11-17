import microbit
import random

# definition of functions
def initialize_submarines(nb_submarines, submarine_life):
    """Initialize the data structure for the game

    Parameters
    ----------
    nb_submarines: Amount of submarines to create (int)
    submarine_life: Life to give to the submarines (int)

    Returns
    -------
    submarines_list: list of dictionaries (list)
    """

    submarines_list = []
    for i in range(nb_submarines):
        submarine = {
            'position_x': random.randint(0, 4),
            'position_y': random.randint(0, 4),
            'life': submarine_life,
            'direction_x': 0,
            'direction_y': 0
        }
        submarine['direction_x'], submarine['direction_y'] = define_new_direction()
        submarines_list.append(submarine)
    return submarines_list

def update_direction(submarines_list):
    """Update the directions of each submarines with a 10% chance

    Parameters
    ----------
    submarines_list: List of all submarines (list)
    
    """
    for submarine in submarines_list:
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            submarine['direction_x'], submarine['direction_y'] = define_new_direction()

def define_new_direction():
    """Returns a random direction

    Returns
    -------
    new_direction_x: New direction on the x axis (int)
    new_direction_y: New direction on the y axis (int)
    
    """
    random_direction = random.randint(0, 4)
    if random_direction == 0:
        return 0, 0
    elif random_direction == 1:
        return 0, -1
    elif random_direction == 2:
        return 0, 1
    elif random_direction == 3:
        return 1, 0
    else:
        return -1, 0

def update_position(submarines_list):
    """Update the direction and current position of submarines

    Parameters
    ----------
    submarines_list: The list of the submarines (list)
    
    """

    for submarine in submarines_list:
        if submarine['position_x'] + submarine['direction_x'] > 4 or submarine['position_x'] + submarine['direction_x'] < 0:
            submarine['direction_x'], submarine['direction_y'] = define_new_direction()
        elif submarine['position_y'] + submarine['direction_y'] > 4 or submarine['position_y'] + submarine['direction_y'] < 0:
            submarine['direction_x'], submarine['direction_y'] = define_new_direction()
        else:
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

    submarines_alive = False
    submarines_index = 0

    while not submarines_alive and submarines_index < len(submarines_list):
        if submarines_list[submarines_index]['life'] != 0:
            submarines_alive = True
        submarines_index += 1

    return submarines_alive


def update_target(target_x, target_y):
    """Updates the current target of the player using the accelerometer of the microbit

    Parameters
    ----------
    target_x: Current target on the x axis (int)
    target_y: Current target on the y axis (int)

    Returns
    -------
    updated_target_x: New target on the x axis (int)
    updated_target_y: New target on the y axis (int)

    Notes
    -----
    After multiple testing we decided to use 600 [1/1000 G] has the limit for the trigger of this functions
    We found that it was a good balance between maniability and the avoidance of unwanted movement
    
    """

    accel_x = microbit.accelerometer.get_x()
    accel_y = microbit.accelerometer.get_y()

    if accel_x > 600 and target_x < 4:
        target_x += 1
    elif accel_x < -600 and target_x > 0:
        target_x -= 1
    elif accel_y > 600 and target_y < 4:
        target_y += 1
    elif accel_y < -600 and target_y > 0:
        target_y -= 1

    microbit.display.clear()
    microbit.display.set_pixel(target_x, target_y, 9)

    return target_x, target_y

def fire(target_x, target_y, submarines_list):
    """Checks if a submarine exist on the coordinates of the target and removes a life if it was

    Parameters
    ----------
    target_x: Current target on the x axis (int)
    target_y: Current target on the y axis (int)
    submarines_list: List of all submarines (list)
    
    """
    found_submarine = False
    for submarine in submarines_list:
        if submarine['position_x'] == target_x and submarine['position_y'] == target_y:
            submarine['life'] -= 1
            microbit.display.set_pixel(target_x, target_y, 8)
            found_submarine = True
    
    if not found_submarine:
        microbit.display.set_pixel(target_x, target_y, 3)

def sonar(submarines_list):
    """Turn on a pixel of the screen on the position of each submarines

    Parameters
    ----------
    submarines_list: List of all submarines (list)
    
    """
    microbit.display.clear()

    for submarine in submarines_list:
        if submarine['life'] != 0:
            microbit.display.set_pixel(submarine['position_x'], submarine['position_y'], 9)
            



# settings
target_x = 2
target_y = 2
nb_submarines = 4
submarine_life = 2

# create board and place submarines
submarines_list = initialize_submarines(nb_submarines, submarine_life)

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
    game_is_over = not check_submarines_life(submarines_list)
    
    if not game_is_over:
	    # update position of submarines
	    update_position(submarines_list)
	    
	    # update direction of submarines
	    update_direction(submarines_list)

# tell that the game is over
microbit.display.scroll("Game over, you win", delay=100)