from time import sleep

from ui.press_key import press_key


def vitality(dlg):
    dlg.set_focus()
    press_key(dlg, '3')
    sleep(4)
