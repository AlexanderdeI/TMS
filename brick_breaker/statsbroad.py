import pygame.font
from pygame.sprite import Group
from improvments import Life
from bricks import Brick


class Statsboard():
    """Класс для вывода игровой информации"""
    def __init__(self, screen, conf_screen, statistics):
        """Инициализирует игровые переменные"""
        self.screen = screen
        self.conf_screen = conf_screen
        self.screen_rect = screen.get_rect()
        self.statistics = statistics

        # Настройки шрифта для вывода на экран
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 18)
        # Подготовка изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lifes()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображеие"""
        score = str(self.statistics.score)
        self.score_image = self.font.render("Score: " + score, True,
                                            self.text_color,
                                            self.conf_screen.BG_COLOR)

        # Вывод счета в нижней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.bottom = self.screen_rect.bottom - 4

    def prep_high_score(self):
        """Создание графического отображения макс. счета"""
        high_score = str(self.statistics.high_score)
        self.h_score_image = self.font.render("High Score: " + high_score, True,
                                              self.text_color,
                                              self.conf_screen.BG_COLOR)

        # Вывод счета в нижней правой части экрана
        self.h_score_rect = self.score_image.get_rect()
        self.h_score_rect.right = self.screen_rect.right - 60
        self.h_score_rect.bottom = self.score_rect.bottom

    def prep_level(self):
        """Подготовка отображения № уровня"""
        self.level_image = self.font.render("Level: " + str(self.statistics.level), True,
                                            self.text_color, self.conf_screen.BG_COLOR)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = 30
        self.level_rect.bottom = self.score_rect.bottom

    def prep_lifes(self):
        """Подготовка отображения жизней"""
        self.lifes = Group()
        self.brick = Brick(self.screen)
        for life in range(self.statistics.lifes):
            self.life = Life(self.screen, self.brick)
            self.life.rect.x = 10 + life * (self.life.rect.width + 2.5)
            self.life.rect.y = 5
            self.lifes.add(self.life)

    def show_score(self):
        """Выводит статистику на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.h_score_image, self.h_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        for life in self.lifes.sprites():
            life.blit()
