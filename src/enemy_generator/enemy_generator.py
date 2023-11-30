import random

from src.enemy_generator.pattern_generator import PatternGenerator
from src.models.colors import Color, ALL_COLORS
from src.models.enemy import Enemy
from src.models.tiles import Tile


class EnemyGenerator(PatternGenerator):

    def __init__(self):
        super().__init__(
            colors_pull=ALL_COLORS,
        )

    def generate_random_enemies(self, num_enemies: int) -> list[Enemy]:
        return [
            self.generate_random_enemy()
            for _ in range(num_enemies)
        ]

    def generate_random_enemy(self) -> Enemy:
        pattern = self.generate_random_pattern()
        return Enemy(
            tiles=pattern.tiles,
        )

    def generate_bullseye_enemy(
            self,
            out_color: Color = None,
            middle_color: Color = None,
    ) -> Enemy:
        if out_color is None:
            out_color = self._random_color()
        if middle_color is None:
            middle_color = self._random_color(
                exclude_color=out_color,
            )
        tiles = [
            Tile(
                color=out_color,
            )
            for _ in range(9)
        ]
        tiles[4] = Tile(
            color=middle_color,
        )
        return Enemy(
            tiles=tiles,
        )

    def _random_color(
            self,
            exclude_color: Color = None,
    ) -> Color:
        colors = [
            color
            for color in self._colors_pull
            if color != exclude_color
        ]

        return random.sample(colors, 1)[0]
