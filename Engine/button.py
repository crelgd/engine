# Название: Код для управления кнопками
# 
# Описание:
# Этот код содержит класс Button для создания и управления кнопками
# Он предоставляет основные методы управления кнопками:
# - расположения кнопки
# - при нажатии на кнопку будет происходить указаная функция
# - отображения кнопок
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

import pygame

from .window import Window 
from .label import Label

# Инициализация pygame
pygame.init()

# Дефолтные цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Button(Window):
    """
    Класс для создания и управления кнопками
    """

    def __init__(self, text="Button", color=GRAY):
        """
        Инициализация кнопки.

        Параметры:
        - text (str): Текст, который будет отображаться на кнопке.
        - color (int): Цвет фона кнопки
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
        Отображение обьетов
        """

        # Отрисовка поверхности кнопки
        pygame.draw.rect(self.win, self.color, self.rect)

        # Отрисовка текста кнопки
        self.text_rect = self.text_rendered.get_rect(center=self.rect.center)
        self.win.blit(self.text_rendered, self.text_rect)

       # Проверка события нажатия кнопки только один раз
        if pygame.mouse.get_pressed()[0] and \
            self.rect.collidepoint(pygame.mouse.get_pos()) and not self.pressed:
            self.pressed = True
            if self.callback:
                self.callback()  # Вызов функции обратного вызова при нажатии кнопки
        elif not pygame.mouse.get_pressed()[0]:
            self.pressed = False

    def connectFunction(self, callback=None):
        """
        Подключение функции к кнопке.
        
        Параметры:
        - callback (function): Функция, которая будет вызываться при нажатии кнопки.
        """

        self.callback = callback

    def setColor(self, color):
        """
        Изменение цвета обьекта

        Параметры:
        - color (int): Новый цвет
        """

        self.color = color

    def setCoord(self, x, y):
        """
        Изменение расположения обьекта

        Параметры:
        - x (int): Новая ширина окна.
        - y (int): Новая высота окна.
        """

        self.x = x 
        self.y = y

        self.rect.x = x
        self.rect.y = y

        self.render()

    def padding(self, pad):
        """
        Изменение размера кнопки

        Параметры:
        - pad (int): Не знаю как обьяснить :)
        """

        self.text_rect = self.text.render().get_rect()

        # Обновляем размеры кнопки с учетом отступа
        self.width = self.text_rect.width + 10 * pad 
        self.height = self.text_rect.height + 5 * pad

        # Обновляем размеры и положение прямоугольника кнопки
        self.rect.width = self.width
        self.rect.height = self.height

        # Перерисовываем кнопку с новыми размерами
        self.render()