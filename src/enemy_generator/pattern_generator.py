import random

from src.models.colors import Color
from src.models.pattern import Pattern
from src.models.tiles import Tile


class PatternGenerator:

    def __init__(
            self,
            colors_pull: list[Color],
    ):
        self._colors_pull = colors_pull

    def generate_random_patterns(self, num_patterns: int) -> list[Pattern]:
        return [
            self.generate_random_pattern()
            for _ in range(num_patterns)
        ]

    def generate_random_pattern(self) -> Pattern:
        pattern_colors = [
            random.sample(self._colors_pull, 1)[0]
            for _ in range(9)
        ]
        return self._colors_to_pattern(
            colors=pattern_colors,
        )

    def generate_pattern_from_str(
            self,
            pattern_str: str,
    ) -> Pattern:
        assert len(pattern_str) == 9
        unique_pattern_chars = list(set(pattern_str))
        assert len(unique_pattern_chars) <= len(self._colors_pull)
        random.shuffle(unique_pattern_chars)
        pattern_char_to_color = {
            pattern_char: self._colors_pull[i]
            for i, pattern_char in enumerate(unique_pattern_chars)
        }
        return self._colors_to_pattern(
            colors=[
                pattern_char_to_color[pattern_char]
                for pattern_char in pattern_str
            ],
        )

    @classmethod
    def _colors_to_pattern(
            cls,
            colors: list[Color],
    ) -> Pattern:
        return Pattern(
            tiles=[
                Tile(
                    color=color,
                )
                for color in colors
            ],
        )
