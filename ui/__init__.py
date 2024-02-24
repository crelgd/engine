# Инициализация всех файлов

from .window import Window 
from .label import Label

# При импорте всех файлов будут импортироваться эти функции:
__all__ = [
    'Window', 'Label'
]

# Версия пакета
__version__ = '1.0.0'

# Проверка зависимостей
try:
    import pygame
except ImportError:
    raise ImportError("Pygame library is required to use this package.")
