import emoji

from src.abilities.ability import Ability, AbilityResponse
from src.models.colors import Color, AnyColor, name_to_color, ALL_COLORS
from src.models.enemy import Enemy
from src.models.exceptions import InvalidPlay
from src.models.tiles import Tile


class ChangeTile(Ability):

    def __init__(
            self,
            from_color: Color,
            to_color: Color,
    ):
        self._from_color = from_color
        self._to_color = to_color

    def play(
            self,
            ability_args: dict,
    ) -> AbilityResponse:
        enemy: Enemy = ability_args["enemy"]
        tile_index = ability_args["tile_index"]
        if self._from_color != AnyColor and enemy[tile_index].color != self._from_color:
            raise InvalidPlay(
                f"Enemy tile color {enemy[tile_index].color} != change tile from color {self._from_color}"
            )
        to_color = (
            self._to_color
            if self._to_color != AnyColor
            else name_to_color(
                name=ability_args["to_color"],
            )
        )
        new_tile = Tile(
            color=to_color,
        )
        enemy[tile_index] = new_tile
        return AbilityResponse.empty()

    def __repr__(self) -> str:
        return f'{self._from_color.char} {emoji.emojize(":right_arrow:")}  {self._to_color.char}'

    @classmethod
    def all_options(cls) -> list[Ability]:
        return [
            ChangeTile(
                from_color=from_color,
                to_color=to_color,
            )
            for from_color in ALL_COLORS
            for to_color in ALL_COLORS
        ]
