from dataclasses import dataclass

import emoji


@dataclass
class Color:
    name: str
    char: str = None

    def __post_init__(self):
        if self.char is None:
            self.char = emoji.emojize(f":{self.name}_square:")

    def __str__(self) -> str:
        return self.char

    def __eq__(self, other):
        return isinstance(other, Color) and other.name == self.name


Blue = Color(
    name="blue",
)
Green = Color(
    name="green",
)
Yellow = Color(
    name="yellow",
)
Red = Color(
    name="red",
)
Purple = Color(
    name="purple",
)
Orange = Color(
    name="orange",
)
Black = Color(
    name="black",
    char=emoji.emojize(":black_large_square:"),
)
Brown = Color(
    name="brown",
)
White = Color(
    name="white",
    char=emoji.emojize(":white_large_square:"),
)
AnyColor = Color(
    name="any",
    char=emoji.emojize(":joker:"),
)

ALL_COLORS = [
    Blue,
    Green,
    Yellow,
    Red,
    Purple,
    Orange,
]
PATTERN_COLORS = [
    Black,
    Brown,
    White,
]

def name_to_color(name: str) -> Color:
    return next(
        color
        for color in ALL_COLORS
        if color.name == name
    )
