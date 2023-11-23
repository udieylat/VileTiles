from abc import abstractmethod

from src.models.colors import Color
from src.models.enemy import Enemy


class EnemyAttack:

    ATTACK_TO_STR = [
        u'\u0030\ufe0f\u20e3',
        u'\u0031\ufe0f\u20e3',
        u'\u0032\ufe0f\u20e3',
        u'\u0033\ufe0f\u20e3',
        u'\u0034\ufe0f\u20e3',
        u'\u0035\ufe0f\u20e3',
        u'\u0036\ufe0f\u20e3',
        u'\u0037\ufe0f\u20e3',
        u'\u0038\ufe0f\u20e3',
        u'\u0039\ufe0f\u20e3',
    ]

    @abstractmethod
    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        ...

    def attack_for_str(
            self,
            enemy: Enemy,
    ) -> str:
        attack = self.attack_for(
            enemy=enemy,
        )
        return self.ATTACK_TO_STR[attack]


class NumberOfXTiles(EnemyAttack):

    def __init__(
            self,
            color: Color,
    ):
        self._color = color

    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        return sum(
            tile.color == self._color
            for tile in enemy.tiles
        )
