import pygame
from pygame.draw import *

# === Инициализация === #
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

# === Константы === #
WHITE = (255, 255, 255)
HARE_COLOR = (200, 200, 200)    # Цвет зайца
EYE_COLOR = (0, 0, 0)           # Цвет глаз
NOSE_COLOR = (255, 0, 0)        # Цвет носа

# === Конфигурация зайца === #
HARE_CONFIG = {
    "width": 200,
    "height": 400,
    "body_height_ratio": 2 / 5,
    "head_size_ratio": 1 / 3,
    "ear_height_ratio": 1 / 1.5,
    "ear_width_ratio": 1 / 8,
    "leg_height_ratio": 1 / 12,
    "eye_size_ratio": 1 / 10,
}

# === Функции === #

def draw_hare(surface, x, y, config, color):
    """
    Рисует изменённого зайца на экране без использования эллипсов.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    
    width = config["width"]
    height = config["height"]
    
    body_height = height * config["body_height_ratio"]
    body_width = width / 2
    head_size = height * config["head_size_ratio"]
    ear_height = head_size * config["ear_height_ratio"]
    ear_width = width * config["ear_width_ratio"]
    leg_height = height * config["leg_height_ratio"]
    eye_size = head_size * config["eye_size_ratio"]

    # Рисуем тело
    draw_body(surface, x, y + body_height / 3, body_width, body_height, color)

    # Рисуем голову
    draw_head(surface, x, y - head_size / 2 + 15, head_size, color)

    # Рисуем уши
    ear_y = y - height / 2 + ear_height
    draw_ear(surface, x - ear_width / 2 - 15, ear_y, ear_width, ear_height, color)
    draw_ear(surface, x + ear_width / 2 + 15, ear_y, ear_width, ear_height, color)

    # Рисуем ноги
    leg_y = y + body_height / 2 - leg_height / 2
    draw_leg(surface, x - body_width / 4, leg_y, body_width / 4, leg_height, color)
    draw_leg(surface, x + body_width / 4, leg_y, body_width / 4, leg_height, color)

    # Добавим глаза и нос
    draw_eyes(surface, x, y - head_size / 2 + head_size / 4, eye_size)
    draw_nose(surface, x, y - head_size / 2 + head_size / 2, eye_size / 2)


def draw_body(surface, x, y, width, height, color):
    """Рисует тело зайца в виде многоугольника"""
    points = [
        (x - width / 2, y + height / 5),
        (x + width / 2, y + height / 5),
        (x + width / 4, y - height / 2 + 40),
        (x - width / 4, y - height / 2 + 40),
    ]
    polygon(surface, color, points)

def draw_head(surface, x, y, size, color):
    """Рисует голову зайца"""
    points = [
        (x - size / 2, y + size / 2),
        (x + size / 2, y + size / 2),
        (x + size / 2, y - size / 2),
        (x - size / 2, y - size / 2)
    ]
    polygon(surface, color, points)

def draw_ear(surface, x, y, width, height, color):
    """Рисует ухо зайца"""
    points = [(x, y - height), (x - width / 2, y), (x + width / 2, y)]
    polygon(surface, color, points)

def draw_leg(surface, x, y, width, height, color):
    """Рисует ногу зайца"""
    points = [
        (x - width / 2, y),
        (x + width / 2, y),
        (x + width / 2, y + height),
        (x - width / 2, y + height)
    ]
    polygon(surface, color, points)

def draw_eyes(surface, x, y, size):
    """Рисует глаза зайца"""
    circle(surface, EYE_COLOR, (int(x - size - 5), int(y)), int(size))
    circle(surface, EYE_COLOR, (int(x + size + 5), int(y)), int(size))

def draw_nose(surface, x, y, size):
    """Рисует нос зайца"""
    circle(surface, NOSE_COLOR, (int(x), int(y)), int(size))


# === Основной цикл === #
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Рисуем зайца
    draw_hare(screen, 200, 200, HARE_CONFIG, HARE_COLOR)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
