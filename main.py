from random import choice
from time import sleep

import numpy as np
from PIL import Image

from actions.move import move, DIRECTIONS
from actions.attack import attack
from actions.focus_player import focus_player
from assets.icons import get_icon_arrays
from font.numbers import get_number
from font.words import get_word_arrays
from screen.screenshot import get_screenshot
from screen.find_logout_button import find_logout_button
from screen.get_status import get_status_images
from screen.get_command_word import get_command_word
from screen.get_battle_icon import get_battle_icon


ICON_SWORD, ICON_SWORD_ACTIVE = get_icon_arrays()
WORD_COMMAND = get_word_arrays()[0]


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
    focus_player(1)
    ref_loc = find_logout_button(get_screenshot())
    while True:
        screenshot = get_screenshot()
        battle_image = get_battle_icon(screenshot, ref_loc)
        in_battle = check_in_battle(battle_image)
        print("In battle: {}".format(in_battle))
        command_image = get_command_word(screenshot, ref_loc)
        ready_for_command = check_if_ready_for_command(command_image)
        print("Ready for command: {}".format(ready_for_command))
        status_images = get_status_images(screenshot, ref_loc, in_battle)
        hp1, mp1 = get_status(*status_images[:6])
        print("HP: {}, MP: {}".format(hp1, mp1))
        hp2, mp2 = get_status(*status_images[6:12])
        print("HP: {}, MP: {}".format(hp2, mp2))
        hp3, mp3 = get_status(*status_images[12:])
        print("HP: {}, MP: {}".format(hp3, mp3))
        direction = choice(DIRECTIONS)
        if not in_battle:
            focus_player(1)
            move(direction)
        elif in_battle and ready_for_command:
            focus_player(1)
            attack()
            focus_player(2)
            attack()
            focus_player(3)
            attack()


if __name__ == '__main__':
    main()
