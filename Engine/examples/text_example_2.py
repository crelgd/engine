from Engine import Window
from Engine import Label 

window = Window()
window.create()

label = Label(text='Example Text', size=25)
label.setPos(x=100, y=100)

window.winLoop([label.render])