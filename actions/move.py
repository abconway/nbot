import pyautogui as gui


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


def move(direction):
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
    gui.keyDown(key)
    gui.keyUp(key)
