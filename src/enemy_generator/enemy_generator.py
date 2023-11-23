import random

from src.models.colors import Blue, Green, Purple, Red, Yellow, Orange
from src.models.enemy import Enemy
from src.models.tiles import Tile


class EnemyGenerator:

    S_TO_COLOR = {
        'b': Blue,
        'g': Green,
        'p': Purple,
        'y': Yellow,
        'r': Red,
        'o': Orange,
    }

    def generate_random_enemy(self) -> Enemy:
        enemy_str = sum(
            random.sample(self.S_TO_COLOR.keys(), 1)
            for _ in range(9)
        )
        return self.str_to_enemy(
            enemy_str=enemy_str,
        )

    def str_to_enemy(
            self,
            enemy_str: str,
    ) -> Enemy:
        return Enemy(
            tiles=[
                self._str_to_tile(s)
                for s in enemy_str
            ],
        )

    def _str_to_tile(self, s: str) -> Tile:
        return Tile(
            color=self.S_TO_COLOR[s],
        )
