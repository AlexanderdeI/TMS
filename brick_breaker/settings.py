import pygame
import os


class SetScreen():
    # Параметры экрана
    def __init__(self):
        self.WIDTH = 640
        self.HEIGHT = 480
        self.FLAGS = 0
        self.DEPTH = 32
        self.BG_COLOR = (205, 255, 205)
        self.FPS = 100


class SetBat():
    # Параметры ракетки
    def __init__(self):
        self.IMAGE = pygame.image.load(os.getcwd() + r'/images/bat.png')
        self.SPEED = 8
        self.COEF_LR = 0.4
        self.COEF_CENTR = 0.1
        self.DEFAULT_POWER = 0.1


class SetBall():
    # Параметры шара
    def __init__(self):
        self.IMAGE = pygame.image.load(os.getcwd() + r'/images/ball.png')
        self.SPEED = 2.5
        self.LIFES = 3
        self.BALLS_COUNT = 0


class SetBrick():
    # Параметры кирпичей
    def __init__(self):
        self.IMAGE = pygame.image.load(os.getcwd() + r'/images/brick.png')
        self.IRON_BRICK_IMAGE = pygame.image.load(os.getcwd() +
                                                  r'/images/iron_brick.png')
        self.COST = 50


class SetImprovmets():
    # Параметры улучшений
    def __init__(self):
        self.LIFE = pygame.image.load(os.getcwd() + r'/images/life.png')
        self.EXTRA_BALL = pygame.image.load(os.getcwd() + r'/images/ball.png')
        self.DEATH = pygame.image.load(os.getcwd() + r'/images/death.png')
        self.FALL_RATE = 2
