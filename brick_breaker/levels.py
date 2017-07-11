import os


class Level():
    """Класс уровней"""
    def __init__(self, statistics):
        self.number_levels = self.search_levels()
        self.level = statistics.level

    def load_level(self, level):
        """Загружает из файла и подготавливает уровнеь к созданию"""
        level_file = os.getcwd() + r"\levels\level_" + str(level) + ".txt"
        prep_lines = [el.split() for el in open(level_file).read().split("\n")]
        prepared_level = [list(el) for lines in prep_lines for el in lines]
        return prepared_level

    def search_levels(self):
        """Выполняет поиск уровней в директории levels"""
        directory = os.getcwd() + "\\levels\\"
        files = os.listdir(directory)
        number_levels = [file for file in files if file[0:6] == "level_"]
        return len(number_levels)
