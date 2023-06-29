from ui.press_key import press_key


def attack(dlg):
    dlg.set_focus()
    press_key(dlg, '3')
    press_key(dlg, '1')
