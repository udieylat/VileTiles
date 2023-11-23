from dataclasses import dataclass


@dataclass
class Color:
    name: str
    char: str

    def __str__(self) -> str:
        return self.char


Blue = Color(
    name="blue",
    char="\U0001F7E6",
)
Green = Color(
    name="green",
    char="\U0001F7E9",
)
Yellow = Color(
    name="green",
    char="\U0001F7E8",
)
Red = Color(
    name="green",
    char="\U0001F7E5",
)
Purple = Color(
    name="green",
    char="\U0001F7EA",
)
Orange = Color(
    name="green",
    char="\U0001F7E7",
)
