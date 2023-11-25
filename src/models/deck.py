from pydantic import BaseModel

from src.abilities.ability import Ability


class Deck(BaseModel):
    abilities: list[Ability]
