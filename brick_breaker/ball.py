from pygame.sprite import Sprite
from settings import SetBall

conf_ball = SetBall()


class Ball(Sprite):

    def __init__(self, screen, bat):
        """Создает шарик в текущей позиции ракетки"""
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = conf_ball.IMAGE
        self.rect = self.image.get_rect()
        # Назначение начальной позиции
        self.rect.centerx = bat.rect.centerx
        self.rect.bottom = bat.rect.top - 10
        # Переменные с текущими координатами
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        self.speedx, self.speedy = conf_ball.SPEED, conf_ball.SPEED
        self.count = conf_ball.BALLS_COUNT

        # Статус движения
        self.moving = False
        self.moving_left = False
        self.moving_right = False

    def reflect(self, bat, reverse=False):
        """Отражает шарик от ракетки"""
        r_fact = 1
        if reverse:
            r_fact = -1
        distance_from_center = abs(int(self.x - bat.center))
        d_fact = distance_from_center / bat.lenght
        self.speedx = 3.5 * d_fact * r_fact * conf_ball.SPEED + bat.power
        self.speedy = 1.75 * (1 - d_fact) * conf_ball.SPEED + 0.1 * bat.power

    def update(self, bat):
        """Перемещает шарик по экрану"""
        if self.moving:
            self.y -= self.speedy
            self.x += self.speedx
        # Изменение направления при столкновении с краем экрана
        if self.y < 0:
            self.speedy *= -1
        elif self.x < 0 or self.x > self.screen_rect.right:
            self.speedx *= -1
        # Изменение статуса движения
        if self.speedx > 0:
            self.moving_right = True
            self.moving_left = False
        elif self.speedx < 0:
            self.moving_right = False
            self.moving_left = True
        # Изменение направления при столкновении с ракеткой
        if self.y > bat.rect.top and self.rect.colliderect(bat.rect):
            if self.x <= bat.center:
                self.reflect(bat, reverse=True)
            else:
                self.reflect(bat)
        # Обновление координат шарика
        self.rect.centery = self.y
        self.rect.centerx = self.x

    def reflect_from_brick(self, reverse=False):
        if reverse:
            self.speedy *= -1
            self.speedx *= -1
        else:
            self.speedy *= -1

    def blit_ball(self):
        # Рисует шарик в текущей позиции
        self.screen.blit(self.image, self.rect)
