import os
from settings import SetScreen
from bricks import Brick

screen = SetScreen()
brick = Brick(screen)


class Level():
    """Класс уровней"""
    def __init__(self, statistics):
        self.number_levels = self.search_levels()
        self.level = statistics.level

    def load_level(self, level):
        """Загружает из файла и подготавливает уровнеь к созданию"""
        level_file = os.path.join(os.getcwd(), "levels",
                                  "level_{0}.txt".format(str(level)))
        prep_lines = [el.split() for el in open(level_file).read().split("\n")]
        prepared_level = [list(el) for lines in prep_lines for el in lines]
        max_brick_row = screen.WIDTH // brick.width - 1
        max_brick_column = screen.HEIGHT // brick.height - 7
        if len(max(prepared_level)) > max_brick_row:
            print("Incorrect level_{0} file:\n"
                  "The length of brick wall bigger than screen width\n"
                  "The max number of bricks in row: {1}\n"
                  "Please correct file to play.".format(self.level, max_brick_row))
            exit()
        elif len(prepared_level) > max_brick_column:
            print("Incorrect level_{0} file:\n"
                  "The length of brick wall bigger than screen height\n"
                  "The max number of bricks in column: {1}\n"
                  "Please correct file to play.".format(self.level, max_brick_column))
            exit()
        else:
            return prepared_level

    def search_levels(self):
        """Выполняет поиск уровней в директории levels"""
        directory = os.path.join(os.getcwd(), "levels")
        files = os.listdir(directory)
        number_levels = [file for file in files if file[0:7] == "level_"]
        return len(number_levels)
