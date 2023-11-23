from src.models.enemy import Enemy


class DisplayManager:
    def __init__(
            self,
            enemies: list[Enemy],
    ):
        self._enemies = enemies

    def display_enemies(self):
        prefix = "    "
        gap = "       "
        s = prefix + f"\n{prefix}".join(
            [
                gap.join(
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

    def display_enemy_attacks(self):
        pass

    def display_new_abilities(self):
        pass
