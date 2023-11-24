import random

from src.models.colors import Blue, Green, Purple, Red, Yellow, Orange, Color, ALL_COLORS
from src.models.enemy import Enemy
from src.models.tiles import Tile


class EnemyGenerator:

    COLOR_STRINGS = "".join(
        color.name[0]
        for color in ALL_COLORS
    )
    S_TO_COLOR = {
        s: color
        for s, color in zip(COLOR_STRINGS, ALL_COLORS)
    }

    @classmethod
    def generate_random_enemy(cls) -> Enemy:
        enemy_str = "".join(
            random.sample(cls.COLOR_STRINGS, 1)[0]
            for _ in range(9)
        )
        return cls._str_to_enemy(
            enemy_str=enemy_str,
        )

    @classmethod
    def generate_bullseye_enemy(
            cls,
            out_color: Color = None,
            middle_color: Color = None,
    ) -> Enemy:
        if out_color is None:
            out_color = cls._random_color()
        if middle_color is None:
            middle_color = cls._random_color(
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

    @classmethod
    def _str_to_enemy(
            cls,
            enemy_str: str,
    ) -> Enemy:
        return Enemy(
            tiles=[
                cls._str_to_tile(
                    s=s,
                )
                for s in enemy_str
            ],
        )

    @classmethod
    def _str_to_tile(cls, s: str) -> Tile:
        return Tile(
            color=cls.S_TO_COLOR[s],
        )

    @classmethod
    def _random_color(
            cls,
            exclude_color: Color = None,
    ) -> Color:
        colors = [
            color
            for color in ALL_COLORS
            if color != exclude_color
        ]

        return random.sample(colors, 1)[0]
