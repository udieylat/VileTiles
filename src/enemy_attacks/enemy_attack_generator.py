from src.enemy_attacks.max_similar_colors import MaxSimilarColors
from src.enemy_attacks.num_different_colors import NumDifferentColors
from src.enemy_attacks.numer_of_x_tiles import NumberOfXTiles
from src.models.colors import ALL_COLORS

ALL_ENEMY_ATTACKS = [
    MaxSimilarColors(),
    NumDifferentColors(),
]
ALL_ENEMY_ATTACKS += [
    NumberOfXTiles(
        color=color,
    )
    for color in ALL_COLORS
]
