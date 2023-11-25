from abc import abstractmethod

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
