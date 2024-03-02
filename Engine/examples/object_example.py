# Import engine modules
from Engine import Window
from Engine import Object

class Main():
    """
    Class for initializing and drawing objects and windows
    """

    def __init__(self):
        """
        Initializing a window
        Creating a window and object
        """

        self.window = Window()
        self.obj = Object()

    def setting(self):
        """
        Setting up objects
        """

        self.obj.resize(x=50, y=50)
        self.obj.setPos(x=100, y=50)

    def render(self):
        """
        Drawing objects
        """
        
        self.obj.render()

if __name__ == '__main__':
    main = Main()
    main.window.create()

    main.setting()

    main.window.winLoop([main.render])