# Title: Code to control the window
#
# Description:
# This code contains the Window class to create a window
# It provides basic methods for controlling the window, background and display of objects
#
# Author: crelgd
#
# License:
# MIT License
# 
# Copyright (c) 2024 crelgd
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pygame import *
import os

class Window:
    """
    A class for creating and managing a game window.
    """

    def __init__(self, winTitle='Engine', icon=None, bg=None):
        """
        Initializing the window.

        Options:
        - winTitle (str): Window title.
        """

        self.x = 300
        self.y = 200
        self.winTitle = winTitle

        self.FPS = 60
        self.clock = time.Clock()
        self.run = True

        # Create a window with dimensions self.x, self.y
        self.win = display.set_mode((self.x, self.y))
        display.set_caption(winTitle)

        if bg is None:
            # We get the path to the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Change the current working directory to the directory with the file
            os.chdir(os.path.join(script_dir, 'res'))

            # Load a background image and resize it to fit the window
            self.background = transform.scale(image.load("bg.png"), (self.x, self.y))
        else:
            self.background = transform.scale(image.load(bg), (self.x, self.y))

        if icon is None:
            # We get the path to the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Change the current working directory to the directory with the file
            os.chdir(os.path.join(script_dir, 'res'))

            # Setting the window icon
            display.set_icon(image.load('ico.png'))
        else:
            # Setting the window icon
            display.set_icon(image.load(icon))

    def setTitle(self, title):
        """
        Sets the window title.

        Options:
        - title (str): New window title.
        """

        display.set_caption(title)

    def setBG(self, obj):
        """
        Sets a new window background image.

        Options:
        - obj): New background image.
        """

        self.background = transform.scale(obj, (self.x, self.y))

    def resize(self, x, y):
        """
        Resizes the window.

        Options:
        - x (int): New window width.
        - y (int): New window height.
        """

        self.x = x
        self.y = y
        self.win = display.set_mode((x, y))
        self.background = transform.scale(self.background, (x, y))

    def create(self):
        """Creates a window with the current settings."""

        display.set_caption(self.winTitle)

    def winLoop(self, draw_functions=None):
        """
        The main window update cycle.

        Options:
        - draw_functions: List of functions for rendering additional objects.
        """

        while self.run:
            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            # Rendering a background image
            self.win.blit(self.background, (0, 0))
            
            # Calling rendering functions
            if draw_functions: 
                for func in draw_functions:
                    func()  
                
            display.update()
            self.clock.tick(self.FPS)

# Testing
if __name__ == '__main__':
    window = Window()
    window.create()
    window.setBG(image.load("res/bg.png"))
    window.winLoop()
