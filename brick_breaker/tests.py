import unittest
import pygame
from bat import Bat
from ball import Ball
from bricks import Brick


class TestGame(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.screen_rect = self.screen.get_rect()
        self.bat = Bat(self.screen)
        self.ball = Ball(self.screen, self.bat)
        self.brick = Brick(self.screen)

    def test_check_bat_moving_right(self):
        bat_start_position = self.bat.rect.topleft
        self.bat.moving_right = True
        for _ in range(10):
            self.bat.update()
        self.bat.moving_right = False
        self.assertGreater(self.bat.rect.topleft, bat_start_position)

    def test_check_bat_moving_left(self):
        bat_start_position = self.bat.rect.topleft
        self.bat.moving_left = True
        for _ in range(10):
            self.bat.update()
        self.bat.moving_left = False
        self.assertLess(self.bat.rect.topleft, bat_start_position)

    def test_bat_no_screen_out(self):
        self.bat.rect.left = self.screen_rect.left
        bat_start_position = self.bat.rect.left
        self.bat.moving_left = True
        for _ in range(1000):
            self.bat.update()
        self.bat.moving_left = False
        self.assertEqual(self.bat.rect.left, bat_start_position)

    def test_ball_moving(self):
        ball_start_position = self.ball.rect.topleft
        self.ball.moving = True
        for _ in range(10):
            self.ball.update(self.bat)
        self.ball.moving = False
        self.assertGreater(self.ball.rect.topleft, ball_start_position)

    def test_ball_reflect_from_screen(self):
        ball_start_speed = self.ball.speedx, self.ball.speedy
        self.ball.moving = True
        while self.ball.rect.colliderect(self.screen_rect):
            self.ball.update(self.bat)
        self.assertNotEqual((self.ball.speedx, self.ball.speedy),
                            ball_start_speed)

    def test_ball_reflect_from_bat(self):
        ball_start_speed = self.ball.speedx, self.ball.speedy
        self.ball.moving = True
        while self.ball.rect.colliderect(self.bat.rect):
            self.ball.update(self.bat)
        self.ball.reflect(self.bat)
        self.assertNotEqual((self.ball.speedx, self.ball.speedy),
                            ball_start_speed)

    def test_ball_reflect_from_brick(self):
        brick_position = (10, 10)
        self.brick.rect.topright = brick_position
        ball_position = (20, 20)
        self.ball.rect.topright = ball_position
        ball_start_speed = self.ball.speedx, self.ball.speedy
        self.ball.moving = True
        while self.ball.rect.colliderect(self.brick.rect):
            self.ball.update(self.bat)
        self.ball.reflect_from_brick()
        self.ball.moving = False
        self.assertNotEqual((self.ball.speedx, self.ball.speedy),
                            ball_start_speed)

if __name__ == '__main__':
    unittest.main()
