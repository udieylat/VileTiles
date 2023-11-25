import emoji

from src.enemy_attacks.enemy_attack import EnemyAttack
from src.models.enemy import Enemy


class EnemyManager:
    def __init__(
            self,
            enemies: list[Enemy],
            enemy_attacks: list[EnemyAttack],
    ):
        self._enemies = enemies
        self._enemy_attacks = enemy_attacks
        self._enemy_buffs = []  # TODO
        self._enemy_debuffs = []  # TODO

    @property
    def enemies(self) -> list[Enemy]:
        return self._enemies

    @property
    def enemy_attacks(self) -> list[EnemyAttack]:
        return self._enemy_attacks

    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        attack_sum = sum(
            enemy_attack.attack_for(
                enemy=enemy,
            )
            for enemy_attack in self._enemy_attacks
        )
        return min(9, attack_sum)

    def attack_for_str(
            self,
            enemy: Enemy,
    ) -> str:
        attack = self.attack_for(
            enemy=enemy,
        )
        return emoji.emojize(f":keycap_{attack}:")
