from src.elimination_conditions.x_tiles_same_color import XTilesSameColor


class SameColorTiles(XTilesSameColor):

    def __init__(self):
        super().__init__(
            num_tiles=9,
        )
