import random
from pygame.sprite import Sprite
from settings import SetImprovmets, SetScreen

conf_imp = SetImprovmets()
conf_screen = SetScreen()


class Improvment(Sprite):
    def __init__(self, screen, brick):
        """Класс улучшений"""
        super(Improvment, self).__init__()
        self.screen = screen
        self.brick = brick

        self.improvments_list = list((conf_imp.LIFE, conf_imp.EXTRA_BALL,
                                      conf_imp.DEATH))
        self.type_dict = {conf_imp.LIFE: "life", conf_imp.EXTRA_BALL: "ball",
                          conf_imp.DEATH: "death"}

        self.improvment = self.chose_random_improvments()
        self.type = self.determine_type()

        self.rect = self.improvment.get_rect()
        self.rect.centerx = self.brick.rect.centerx
        self.rect.centery = self.brick.rect.centery
        self.y = float(self.rect.centery)
        self.fall_rate = conf_imp.FALL_RATE

    def chose_random_improvments(self):
        """Выбирает случайное улучшение"""
        improvment = random.choice(self.improvments_list)
        return improvment

    def determine_type(self):
        """Определяет тип улучшения"""
        type = self.type_dict.get(self.improvment)
        return type

    def fall_down(self):
        """Движение улучшения вниз по экрану"""
        self.y += self.fall_rate
        self.rect.centery = self.y

    def blit(self):
        """Прорисовка улучшения"""
        self.screen.blit(self.improvment, self.rect)


class Life(Improvment):
    """Класс отображения жизней на экране"""
    def __init__(self, screen, brick):
        super().__init__(screen, brick)
        self.improvment = conf_imp.LIFE
        self.rect = conf_imp.LIFE.get_rect()

    def blit(self):
        super().blit()
