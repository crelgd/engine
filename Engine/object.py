# Title: Code for creating\modifying an object
#
# Description:
# This code provides an Object class to create and manage.
# It provides basic button management methods:
# - obj location
# - change of location
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
import os

from .window import Window

# We get the path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the directory with the file
os.chdir(os.path.join(script_dir, 'res'))

# Initializing pygame
pygame.init()

class Object(Window):
    """
    Class for creating and managing objects
    """

    def __init__(self, img='obj.png'):
        """
        Initializing the object.

        Options:
        - img (str): obj img.
        """

        super().__init__()

        self.img = img # img

        # Obj size
        self.x = 30
        self.y = 30

        # Obj positions
        self.posX = 10
        self.posY = 10

    def setPos(self, x, y):
        """
        Changing the location of an object

        Options:
        - x (int): New width.
        - y (int): New height.
        """

        self.posX = x
        self.posY = x

    def resize(self, x, y):
        """
        Changes the size of an object

        Options:
        - x (int): New x.
        - y (int): New y.
        """

        self.x = x
        self.y = y

    def render(self):
        """Display of values"""

        self.obj = pygame.transform.scale(pygame.image.load(self.img), (self.x, self.y))
        self.win.blit(self.obj, (self.posX, self.posY))