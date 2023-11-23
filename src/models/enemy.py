from dataclasses import dataclass

from src.models.tiles import Tile


@dataclass
class Enemy:
    tiles: list[Tile]
