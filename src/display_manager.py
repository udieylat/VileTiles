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

    def display_enemy_attack_menu(self):
        pass

    def display_new_abilities(self):
        pass
