from time import sleep

import pywinauto


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


pywinauto.keyboard.send_keys('{a down}' '{a up}')


def move(dlg, direction):
    dlg.set_focus()
    sleep(0.1)
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
    pywinauto.keyboard.send_keys(f'{{{key} down}}' f'{{{key} up}}')
