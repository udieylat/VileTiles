from dataclasses import dataclass

from src.abilities.ability import Ability


@dataclass
class Deck:
    abilities: list[Ability]
