import random

from src.abilities.block import Block
from src.abilities.change_box import ChangeBox
from src.abilities.change_tile import ChangeTile
from src.models.colors import ALL_COLORS, AnyColor
from src.models.deck import Deck


class StarterDeckGenerator:

    @classmethod
    def generate_starter_deck(cls) -> Deck:
        change_tile_abilities = [
            ChangeTile(
                from_color=from_color,
                to_color=AnyColor,
            )
            for from_color in ALL_COLORS
        ]
        change_tile_abilities += [
            ChangeTile(
                from_color=AnyColor,
                to_color=to_color,
            )
            for to_color in ALL_COLORS
        ]
        block_abilities = [
            Block(
                num_block=num_block,
            )
            for num_block in [3, 4, 5]
        ]
        change_box_abilities = [
            ChangeBox(
                to_color=to_color,
            )
            for to_color in ALL_COLORS
        ]

        num_starter_change_tile_abilities = 5
        num_starter_block_abilities = 3
        num_starter_change_box_abilities = 2
        starter_deck_abilities = (
            random.sample(change_tile_abilities, num_starter_change_tile_abilities) +
            random.sample(block_abilities, num_starter_block_abilities) +
            random.sample(change_box_abilities, num_starter_change_box_abilities)
        )

        return Deck(
            abilities=starter_deck_abilities,
        )
