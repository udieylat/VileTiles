import emoji

from src.abilities.ability import Ability, AbilityResponse
from src.models.colors import Color, name_to_color, AnyColor, ALL_COLORS
from src.models.enemy import Enemy
from src.models.exceptions import InvalidPlay
from src.models.tiles import Tile


class ChangeBox(Ability):

    ALLOWED_INDICES = [0, 1, 3, 4]

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
        tile_index = ability_args["tile_index"]
        if tile_index not in self.ALLOWED_INDICES:
            raise InvalidPlay(f"Input tile_index must be in {self.ALLOWED_INDICES}")
        to_color = (
            self._to_color
            if self._to_color != AnyColor
            else name_to_color(
                name=ability_args["to_color"],
            )
        )
        for t_index in self.ALLOWED_INDICES:
            new_tile = Tile(
                color=to_color,
            )
            enemy[tile_index + t_index] = new_tile
        return AbilityResponse.empty()

    def __repr__(self) -> str:
        return f'{emoji.emojize(":package:")}{self._to_color.char}'

    @classmethod
    def all_options(cls) -> list[Ability]:
        return [
            ChangeBox(
                to_color=to_color,
            )
            for to_color in ALL_COLORS
        ]
