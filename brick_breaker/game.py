import pygame
from pygame.sprite import Group
from settings import SetScreen, SetBall
from bat import Bat
from game_statistics import GameStatistics
from statsbroad import Statsboard
from levels import Level
from button import Button, ExitButton, ContinueButton
import game_functions as gf

conf_screen = SetScreen()
conf_ball = SetBall()


def run_game():
    """Запускает игру"""
    # Создание экрана
    pygame.init()
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((conf_screen.WIDTH, conf_screen.HEIGHT),
                                     conf_screen.FLAGS, conf_screen.DEPTH)
    pygame.display.set_caption("Brick Breaker")
    # Инициализация кнопок
    play_button = Button(screen)
    exit_button = ExitButton(screen)
    continue_button = ContinueButton(screen)
    # Инициалтзация игровой статистики
    statistics = GameStatistics(conf_ball)
    sb = Statsboard(screen, conf_screen, statistics)
    # Инициализация игровых объектов
    bat = Bat(screen)
    balls = Group()
    bricks = Group()
    iron_bricks = Group()
    improvments = Group()
    levels = Level(statistics)
    # Главный цикл
    while True:
        # Проверака событий клавиш и мышки
        gf.check_events(statistics, sb, improvments, play_button, exit_button,
                        continue_button, screen, bat, balls,
                        bricks, iron_bricks, levels)
        # Обновление объектов в игре
        if statistics.game_active and not statistics.K_ESCAPE_active:
            # Ракетка
            bat.update()
            # Обновление мячей
            gf.update_balls(conf_screen, screen, statistics, sb, improvments,
                            bat, balls, bricks, iron_bricks, levels)
            # Обновление улучшений
            gf.update_improvments(conf_screen, screen, improvments,
                                  bat, balls, statistics, sb)
        # Обновление экрана
        gf.update_screen(conf_screen, screen, fps, statistics, sb, improvments,
                         bat, balls, bricks, iron_bricks, play_button,
                         exit_button, continue_button)


run_game()
