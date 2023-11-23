from abc import abstractmethod

from src.models.tiles import Tile


class Ability:

    @abstractmethod
    def play(
            self,
            ability_args: dict,
    ):
        ...


class ChangeAbility(Ability):

    def play(
            self,
            ability_args: dict,
    ):
        enemy = ability_args["enemy"]
        tile_index = ability_args["tile_index"]
        to_color = ability_args["to_color"]
        new_tile = Tile(
            color=to_color,
        )
        enemy[tile_index] = new_tile
