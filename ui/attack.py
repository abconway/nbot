from time import sleep

import pywinauto


def attack(dlg):
    dlg.set_focus()
    sleep(0.3)
    pywinauto.keyboard.send_keys('{4 down}' '{4 up}')
    sleep(0.3)
    pywinauto.keyboard.send_keys('{1 down}' '{1 up}')
