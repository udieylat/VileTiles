import emoji

from src.abilities.ability import Ability, AbilityResponse
from src.models.colors import Color, name_to_color, AnyColor, ALL_COLORS
from src.models.enemy import Enemy
from src.models.tiles import Tile


class ChangeLine(Ability):

    def __init__(
            self,
            to_color: Color,
    ):
        self._to_color = to_color

    def play(
            self,
            ability_args: dict,
    ) -> AbilityResponse:
        enemy: Enemy = ability_args["enemy"]
        column = ability_args.get("column")
        if column is None:
            row = ability_args["row"]
            assert row in [1, 2, 3]
            tiles_range = range((row - 1) * 3, row * 3)
        else:
            assert column in [1, 2, 3]
            tiles_range = range(column - 1, 9, 3)
        to_color = (
            self._to_color
            if self._to_color != AnyColor
            else name_to_color(
                name=ability_args["to_color"],
            )
        )
        for tile_index in tiles_range:
            new_tile = Tile(
                color=to_color,
            )
            enemy[tile_index] = new_tile
        return AbilityResponse.empty()

    def __repr__(self) -> str:
        return f'{emoji.emojize(":straight_ruler:")}{self._to_color.char}'

    @classmethod
    def all_options(cls) -> list[Ability]:
        return [
            ChangeLine(
                to_color=to_color,
            )
            for to_color in ALL_COLORS
        ]
