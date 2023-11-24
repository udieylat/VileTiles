from src.abilities.ability import Ability
from src.models.colors import Color
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
    ):
        enemy: Enemy = ability_args["enemy"]
        tile_index = ability_args["tile_index"]
        if enemy[tile_index].color != self._from_color:
            raise InvalidPlay("")
        new_tile = Tile(
            color=self._to_color,
        )
        enemy[tile_index] = new_tile
