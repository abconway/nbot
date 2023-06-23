import pyautogui as gui


SCREEN_WIDTH, SCREEN_HEIGHT = gui.size()


def focus_player(player_num):
    if player_num == 1:
        gui.click(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.25)
    elif player_num == 2:
        gui.click(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.75)
    elif player_num == 3:
        gui.click(SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75)
