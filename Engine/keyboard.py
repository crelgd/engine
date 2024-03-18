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
#
# This code contains methods to handle keyboard events
# It provides basic methods for reading events:
# - button events
# - ?mouse button events
# Coming soon...
# I'll probably add the cursor position and mouse button events
#
# Author: crelgd

import keyboard as k # import keyboard lib

def ifClicked(button="q"):
    """
    check function 'is the button pressed?' 
    if so, then the action is performed...

    Options:
    - button (str): the button that will be tracked
    """

    buttonPress = k.is_pressed(button)
    
    clicked = False  # a variable that will determine 'is the button pressed?'
    if (buttonPress):   # if buttpn is pressed returns "True"
        clicked = True
        return clicked
    else:
        clicked = False # if button not pressed returns "False"
        return clicked

    # I don't know why I wrote this :/
