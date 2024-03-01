# Test 1: creating a program through a class

# Import engine modules
from Engine import Window
from Engine import Label

class Main():
    """
    Class for initializing and drawing objects and windows
    """

    def __init__(self):
        """
        Initializing a window
        Creating a window and text
        """
        self.window = Window() # Window initialization (all default)
        self.label = Label() # Initialize text (all default)

    def render(self):
        """
        Drawing objects
        """

        self.label.render() # Drawing text

if __name__ == "__main__":
    main = Main()
    main.window.create() # creating a window
    main.window.winLoop([main.render]) # drawing everything in self.render