import pyautogui as pygui
from time import sleep
a = pygui.getWindowsWithTitle("Devolução Cliente")[0]
a.activate()
sleep(2)
pygui.write("c01".upper())

pygui.hotkey("tab")
pygui.write("comercial".upper())

# input('ESSE TAB TA ERRADO POIS VARIA DE ACORDO COM A QUANTIDADE')
# [pygui.hotkey('tab') for i in range(5)]

# pygui.hotkey('tab', 'enter', interval=1)
pygui.keyDown("shift")
[pygui.hotkey('tab') for i in range(16)]
pygui.keyUp("shift")

pygui.write("PA")
sleep(.5)
pygui.hotkey('tab', 'enter', interval=1)

# input('teste')

pygui.hotkey("f8")


pygui.getWindowsWithTitle("devolucao")[0].activate()
pygui.hotkey("up")
a.activate()
