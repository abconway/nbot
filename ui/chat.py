from time import sleep

from ui.press_key import press_key


def chat(dlg, text, channel='y'):
    dlg.set_focus()
    press_key(dlg, channel)
    sleep(0.3)
    dlg.edit2.set_text(text)
    dlg.edit2.type_keys('{ENTER}')
