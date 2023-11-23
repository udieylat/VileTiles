from src.models.enemy import Enemy


class DisplayManager:
    def __init__(
            self,
            enemies: list[Enemy],
    ):
        self._enemies = enemies

    def display(self):
        s = "\n".join(
            [
                "    ".join(
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
