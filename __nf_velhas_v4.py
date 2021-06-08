# ficar coisando até coisar
import nova_forma
import pyautogui as pygui
from time import sleep
from __pressb4 import press_key_b4 as pressb4

def write_after_cod():
    while True:
        try:
            a = pygui.getWindowsWithTitle("Devolução Cliente")[0]
            a.activate()
            break
        except IndexError:
            sleep(2)
            
    # sleep(2)
    pygui.write("c00".upper())
    pygui.hotkey("tab")
    pygui.write("comercial".upper())
    pygui.hotkey("f8")
    # ativa cmd
    # pygui.getWindowsWithTitle("C:\Windows\System32\cmd.exe")[0].activate()
    pygui.getWindowsWithTitle("devolucao")[0].activate()
    pygui.hotkey("up")
    a.activate()

for val in nova_forma.dale():
    while True:
        try:
            a = pygui.getWindowsWithTitle("Desenvolvimento Devolução - XML")[0]
            a.activate()
            break
        except IndexError:
            sleep(2)
            pygui.hotkey("f3")
    sleep(1)
    pygui.hotkey('tab')
    pygui.write(val)
    pygui.hotkey('f8')
    write_after_cod()

