from Engine import Window 
from Engine import Label 

window = Window()
window.create()

lab = Label(text='Test')

window.winLoop([lab.render])