import os


class GameStatistics():
    """Ведение статистики"""

    def __init__(self, conf_ball):
        """Инициализирует статистику"""
        self.conf_ball = conf_ball
        self.game_active = False
        self.K_ESCAPE_active = False
        self.reset_statistics()
        self.score = 0
        # Файл рекордов
        self.record_file = open(os.path.join(os.getcwd(), "records",
                                             "records.txt"), "r+")
        score_list = self.record_file.read().split("\n")
        self.high_score = max([int(n) for n in score_list])

    def reset_statistics(self):
        """Сбрасывает статистику"""
        self.lifes = self.conf_ball.LIFES
        self.score = 0
        self.level = 0
