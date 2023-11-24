from abc import abstractmethod

import emoji

from src.models.enemy import Enemy


class EnemyAttack:

    @abstractmethod
    def attack_for(
            self,
            enemy: Enemy,
    ) -> int:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    def attack_for_str(
            self,
            enemy: Enemy,
    ) -> str:
        attack = self.attack_for(
            enemy=enemy,
        )
        return emoji.emojize(f":keycap_{attack}:")
