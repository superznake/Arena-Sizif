import os
from typing import List


class ContentLoader:

    def __init__(self, content_dir: str):
        self.characters_dir: List[str]
        self.characters_dir = []
        self.enemies_dir: List[str]
        self.enemies_dir = []
        self.work_dir = content_dir
        print("Loader setup|Настройка загрузчика")
        for directory in os.listdir(self.work_dir):
            if not ('.' in directory.lower()):
                if "character" in directory.lower():
                    self.characters_dir.append(os.path.join(self.work_dir,directory))
                if "enemy" in directory.lower():
                    self.enemies_dir.append(os.path.join(self.work_dir,directory))

    def character_loader(self):
        print("Characters loading started...|Загрузка персонажей началась...")
        if not self.characters_dir:
            print("No characters files|Нет файлов персонажей")
        else:
            for directory in self.characters_dir:
                file_path = os.path.join(directory, "list.txt")
                if os.path.exists(file_path):
                    with open(file_path) as f:
                        print("Loaded:|Загружено:\n"+f.read())
                else:
                    print("Broken characters files|Файлы персонажей повреждены")
