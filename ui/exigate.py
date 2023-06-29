from time import sleep

from ui.press_key import press_key


def exigate(dlg):
    dlg.set_focus()
    press_key(dlg, '4')
