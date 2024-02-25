from Engine import Window
from Engine import Label
from Engine import Button

window = Window()
window.create()

label = Label(text='Not clicked!', size=26)
label.setCoord(x=100, y=100)

def ifClicked():
    label.text = 'Clicked!'

button = Button(text='Click me!')

button.padding(5)

button.setCoord(x=100, y=40)
button.connectFunction(ifClicked)

def rendering():
    label.render()
    button.render()

window.winLoop([rendering])