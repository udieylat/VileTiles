import emoji

from src.abilities.ability import Ability, AbilityResponse


class Block(Ability):

    def __init__(
            self,
            num_block: int,
    ):
        self._num_block = num_block

    def play(
            self,
            ability_args: dict,
    ) -> AbilityResponse:
        return AbilityResponse(
            num_shields=self._num_block,
        )

    def __repr__(self) -> str:
        return (emoji.emojize(":shield:") + ' ') * self._num_block

    @classmethod
    def all_options(cls) -> list[Ability]:
        return [
            Block(
                num_block=num_block,
            )
            for num_block in [3, 4, 5]
        ]
