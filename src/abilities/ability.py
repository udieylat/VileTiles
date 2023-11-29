from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class AbilityResponse:
    num_shields: int = 0

    @classmethod
    def empty(cls) -> AbilityResponse:
        return AbilityResponse()


class Ability:

    @abstractmethod
    def play(
            self,
            ability_args: dict,
    ) -> AbilityResponse:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @classmethod
    @abstractmethod
    def all_options(cls) -> list[Ability]:
        ...
