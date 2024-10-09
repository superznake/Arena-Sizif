from content.animations import AbilityAnimation as Animation


class ActiveAbility:

    def __init__(self, name: str, cost: int, power: int, description: str, animation: Animation):
        self.name = name
        self.cost = cost
        self.power = power
        self.description = description
        self.animation = animation

    def use(self, target):
        ...
