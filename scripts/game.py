from scripts.character import Character
from scripts.game_states import GameState as State


class Game:

    def __init__(self):
        self.character = None
        self.state = State.MENU

    def start(self, character: Character):
        self.character = character
        self.state = State.MAP

    def shop(self):
        self.state = State.SHOP

    def battle(self):
        self.state = State.BATTLE