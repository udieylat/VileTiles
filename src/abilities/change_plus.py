import emoji

from src.abilities.ability import Ability, AbilityResponse
from src.models.colors import Color, name_to_color, AnyColor
from src.models.enemy import Enemy
from src.models.tiles import Tile


class ChangePlus(Ability):

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
        to_color = (
            self._to_color
            if self._to_color != AnyColor
            else name_to_color(
                name=ability_args["to_color"],
            )
        )
        for tile_index in [1, 3, 4, 5, 7]:
            new_tile = Tile(
                color=to_color,
            )
            enemy[tile_index] = new_tile
        return AbilityResponse.empty()

    def __repr__(self) -> str:
        return f'{emoji.emojize(":plus:")}{self._to_color.char}'
