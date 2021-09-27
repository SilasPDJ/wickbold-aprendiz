import pyautogui as pygui
from keyboard import is_pressed

def press_key_b4(key: str):
    """
    Só dá break quando uma tecla específica é pressionada, e então, continua o código
    :param key:
    :return:
    """

    while True:
        #
        if is_pressed(key):
            if is_pressed(key):
                return True
        else:
            ...


with open("pos.txt") as f:
    fr = f.read()
    fr = fr.split(",")
    fr = [float(s) for s in fr]
    

while True:
    press_key_b4("ç")
    pygui.click(*fr)
    
