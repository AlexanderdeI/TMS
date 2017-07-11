import pygame
from pygame.sprite import Sprite
from settings import SetBrick

conf_brick = SetBrick()


class Brick(Sprite):
    """Класс, представляющий один кирпичик"""
    def __init__(self, screen):
        """Создает кирпич в начальной позиции"""
        super().__init__()
        self.screen = screen

        self.image = conf_brick.IMAGE
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.width = self.rect.width
        self.height = self.rect.height

        self.x = float(self.rect.x)
        # Стоимость кирпича(очки)
        self.cost = conf_brick.COST

    def blit_brick(self):
        """Выводит кирпичик на экран"""
        self.screen.blit(self.image, self.rect)


class IronBrick(Brick):
    """Класс неразрушаемого кирпича"""
    def __init__(self, screen):
        super().__init__(screen)
        self.image = conf_brick.IRON_BRICK_IMAGE

    def blit_brick(self):
        super().blit_brick()
