import os
import time


class SaveLoadManager:
    def __init__(self, directory: str, name: str = "auto.txt"):
        self.directory = directory
        self.name = name

    def save(self):
        with open(os.path.join(self.directory, self.name),'w') as f:
            f.write(str(time.time()))

    def load(self):
        ...
