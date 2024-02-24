# Отвечает для создания окна
# В других файлах будет продожение этого файла

from pygame import *
import os

# Получить путь к директории, где находится этот скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Изменить текущую рабочую директорию на директорию с файлом
os.chdir(os.path.join(script_dir, 'res'))

class Window:
    # Инициализация данный
    def __init__(self, winTitle='Engine'):
        self.x = 300
        self.y = 200
        self.winTitle = winTitle

        self.FPS = 60
        self.clock = time.Clock()
        self.run = True

        self.win = display.set_mode((self.x, self.y))

        self.background = transform.scale(image.load("bg.png"), (self.x, self.y))

        display.set_icon(image.load('ico.png'))

    # Дает возможноть менять название окна
    def setTitle(self, title):
        display.set_caption(title)

    # Дает возможность изменять фон
    def setBG(self, obj):
        self.background = transform.scale(obj, (self.x, self.y))

    # Изменение размера окна
    def reSize(self, x, y):
        self.x = x
        self.y = y
        self.win = display.set_mode((x, y))
        self.background = transform.scale(self.background, (x, y))

    # Создает окно
    def create(self):
        display.set_caption(self.winTitle)

    # Рисование обьектов
    def winLoop(self, draw_functions=None): 
        while self.run:
            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            self.win.blit(self.background, (0, 0))
            
            if draw_functions: 
                for func in draw_functions:
                    func()  
                
            display.update()
            self.clock.tick(self.FPS)

# Просто тест написаного
if __name__ == '__main__':
    window = Window()
    window.create()
    # Тут код...
    window.setBG(image.load("res/bg.png"))
    window.winLoop()

