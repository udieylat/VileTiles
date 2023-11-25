from dataclasses import dataclass

import emoji


@dataclass
class Color:
    name: str
    char: str

    def __str__(self) -> str:
        return self.char

    def __eq__(self, other):
        return isinstance(other, Color) and other.name == self.name


Blue = Color(
    name="blue",
    char=emoji.emojize(':blue_square:'),
)
Green = Color(
    name="green",
    char=emoji.emojize(':green_square:'),
)
Yellow = Color(
    name="yellow",
    char=emoji.emojize(':yellow_square:'),
)
Red = Color(
    name="red",
    char=emoji.emojize(':red_square:'),
)
Purple = Color(
    name="purple",
    char=emoji.emojize(':purple_square:'),
)
Orange = Color(
    name="orange",
    char=emoji.emojize(':orange_square:'),
)

ALL_COLORS = [
    Blue,
    Green,
    Yellow,
    Red,
    Purple,
    Orange,
]


def name_to_color(name: str) -> Color:
    return next(
        color
        for color in ALL_COLORS
        if color.name == name
    )
