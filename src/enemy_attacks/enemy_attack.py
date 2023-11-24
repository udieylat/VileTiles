from abc import abstractmethod

import emoji

from src.models.colors import Color
from src.models.enemy import Enemy


class EnemyAttack:

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
        return emoji.emojize(f":keycap_{attack}:")


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
