from time import sleep

import pywinauto


def press_key(dlg, key, slp=0.3):
    sleep(slp)
    pywinauto.keyboard.send_keys(f'{{{key} down}}' f'{{{key} up}}')