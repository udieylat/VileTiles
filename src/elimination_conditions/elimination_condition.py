from abc import abstractmethod

from src.models.enemy import Enemy


class EliminationCondition:

    @abstractmethod
    def trigger(
            self,
            enemies: list[Enemy],
    ):
        ...
