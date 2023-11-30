import random

from src.abilities.block import Block
from src.abilities.change_box import ChangeBox
from src.abilities.change_line import ChangeLine
from src.abilities.change_plus import ChangePlus
from src.abilities.change_tile import ChangeTile
from src.models.colors import Blue, Red, Yellow, AnyColor
from src.models.deck import Deck


class StarterDeckGenerator:

    @classmethod
    def generate_starter_deck(cls) -> Deck:
        start_deck_colors = [
            Blue,
            Red,
            Yellow,
        ]
        change_tile_abilities = [
            ChangeTile(
                from_color=from_color,
                to_color=AnyColor,
            )
            for from_color in start_deck_colors
        ]
        change_tile_abilities += [
            ChangeTile(
                from_color=AnyColor,
                to_color=to_color,
            )
            for to_color in start_deck_colors
        ]

        # num_starter_change_tile_abilities = 6
        # num_starter_block_abilities = 3
        starter_deck_abilities = (
            change_tile_abilities +
            Block.all_options() +
            random.sample(
                ChangeBox.all_options() +
                ChangeLine.all_options() +
                ChangePlus.all_options(),
                3,
            )
        )

        return Deck(
            abilities=starter_deck_abilities,
        )
