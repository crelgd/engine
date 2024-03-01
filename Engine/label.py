# Title: Code for text manipulation
#
# Description:
# This code contains a Label class for creating and manipulating text
# It provides basic text manipulation methods:
# - text locations
# - and display text
#
# Author: crelgd <decrelgd@gmail.com>
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

from .window import Window
import pygame as p

# Initializing pygame
p.init()

class Label(Window):
    """
    Class for creating and managing text
    """

    def __init__(self, text='Label', size = 16, font_name='Roboto'):
        """
        Initializing the window.

        Options:
        - text (str): The text that will be displayed.
        - size (int): Text size.
        - font_name (int): Font name.

        * FONTS THAT ARE NOT IN THE OS WILL NOT BE DISPLAYED!
        """

        super().__init__()

        self.text = text 
        self.font_name = font_name 
        self.font_size = size
        self.image = ''

        # Initializing text position
        self.x = 0
        self.y = 0

        # Initialize fonts
        # Accepts parameters:
        # - self.font_name: Font name
        # - self.font_size: Font size
        self.font = p.font.SysFont(self.font_name, self.font_size)

    def render(self):
        """Display of values"""

        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.win.blit(self.image, (self.x, self.y))

        return self.font.render(self.text, True, (0, 0, 0))

    def setCoord(self, x, y):
        """
        Changing the location of an object

        Options:
        - x (int): New window width.
        - y (int): New window height.
        """

        self.x = x
        self.y = y 

        self.render()
        self.win.blit(self.image, (self.x, self.y))

# Code testing
if __name__ == '__main__':
    window = Window()
    window.create()

    lab = Label(size=20)

    window.winLoop([lab.render])