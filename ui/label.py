# Название: Код для управления текстом
# 
# Описание:
# Этот код содержит класс Label для создания и управления текстом
# Он предоставляет основные методы управления текстом:
# - расположения текстом
# - и отображения текста
# 
# Автор: crelgd <decrelgd@gmail.com>
# 
# Лицензия:
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

# Инициализация pygame
p.init()

class Label(Window):
    """
    Класс для создания и упралением текстом
    """

    def __init__(self, text='Label', size = 16, font_name='Roboto'):
        """
        Инициализация окна.

        Параметры:
        - text (str): Текст который будет отображатся.
        - size (int): Размер текста.
        - font_name (int): Название шрифта.

        * ШРИФТЫ КОТОРЫХ НЕТ В ОС НЕ БУДУТ ОТОБРАЖАТЬСЯ!
        """

        super().__init__()

        self.text = text 
        self.font_name = font_name 
        self.font_size = size
        self.image = ''

        # Инициализация рамположения текста
        self.x = 0
        self.y = 0

        # Инициализация шрифтов
        # Принимает параметры: 
        # - self.font_name: Название шрифта
        # - self.font_size: Размер шрифта
        self.font = p.font.SysFont(self.font_name, self.font_size)

    def render(self):
        """
        Отображение обьетов
        """

        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.win.blit(self.image, (self.x, self.y))

    def changeCoord(self, x, y):
        """
        Изменение расположения обьекта

        Параметры:
        - x (int): Новая ширина окна.
        - y (int): Новая высота окна.
        """

        self.x = x
        self.y = y 

        self.render()
        self.win.blit(self.image, (self.x, self.y))

# Тестирование кода
if __name__ == '__main__':
    window = Window()
    window.create()

    lab = Label(size=20)

    window.winLoop([lab.render])