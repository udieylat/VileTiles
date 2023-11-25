from src.elimination_conditions.elimination_condition import EliminationCondition
from src.models.enemy import Enemy


class SameColorTiles(EliminationCondition):
    def trigger(
            self,
            enemies: list[Enemy],
    ):
        for enemy in enemies:
            if self._eliminate_enemy(
                    enemy=enemy,
            ):
                enemy.disable()

    @classmethod
    def _eliminate_enemy(
            cls,
            enemy: Enemy,
    ) -> bool:
        return all(
            enemy[0].color == tile.color
            for tile in enemy.tiles
        )
