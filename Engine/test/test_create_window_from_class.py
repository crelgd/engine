# Текст 1: создания программы через класс

# Импорт модулей движка
from Engine import Window
from Engine import Label

class Main():
    """
    Класс для инициализации и рисования обьектов и окна
    """

    def __init__(self):
        """
        Инициализация окна
        Создание окна и текста
        """
        self.window = Window() # Инициализация окна (все по умолчанию)
        self.label = Label() # Иницилизация текста (все по умолчанию)

    def render(self):
        """
        Рисование обьектов
        """

        self.label.render() # Рисование текста

if __name__ == "__main__":
    main = Main()
    main.window.create() # создание окна
    main.window.winLoop([main.render]) # рисование всего что есть в self.render