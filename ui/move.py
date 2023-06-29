from time import sleep

from ui.press_key import press_key


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
# DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
DIRECTIONS = [LEFT, RIGHT]
KEY_W = 'w'
KEY_A = 'a'
KEY_S = 's'
KEY_D = 'd'


def move(dlg, direction):
    if direction == UP:
        key = KEY_W
    elif direction == DOWN:
        key = KEY_S
    elif direction == LEFT:
        key = KEY_A
    elif direction == RIGHT:
        key = KEY_D
    else:
        raise Exception('Invalid direction')
    dlg.set_focus()
    press_key(dlg, key, slp=0.1) 
