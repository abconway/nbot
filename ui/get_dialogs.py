import pywinauto
from pywinauto.application import Application


def get_dialogs():
    windows = pywinauto.findwindows.find_elements(title_re=".*NEStalgia | The Time Lords.*")
    dlgs = {}
    handles = []

    for window in windows:
        handle = window.handle
        app = Application(backend='uia')
        app.connect(handle=handle)
        dlg = app.window(handle=handle)
        dlgs[handle] = dlg
        handles.append(handle)

    return (dlgs, handles)
