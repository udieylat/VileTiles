from src.elimination_conditions.elimination_condition import IndependentEliminationCondition
from src.models.enemy import Enemy


class RectSameColorTiles(IndependentEliminationCondition):

    @classmethod
    def _eliminate_enemy(
            cls,
            enemy: Enemy,
    ) -> bool:
        rect_possible_indices = [
            [0, 1, 3, 4, 6, 7],
            [1, 2, 4, 5, 7, 8],
            [0, 1, 2, 3, 4, 5],
            [3, 4, 5, 6, 7, 8],
        ]
        return any(
            all(
                enemy[indices[0]].color == enemy[index].color
                for index in indices
            )
            for indices in rect_possible_indices
        )

    @property
    def description(self) -> str:
        return "Rectangle with same tiles color"
