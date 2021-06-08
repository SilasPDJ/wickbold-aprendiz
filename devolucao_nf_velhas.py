import pyautogui as pygui
from time import sleep
a = pygui.getWindowsWithTitle("Devolução Cliente")[0]
a.activate()
sleep(2)
pygui.write("c00".upper())
pygui.hotkey("tab")
pygui.write("comercial".upper())
pygui.hotkey("f8")
# ativa cmd
# pygui.getWindowsWithTitle("C:\Windows\System32\cmd.exe")[0].activate()
pygui.getWindowsWithTitle("devolucao")[0].activate()
pygui.hotkey("up")
a.activate()


