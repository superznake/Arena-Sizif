from scripts.animations import AbilityAnimation as Animation


class UltraAbility:

    def __init__(self, name: str, power: int, description: str, animation: Animation):
        self.name = name
        self.power = power
        self.description = description
        self.animation = animation

    def use(self, target):
        ...


class EnemyUltra:
    def use(self, target):
        ...
