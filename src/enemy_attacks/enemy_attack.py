from abc import abstractmethod

from src.models.colors import Color
from src.models.enemy import Enemy


class EnemyAttack:

    @abstractmethod
    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        ...


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
