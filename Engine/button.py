# Title: Code for controlling buttons
#
# Description:
# This code contains the Button class for creating and managing buttons
# It provides basic button management methods:
# - button location
# - when you press the button, the specified function will occur
# - display buttons
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

import pygame

from .window import Window 
from .label import Label

# Initializing pygame
pygame.init()

# Default colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Button(Window):
    """
    Class for creating and managing buttons
    """

    def __init__(self, text="Button", color=GRAY):
        """
        Initializing the button.

        Options:
        - text (str): The text that will be displayed on the button.
        - color (int): Button background color
        """

        super().__init__()

        self.text = Label(text=text)
        self.text_rendered = self.text.render()
        self.text_rect = self.text.render().get_rect()

        self.x = 0
        self.y = 0
        self.width = self.text_rect.width + 10
        self.height = self.text_rect.height + 5
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self):
        """
        Display of values
        """

        # Rendering the Button Surface
        pygame.draw.rect(self.win, self.color, self.rect)

        # Rendering button text
        self.text_rect = self.text_rendered.get_rect(center=self.rect.center)
        self.win.blit(self.text_rendered, self.text_rect)

       # Checking the button click event only once
        if pygame.mouse.get_pressed()[0] and \
            self.rect.collidepoint(pygame.mouse.get_pos()) and not self.pressed:
            self.pressed = True
            if self.callback:
                self.callback()  # Calling a callback function when a button is clicked
        elif not pygame.mouse.get_pressed()[0]:
            self.pressed = False

    def connectFunction(self, callback=None):
        """
        Connecting a function to a button.
        
        Options:
        - callback (function): The function that will be called when the button is pressed.
        """

        self.callback = callback

    def setColor(self, color):
        """
        Changing the color of an object

        Options:
        - color (int): New color
        """

        self.color = color

    def setPos(self, x, y):
        """
        Changing the location of an object

        Options:
        - x (int): New window width.
        - y (int): New window height.
        """

        self.x = x 
        self.y = y

        self.rect.x = x
        self.rect.y = y

        self.render()

    def padding(self, pad):
        """
        Changing the size of a button

        Options:
        - pad (int): I dont know how to explain :)
        """

        self.text_rect = self.text.render().get_rect()

        # Updating the size of the button taking into account the indentation
        self.width = self.text_rect.width + 10 * pad 
        self.height = self.text_rect.height + 5 * pad

        # Update the size and position of the button rectangle
        self.rect.width = self.width
        self.rect.height = self.height

        # Redrawing the button with new sizes
        self.render()