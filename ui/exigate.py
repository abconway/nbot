from time import sleep

import pywinauto


def exigate(dlg):
    dlg.set_focus()
    sleep(0.3)
    pywinauto.keyboard.send_keys('{4 down}' '{4 up}')
