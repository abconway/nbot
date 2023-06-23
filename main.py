from random import choice
from time import sleep

import numpy as np
from PIL import Image
import pywinauto


from assets.icons import get_icon_arrays
from font.numbers import get_number
from font.words import get_word_arrays
from screen.screenshot import get_screenshot
from screen.find_logout_button import find_logout_button
from screen.get_status import get_status_images
from screen.get_command_word import get_command_word
from screen.get_battle_icon import get_battle_icon
from screen.get_party_icon import get_party_icon
from ui.attack import attack
from ui.chat import chat
from ui.get_dialogs import get_dialogs
from ui.move import move, UP, DOWN, LEFT, RIGHT


ICON_SWORD, ICON_SWORD_ACTIVE, ICON_PARTY = get_icon_arrays()
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


def check_if_party_leader(image: Image) -> bool:
    im_array = np.asarray(image)
    if np.array_equal(im_array, ICON_PARTY):
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
    dialogs, handles = get_dialogs()
    ref_locs = {}
    for handle in handles:
        ref_locs[handle] = find_logout_button(get_screenshot(handle))
    leader_handle = None
    for handle in handles:
        screenshot = get_screenshot(handle)
        party_icon = get_party_icon(screenshot, ref_locs[handle])
        if check_if_party_leader(party_icon):
            leader_handle = handle
            break
    leader_dlg = dialogs[leader_handle]
    chat(leader_dlg, 'I am the party leader!', channel='h')
    move_left = True
    while True:
        screenshot = get_screenshot(leader_handle)
        battle_image = get_battle_icon(screenshot, ref_locs[leader_handle])
        in_battle = check_in_battle(battle_image)
        print("In battle: {}".format(in_battle))
        command_image = get_command_word(screenshot, ref_locs[leader_handle])
        ready_for_command = check_if_ready_for_command(command_image)
        print("Ready for command: {}".format(ready_for_command))
        status_images = get_status_images(screenshot, ref_locs[leader_handle], in_battle)
        hp1, mp1 = get_status(*status_images[:6])
        print("HP: {}, MP: {}".format(hp1, mp1))
        hp2, mp2 = get_status(*status_images[6:12])
        print("HP: {}, MP: {}".format(hp2, mp2))
        hp3, mp3 = get_status(*status_images[12:])
        print("HP: {}, MP: {}".format(hp3, mp3))
        # direction = choice(DIRECTIONS)
        if not in_battle:
            leader_dlg.set_focus()
            sleep(0.1)
            if move_left:
                move(leader_dlg, LEFT)
                move_left = False
            else:
                move(leader_dlg, RIGHT)
                move_left = True
        elif in_battle and ready_for_command:
            for handle in handles:
                dlg = dialogs[handle]
                attack(dlg)


if __name__ == '__main__':
    main()
