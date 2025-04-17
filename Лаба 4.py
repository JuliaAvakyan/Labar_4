import pygame
from pygame.draw import *

# Инициализация Pygame
pygame.init()

# Установка параметров
FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_hare(surface, x, y, width, height, color):
    body_height = height * 2 / 3
    body_width = width / 2

    # Рисуем тело
    draw_body(surface, x, y + body_height / 3, body_width, body_height, color)

    # Рисуем голову
    head_size = height / 4
    head_y = y - head_size / 2
    draw_head(surface, x, head_y, head_size, color)

    # Рисуем уши
    ear_height = height / 2
    ear_width = width / 6
    ear_y = y - height / 2 + ear_height
    
    # Левое ухо (внешнее)
    draw_ear(surface, x - ear_width, ear_y, ear_width, ear_height, color)
    
    # Правое ухо (внешнее)
    draw_ear(surface, x + ear_width, ear_y, ear_width, ear_height, color)

    # Рисуем глаза (белые с черными зрачками)
    eye_size = head_size / 6
    pupil_size = eye_size / 2
    # Левый глаз
    circle(surface, (255, 255, 255), (x - head_size/4, head_y + head_size/8), eye_size)
    circle(surface, (0, 0, 0), (x - head_size/4, head_y + head_size/8), pupil_size)
    # Правый глаз
    circle(surface, (255, 255, 255), (x + head_size/4, head_y + head_size/8), eye_size)
    circle(surface, (0, 0, 0), (x + head_size/4, head_y + head_size/8), pupil_size)

    # Рисуем нос
    nose_size = head_size / 10
    circle(surface, (255, 0, 0), (x, head_y + head_size/3), nose_size)
    # Рисуем ноги
    leg_height = height / 16
    leg_y = y + body_height / 2 - leg_height / 2
    draw_leg(surface, x - body_width / 2, leg_y, body_width / 4, leg_height, color)
    draw_leg(surface, x + body_width / 2, leg_y, body_width / 4, leg_height, color)

    # Рисуем усы
    for i in range(-1, 2):
        # Левые усы
        line(surface, (0, 0, 0), 
             (x - head_size/8, head_y + head_size/2.5),
             (x - head_size/2, head_y + head_size/2.5 + i*head_size/10), 1)
        # Правые усы
        line(surface, (0, 0, 0), 
             (x + head_size/8, head_y + head_size/2.5),
             (x + head_size/2, head_y + head_size/2.5 + i*head_size/10), 1)


def draw_body(surface, x, y, width, height, color):
    """Рисует тело зайца в виде многоугольника"""
    points = [
        (x - width / 2, y + height / 5),
        (x + width / 2, y + height / 5),
        (x + width / 4, y - height / 2 + 30),
        (x - width / 4, y - height / 2 + 30),
    ]
    polygon(surface, color, points)


def draw_head(surface, x, y, size, color):
    """Рисует голову зайца"""
    points = [
        (x - size / 2, y + size / 2),
        (x + size / 2, y + size / 2),
        (x + size / 2, y - size / 2),
        (x - size / 2, y - size / 2),
    ]
    polygon(surface, color, points)


def draw_ear(surface, x, y, width, height, color):
    """Рисует ухо зайца (треугольник)"""
    points = [(x, y - height), (x - width / 2, y), (x + width / 2, y)]
    polygon(surface, color, points)


def draw_leg(surface, x, y, width, height, color):
    """Рисует ногу зайца"""
    points = [
        (x - width / 2, y),
        (x + width / 2, y),
        (x + width / 2, y + height),
        (x - width / 2, y + height),
    ]
    polygon(surface, color, points)


# Основной цикл программы
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Рисуем зайца
    draw_hare(screen, 200, 200, 200, 400, (200, 200, 200))

    # Обновление экрана
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
