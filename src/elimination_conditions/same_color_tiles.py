from src.elimination_conditions.elimination_condition import IndependentEliminationCondition
from src.models.enemy import Enemy


class SameColorTiles(IndependentEliminationCondition):

    @classmethod
    def _eliminate_enemy(
            cls,
            enemy: Enemy,
    ) -> bool:
        return all(
            enemy[0].color == tile.color
            for tile in enemy.tiles
        )
