from src.abilities.ability import Ability
from src.enemy_manager.enemy_manager import EnemyManager


class DisplayManager:

    PREFIX = "    "
    GAP = "       "

    def __init__(
            self,
            enemy_manager: EnemyManager,
    ):
        self._enemy_manager = enemy_manager

    def display_fight(
            self,
            hand: list[Ability],
    ):
        self.display_enemy_attacks()
        self.display_enemies()
        print()
        print()
        self.display_hand(
            hand=hand,
        )
        # TODO: display shields and blood

    def display_enemies(self):
        s = self.PREFIX + f"\n{self.PREFIX}".join(
            [
                self.GAP.join(
                    [
                        enemy.get_display_row(
                            index=index,
                        )
                        for enemy in self._enemy_manager.enemies
                    ]
                )
                for index in [1, 2, 3]
            ]
        )
        print(s)

    def display_enemy_attacks(self):
        s = self.PREFIX + self.GAP.join(
            [
                f"  {self._enemy_manager.attack_for_str(enemy=enemy)}   "
                for enemy in self._enemy_manager.enemies
            ]
        )
        print()
        print(s)
        print()

    @classmethod
    def display_hand(
            cls,
            hand: list[Ability],
    ):
        print()
        for i, ability in enumerate(hand):
            print(f" {i+1}. {ability}")
        print()

    # def display_enemy_attacks_menu(self):
    #     # Maybe obsolete
    #     print()
    #     for i, enemy_attack in enumerate(self._enemy_manager.enemy_attacks):
    #         print(f" {i+1}. {enemy_attack.description}")
    #     print()
    #
    # def display_new_abilities(self):
    #     pass
