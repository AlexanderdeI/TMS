from settings import SetBat

conf_bat = SetBat()


class Bat():

    def __init__(self, screen):
        # Создает ракетку в начальной позиции
        self.screen = screen
        self.image = conf_bat.IMAGE
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Назначение начальной позиции
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.screen_rect.bottom -
                            self.screen_rect.bottom // 20)
        self.bottom = self.rect.bottom

        self.center = float(self.rect.centerx)
        self.power = conf_bat.DEFAULT_POWER
        self.lenght = self.rect.right - self.rect.left

        # Статус движения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию ракетки если статус движения True"""
        if (self.rect.right < self.screen_rect.right - 5.0 and
                self.moving_right):
            self.center += conf_bat.SPEED
            self.power += 0.0075 * conf_bat.SPEED
        if self.moving_left and self.rect.left > 5.0:
            self.center -= conf_bat.SPEED
            self.power += 0.0075 * conf_bat.SPEED
        # Обновление координаты центра ракетки
        self.rect.centerx = self.center

    def set_default_power(self):
        """Сбрасывает силу ракетки"""
        self.power = conf_bat.DEFAULT_POWER

    def center_bat(self):
        """Центрирует ракетку"""
        self.center = self.screen_rect.centerx

    def blit_bat(self):
        # Рисует ракетку в текущей позиции
        self.screen.blit(self.image, self.rect)
