import pygame.font


class Button():
    """Класс кнопки Play"""
    def __init__(self, screen):
        """Инициализирует аттрибуты кнопки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назначение размеров и свойств кнопок
        self.width,  self.height = 125, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - self.height / 2 - 5

        # Текст на кнопке
        self.prepare_msg()

    def prepare_msg(self):
        """Преобразует msg  прямоугольник и выравнивает текст по центру"""
        self.msg = "Play"
        self.msg_image = self.font.render(self.msg, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class ExitButton(Button):
    """Кнопка Выход"""
    def __init__(self, screen):
        super().__init__(screen)
        self.button_color = (255, 0, 0)
        self.rect.centery += self.height + 5

    def prepare_msg(self):
        super().prepare_msg()
        self.msg = "Exit"
        self.msg_image = self.font.render(self.msg, True,
                                          self.text_color, (255, 0, 0))
        self.msg_image_rect.centery += self.height + 5


class ContinueButton(Button):
    """Кнопка Продолжить"""
    def __init__(self, screen):
        super().__init__(screen)
        self.width = 160
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - self.height / 2 - 5

    def prepare_msg(self):
        super().prepare_msg()
        self.msg = "Continue"
        self.msg_image = self.font.render(self.msg, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery
