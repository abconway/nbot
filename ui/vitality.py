from time import sleep

import pywinauto


def vitality(dlg):
    dlg.set_focus()
    sleep(0.3)
    pywinauto.keyboard.send_keys('{3 down}' '{3 up}')
    sleep(4)
