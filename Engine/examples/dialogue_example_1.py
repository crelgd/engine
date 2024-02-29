import sys
from Engine import Window
from Engine import Label
from Engine import Button

def exit():
    sys.exit()

windowX = 500
windowY = 350

window = Window(winTitle="Youre ok?")
window.create()

label = Label(text="Вы согласны?", size=26)
label.setCoord(x=(windowX - 100) // 2, y=100)

ok = Button(text="Ok")
cancel = Button(text="Cancel")

ok.setCoord(x=(windowX - 300) // 2, y=250)
ok.padding(8)

cancel.setCoord(x=(windowX + 300) // 2, y=250)
cancel.padding(8)

ok.connectFunction(exit)
cancel.connectFunction(exit)

def rendering():
    label.render()

    ok.render()
    cancel.render()

window.resize(windowX, windowY)
window.winLoop([rendering])