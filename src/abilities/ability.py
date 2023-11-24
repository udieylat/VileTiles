from abc import abstractmethod


class Ability:

    @abstractmethod
    def play(
            self,
            ability_args: dict,
    ):
        ...

