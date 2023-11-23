from dataclasses import dataclass

from models.tiles import Tile


@dataclass
class Enemy:
    tiles: list[Tile]
