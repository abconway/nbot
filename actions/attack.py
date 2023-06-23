import pyautogui as gui
from time import sleep


def press_key(key):
    gui.keyDown(key)
    gui.keyUp(key)


def attack():
    sleep(1)
    press_key('4')
    sleep(0.5)
    press_key('4')
    sleep(0.5)
    press_key('1')
