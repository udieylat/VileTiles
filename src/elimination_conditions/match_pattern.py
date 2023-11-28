from src.elimination_conditions.elimination_condition import IndependentEliminationCondition
from src.models.enemy import Enemy


class MatchPattern(IndependentEliminationCondition):

    def __init__(
            self,
            pattern_str: str,
    ):
        self._validate_pattern(
            pattern_str=pattern_str,
        )
        self._pattern_str = pattern_str

    def _eliminate_enemy(
            self,
            enemy: Enemy,
    ) -> bool:
        enemy_pattern_str = self._enemy_to_pattern(
            enemy=enemy,
        )
        return enemy_pattern_str == self._pattern_str

    @classmethod
    def _enemy_to_pattern(
            cls,
            enemy: Enemy,
    ) -> str:
        ctr = 0
        num_to_color = {}
        for tile in enemy.tiles:
            if tile.color.name not in num_to_color:
                num_to_color[tile.color.name] = str(ctr)
                ctr += 1
        return "".join(
            num_to_color[tile.color.name]
            for tile in enemy.tiles
        )

    @classmethod
    def _validate_pattern(
            cls,
            pattern_str: str,
    ):
        assert len(pattern_str) == 9
        assert set(pattern_str).issubset(set("012345"))
