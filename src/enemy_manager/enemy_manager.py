import emoji

from src.elimination_conditions.elimination_condition import EliminationCondition
from src.enemy_attacks.enemy_attack import EnemyAttack
from src.models.enemy import Enemy


class EnemyManager:
    def __init__(
            self,
            enemies: list[Enemy],
            enemy_attacks: list[EnemyAttack],
            elimination_conditions: list[EliminationCondition],
    ):
        self._enemies = enemies
        self._enemy_attacks = enemy_attacks
        self._elimination_conditions = elimination_conditions
        self._enemy_buffs = []  # TODO: maybe should be on the enemies
        self._enemy_debuffs = []  # TODO: maybe should be on the enemies

    @property
    def enemies(self) -> list[Enemy]:
        return self._enemies

    @property
    def enemy_attacks(self) -> list[EnemyAttack]:
        return self._enemy_attacks

    def total_attack_for(self) -> int:
        return sum(
            self.attack_for(
                enemy=enemy,
            )
            for enemy in self._enemies
        )

    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        if enemy.disabled:
            return 0
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

    def trigger_elimination_conditions(self):
        for elimination_condition in self._elimination_conditions:
            elimination_condition.trigger(
                enemies=self._enemies,
            )

    def all_enemies_are_disabled(self) -> bool:
        return all(
            enemy.disabled
            for enemy in self._enemies
        )
