from dataclasses import dataclass

from src.models.tiles import Tile


@dataclass
class Enemy:
    tiles: list[Tile]

    def get_display_row(
            self,
            index: int,
    ) -> str:
        assert 1 <= index <= 3
        return sum(
            tile.color.char
            for tile in self.tiles[(index-1)*3:index*3]
        )
