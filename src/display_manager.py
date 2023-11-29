import emoji

from src.abilities.ability import Ability
from src.enemy_manager.enemy_manager import EnemyManager
from src.models.enemy import Enemy


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
            num_shield: int,
            num_blood: int,
    ):
        # TODO: display patterns trigger (enemy elimination / reward)
        # TODO: display patterns
        self._display_enemy_attacks()
        self._display_enemies()
        print()  # TODO: buffs
        self._display_enemy_debuffs()
        self.display_abilities(
            abilities=hand,
        )
        self._display_shield_and_blood(
            num_shield=num_shield,
            num_blood=num_blood,
        )

    def _display_enemies(self):
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

    def _display_enemy_attacks(self):
        s = self.PREFIX + self.GAP.join(
            [
                f"  {self._enemy_manager.attack_for_str(enemy=enemy)}   "
                for enemy in self._enemy_manager.enemies
            ]
        )
        print()
        print(s)
        print()

    def _display_enemy_debuffs(self):
        any_debuffs = any(
            enemy.disabled  # TODO: change to any debuff
            for enemy in self._enemy_manager.enemies
        )
        if not any_debuffs:
            print()
            return

        s = self.PREFIX + self.GAP.join(
            [
                f"  {self._get_enemy_debuff_str(enemy=enemy)}   "
                for enemy in self._enemy_manager.enemies
            ]
        )
        print(s)

    @classmethod
    def _get_enemy_debuff_str(
            cls,
            enemy: Enemy,
    ) -> str:
        if enemy.disabled:
            return emoji.emojize(":cross_mark:")
        return " "

    @classmethod
    def display_abilities(
            cls,
            abilities: list[Ability],
    ):
        print()
        for i, ability in enumerate(abilities):
            print(f" {i+1}. {ability}")
        print()

    @classmethod
    def _display_shield_and_blood(
            cls,
            num_shield: int,
            num_blood: int,
    ):
        shield_str = cls._split_with_delimiter(
            s=emoji.emojize(":shield:") + " ",
            total_amount=num_shield,
        )
        blood_str = cls._split_with_delimiter(
            s=emoji.emojize(":drop_of_blood:"),
            total_amount=num_blood,
        )
        print()
        print(shield_str)
        print(blood_str)
        print()

    @classmethod
    def _split_with_delimiter(
            cls,
            s: str,
            total_amount: int,
            delimiter: str = ",",
            num_split: int = 5,
    ):
        output = delimiter.join(
            [
                s * num_split
                for _ in range(int(total_amount / num_split))
            ]
        )
        if total_amount % num_split == 0:
            return output
        output += delimiter
        output += s * (total_amount % num_split)
        return output

    # def display_enemy_attacks_menu(self):
    #     # Maybe obsolete
    #     print()
    #     for i, enemy_attack in enumerate(self._enemy_manager.enemy_attacks):
    #         print(f" {i+1}. {enemy_attack.description}")
    #     print()
    #
    # def display_new_abilities(self):
    #     pass
