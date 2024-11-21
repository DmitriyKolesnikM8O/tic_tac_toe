from .parts import Board

# Задаем основные параметры для игры
CELL_SIZE = 100  # Размер клетки
BOARD_SIZE = 3  # Размер игрового поля
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE  # Ширина и высота окна игры
LINE_WIDTH = 15  # Толщина линий разделения
BG_COLOR = (28, 170, 156)  # Цвет фона игрового поля
LINE_COLOR = (23, 145, 135)  # Цвет линий игрового поля
X_COLOR = (84, 84, 84)  # Цвет крестиков
O_COLOR = (242, 235, 211)  # Цвет ноликов
X_WIDTH = 15  # Толщина линий крестиков
O_WIDTH = 15  # Толщина линий круга
SPACE = CELL_SIZE // 4  # Отступы внутри клетки для рисунков
