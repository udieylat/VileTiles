from collections import Counter

from src.enemy_attacks.enemy_attack import EnemyAttack
from src.models.enemy import Enemy


class MaxSimilarColors(EnemyAttack):

    @property
    def description(self) -> str:
        return "Max number of the same color"

    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        c = Counter([
            tile.color.name
            for tile in enemy.tiles
        ])
        return max(c.values())
