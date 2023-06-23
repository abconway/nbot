from random import choice
from time import sleep

import numpy as np
from PIL import Image
import pyautogui as gui

from assets.icons import get_icon_arrays
from font.numbers import get_number_arrays
from font.words import get_word_arrays
from screen.screenshot import get_screenshot
from screen.find_logout_button import find_logout_button
from screen.get_status import get_status_images
from screen.get_command_word import get_command_word
from screen.get_battle_icon import get_battle_icon


NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9 = get_number_arrays()
ICON_SWORD, ICON_SWORD_ACTIVE = get_icon_arrays()
WORD_COMMAND = get_word_arrays()[0]

SCREEN_WIDTH, SCREEN_HEIGHT = gui.size()
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
# DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
DIRECTIONS = [LEFT, RIGHT]


def gui_focus_player(player_num):
    if player_num == 1:
        gui.click(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.25)
    elif player_num == 2:
        gui.click(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.75)
    elif player_num == 3:
        gui.click(SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75)


def gui_move(direction):
    if direction == 'up':
        gui.keyDown('w')
        gui.keyUp('w')
    elif direction == 'down':
        gui.keyDown('s')
        gui.keyUp('s')
    elif direction == 'left':
        gui.keyDown('a')
        gui.keyUp('a')
    elif direction == 'right':
        gui.keyDown('d')
        gui.keyUp('d')


def gui_attack():
    sleep(1)
    gui.keyDown('4')
    gui.keyUp('4')
    sleep(1)
    gui.keyDown('4')
    gui.keyUp('4')
    sleep(0.5)
    gui.keyDown('4')
    gui.keyUp('4')


def gui_vitality():
    sleep(1)
    gui.keyDown('3')
    gui.keyUp('3')
    sleep(3)
    print("Vitality safety margin over.")


def check_in_battle(image: Image.Image) -> bool:
    im_array = np.asarray(image)
    if np.array_equal(im_array, ICON_SWORD) or np.array_equal(im_array, ICON_SWORD_ACTIVE):
        return True
    return False


def check_if_ready_for_command(image: Image) -> bool:
    im_array = np.asarray(image)
    if np.array_equal(im_array, WORD_COMMAND):
        return True
    return False


def get_number(im: Image):
    num_array = np.asarray(im)
    if np.array_equal(num_array, NUM_0):
        return 0
    elif np.array_equal(num_array, NUM_1):
        return 1
    elif np.array_equal(num_array, NUM_2):
        return 2
    elif np.array_equal(num_array, NUM_3):
        return 3
    elif np.array_equal(num_array, NUM_4):
        return 4
    elif np.array_equal(num_array, NUM_5):
        return 5
    elif np.array_equal(num_array, NUM_6):
        return 6
    elif np.array_equal(num_array, NUM_7):
        return 7
    elif np.array_equal(num_array, NUM_8):
        return 8
    elif np.array_equal(num_array, NUM_9):
        return 9
    else:
        return 0


def get_status(hp1, hp2, hp3, mp1, mp2, mp3):
    hp1 = get_number(hp1)
    hp2 = get_number(hp2)
    hp3 = get_number(hp3)
    hp = (hp1 * 100) + (hp2 * 10) + hp3
    mp1 = get_number(mp1)
    mp2 = get_number(mp2)
    mp3 = get_number(mp3)
    mp = (mp1 * 100) + (mp2 * 10) + mp3
    return (hp, mp)


def main():
    p1_vitality_cast = False
    p2_vitality_cast = False
    p3_vitality_cast = False
    gui_focus_player(1)
    ref_loc = find_logout_button(get_screenshot())
    while True:
        screenshot = get_screenshot()
        battle_image = get_battle_icon(screenshot, ref_loc)
        in_battle = check_in_battle(battle_image)
        print("In battle: {}".format(in_battle))
        # command_image = get_command_word(screenshot, resolution='957x487')
        # ready_for_command = check_if_ready_for_command(command_image)
        # print("Ready for command: {}".format(ready_for_command))
        status_images = get_status_images(screenshot, ref_loc, in_battle)
        hp1, mp1 = get_status(*status_images[:6])
        print("HP: {}, MP: {}".format(hp1, mp1))
        hp2, mp2 = get_status(*status_images[6:12])
        print("HP: {}, MP: {}".format(hp2, mp2))
        hp3, mp3 = get_status(*status_images[12:])
        print("HP: {}, MP: {}".format(hp3, mp3))
        # direction = choice(DIRECTIONS)
        # if not in_battle:
        #     if hp1 < 183 and p1_vitality_cast is False:
        #         gui_focus_player(1)
        #         gui_vitality()
        #         p1_vitality_cast = True
        #     elif hp2 < 183 and p2_vitality_cast is False:
        #         gui_focus_player(2)
        #         gui_vitality()
        #         p2_vitality_cast = True
        #     elif hp3 < 183 and p3_vitality_cast is False:
        #         gui_focus_player(3)
        #         gui_vitality()
        #         p3_vitality_cast = True
        #     gui_focus_player(1)
        #     gui_move(direction)
        # elif in_battle and ready_for_command:
        #     p1_vitality_cast = False
        #     p2_vitality_cast = False
        #     p3_vitality_cast = False
        #     gui_focus_player(1)
        #     gui_attack()
        #     gui_focus_player(2)
        #     gui_attack()
        #     gui_focus_player(3)
        #     gui_attack()


if __name__ == '__main__':
    main()
