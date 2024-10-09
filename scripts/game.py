from scripts.character import Character
from scripts.game_states import GameState as State
from scripts.enemy import Enemy


class Game:

    def __init__(self):
        self.enemy = None
        self.character = None
        self.state = State.MENU

    def start(self, character: Character):
        self.character = character
        self.state = State.MAP

    def shop(self):
        self.state = State.SHOP

    def battle(self, enemy: Enemy):
        self.state = State.BATTLE
        self.enemy = enemy
        