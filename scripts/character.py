from typing import List

from scripts.animations import CharacterAnimation as Animation
from scripts.active_ability import ActiveAbility
from scripts.ultra_ability import UltraAbility


class Character:

    def __init__(self, name, animation: Animation, abilities: List[ActiveAbility], ultra: UltraAbility):
        self.name = name
        self.animation = animation
        self.abilities = abilities
        self.ultra = ultra
