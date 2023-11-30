from collections import Counter

from src.elimination_conditions.elimination_condition import IndependentEliminationCondition
from src.models.enemy import Enemy


class XTilesSameColor(IndependentEliminationCondition):

    def __init__(
            self,
            num_tiles: int,
    ):
        self._num_tiles = num_tiles

    def _eliminate_enemy(
            self,
            enemy: Enemy,
    ) -> bool:
        c = Counter([
            tile.color.name
            for tile in enemy.tiles
        ])
        return max(c.values()) >= self._num_tiles

    @property
    def description(self) -> str:
        return f"{self._num_tiles} tiles with the same color"
