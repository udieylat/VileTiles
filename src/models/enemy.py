from dataclasses import dataclass

from src.models.tiles import Tile


@dataclass
class Enemy:
    tiles: list[Tile]

    def __repr__(self) -> str:
        return f"""{self.get_display_row(index=1)}
{self.get_display_row(index=2)}
{self.get_display_row(index=3)}
"""

    def get_display_row(
            self,
            index: int,
    ) -> str:
        assert 1 <= index <= 3
        return "".join(
            tile.color.char
            for tile in self.tiles[(index-1)*3:index*3]
        )
