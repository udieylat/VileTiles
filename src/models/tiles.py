from dataclasses import dataclass

from src.models.colors import Color


@dataclass
class Tile:
    color: Color
