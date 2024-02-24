# Манипуляция текстом

from .window import Window 
import pygame as p

p.init()

# Класс со всемі методами/функциями для текста
class Label(Window):
    # Инициализация данный
    def __init__(self, text='Label', size = 16, font_name='Roboto'):
        super().__init__()

        self.text = text 
        self.font_name = font_name 
        self.font_size = size
        self.image = ''

        self.x = 0
        self.y = 0

        self.font = p.font.SysFont(self.font_name, self.font_size)

    # Показывание обьекта
    def render(self):
        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.win.blit(self.image, (self.x, self.y))

    # Изменение координат обьекта
    def changeCoord(self, x, y):
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