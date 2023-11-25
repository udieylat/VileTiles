import random

from src.enemy_attacks.enemy_attack import EnemyAttack
from src.enemy_attacks.max_similar_colors import MaxSimilarColors
from src.enemy_attacks.num_different_colors import NumDifferentColors
from src.enemy_attacks.numer_of_x_tiles import NumberOfXTiles
from src.models.colors import ALL_COLORS

ALL_ENEMY_ATTACKS: list[EnemyAttack] = [
    MaxSimilarColors(),
    NumDifferentColors(),
]
ALL_ENEMY_ATTACKS += [
    NumberOfXTiles(
        color=color,
    )
    for color in ALL_COLORS
]


class EnemyAttackGenerator:

    @classmethod
    def generate_enemy_attacks(
            cls,
            num: int = 3,
    ) -> list[EnemyAttack]:
        return random.sample(ALL_ENEMY_ATTACKS, num)

    @classmethod
    def generate_enemy_attack(cls) -> EnemyAttack:
        return cls.generate_enemy_attacks(num=1)[0]
