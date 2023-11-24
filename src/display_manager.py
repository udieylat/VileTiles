from src.enemy_attacks.enemy_attack import EnemyAttack
from src.models.enemy import Enemy


class DisplayManager:

    PREFIX = "    "
    GAP = "       "

    def __init__(
            self,
            enemies: list[Enemy],
    ):
        self._enemies = enemies

    def display_enemies(self):
        s = self.PREFIX + f"\n{self.PREFIX}".join(
            [
                self.GAP.join(
                    [
                        enemy.get_display_row(
                            index=index,
                        )
                        for enemy in self._enemies
                    ]
                )
                for index in [1, 2, 3]
            ]
        )
        print(s)

    def display_enemy_attacks(
            self,
            enemy_attack: EnemyAttack,
    ):
        s = self.PREFIX + self.GAP.join(
            [
                f"  {enemy_attack.attack_for_str(enemy=enemy)}   "
                for enemy in self._enemies
            ]
        )
        print()
        print(s)
        print()

    @classmethod
    def display_enemy_attacks_menu(
            cls,
            enemy_attacks: list[EnemyAttack],
    ):
        print()
        for i, enemy_attack in enumerate(enemy_attacks):
            print(f" {i+1}. {enemy_attack.description}")
        print()

    def display_new_abilities(self):
        pass
