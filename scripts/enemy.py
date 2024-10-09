from typing import List

from scripts.active_ability import EnemyAbility as Ability
from scripts.animations import Animation
from scripts.ultra_ability import EnemyUltra as Ultra


class Enemy:
    def __init__(self, name: str, animation: Animation,abilities: List[Ability], ultra: Ultra):
        self.name = name
        self.animation = animation
        self.abilities = abilities
        self.ultra = ultra
