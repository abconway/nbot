from time import sleep

import pywinauto


def chat(dlg, text, channel='y'):
    dlg.set_focus()
    sleep(0.3)
    pywinauto.keyboard.send_keys(f'{{{channel} down}}' f'{{{channel} up}}')
    sleep(0.3)
    dlg.edit2.set_text(text)
    dlg.edit2.type_keys('{ENTER}')
