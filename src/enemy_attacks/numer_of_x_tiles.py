import emoji

from src.enemy_attacks.enemy_attack import EnemyAttack
from src.models.colors import Color
from src.models.enemy import Enemy


class NumberOfXTiles(EnemyAttack):

    def __init__(
            self,
            color: Color,
    ):
        self._color = color

    @property
    def description(self) -> str:
        return f"{emoji.emojize(':keycap_#:')} {self._color}"

    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        return sum(
            tile.color == self._color
            for tile in enemy.tiles
        )
