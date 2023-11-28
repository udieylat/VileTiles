from abc import abstractmethod

from src.models.enemy import Enemy


class EliminationCondition:

    @abstractmethod
    def trigger(
            self,
            enemies: list[Enemy],
    ):
        ...


class IndependentEliminationCondition(EliminationCondition):

    def trigger(
            self,
            enemies: list[Enemy],
    ):
        for enemy in enemies:
            if self._eliminate_enemy(
                    enemy=enemy,
            ):
                enemy.disable()

    @abstractmethod
    def _eliminate_enemy(
            self,
            enemy: Enemy,
    ) -> bool:
        ...
