import random

from src.abilities.block import Block
from src.abilities.change_tile import ChangeTile
from src.models.colors import ALL_COLORS
from src.models.deck import Deck


class StarterDeckGenerator:

    @classmethod
    def generate_starter_deck(cls) -> Deck:
        change_tile_abilities = [
            ChangeTile(
                from_color=from_color,
                to_color=to_color,
            )
            for from_color in ALL_COLORS
            for to_color in ALL_COLORS
            if from_color != to_color
        ]
        block_abilities = [
            Block(
                num_block=num_block,
            )
            for num_block in [3, 4, 5]
        ]

        num_starter_change_tile_abilities = 7
        num_starter_block_abilities = 3
        starter_deck_abilities = (
            random.sample(change_tile_abilities, num_starter_change_tile_abilities) +
            random.sample(block_abilities, num_starter_block_abilities)
        )

        return Deck(
            abilities=starter_deck_abilities,
        )
