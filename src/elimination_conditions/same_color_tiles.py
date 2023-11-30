from src.elimination_conditions.x_tiles_same_color import XTilesSameColor


class SameColorTiles(XTilesSameColor):

    def __init__(self):
        super().__init__(
            num_tiles=9,
        )

    @property
    def description(self) -> str:
        return "All tiles with the same color"
