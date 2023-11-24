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
    name="green",
    char=emoji.emojize(':yellow_square:'),
)
Red = Color(
    name="green",
    char=emoji.emojize(':red_square:'),
)
Purple = Color(
    name="green",
    char=emoji.emojize(':purple_square:'),
)
Orange = Color(
    name="green",
    char=emoji.emojize(':orange_square:'),
)
