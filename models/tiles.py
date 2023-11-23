from dataclasses import dataclass

from models.colors import Color


@dataclass
class Tile:
    color: Color
