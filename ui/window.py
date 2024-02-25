# Название: Код для управления окном 
# 
# Описание:
# Этот код содержит класс Window для создания окна 
# Он предоставляет основные методы для управления окном, фоном и отображением обьектов
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

from pygame import *
import os

# Получаем путь к директории, где находится этот скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Изменяем текущую рабочую директорию на директорию с файлом
os.chdir(os.path.join(script_dir, 'res'))

class Window:
    """
    Класс для создания и управления игровым окном.
    """

    def __init__(self, winTitle='Engine'):
        """
        Инициализация окна.

        Параметры:
        - winTitle (str): Название окна.
        """

        self.x = 300
        self.y = 200
        self.winTitle = winTitle

        self.FPS = 60
        self.clock = time.Clock()
        self.run = True

        # Создаем окно с размерами self.x, self.y
        self.win = display.set_mode((self.x, self.y))

        # Загружаем фоновое изображение и изменяем его размеры под размеры окна
        self.background = transform.scale(image.load("bg.png"), (self.x, self.y))

        # Устанавливаем иконку окна
        display.set_icon(image.load('ico.png'))

    def setTitle(self, title):
        """
        Устанавливает заголовок окна.

        Параметры:
        - title (str): Новый заголовок окна.
        """

        display.set_caption(title)

    def setBG(self, obj):
        """
        Устанавливает новое фоновое изображение окна.

        Параметры:
        - obj): Новое фоновое изображение.
        """

        self.background = transform.scale(obj, (self.x, self.y))

    def resize(self, x, y):
        """
        Изменяет размеры окна.

        Параметры:
        - x (int): Новая ширина окна.
        - y (int): Новая высота окна.
        """

        self.x = x
        self.y = y
        self.win = display.set_mode((x, y))
        self.background = transform.scale(self.background, (x, y))

    def create(self):
        """Создает окно с текущими настройками."""

        display.set_caption(self.winTitle)

    def winLoop(self, draw_functions=None):
        """
        Основной цикл обновления окна.

        Параметры:
        - draw_functions: Список функций для отрисовки дополнительных объектов.
        """

        while self.run:
            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            # Отрисовка фонового изображения
            self.win.blit(self.background, (0, 0))
            
            # Вызов функций отрисовки
            if draw_functions: 
                for func in draw_functions:
                    func()  
                
            display.update()
            self.clock.tick(self.FPS)

# Тестирование
if __name__ == '__main__':
    window = Window()
    window.create()
    # Тут код...
    window.setBG(image.load("res/bg.png"))
    window.winLoop()
