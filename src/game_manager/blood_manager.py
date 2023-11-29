

class BloodManager:
    def __init__(
            self,
            num_blood: int,
    ):
        self._num_blood = num_blood

    @property
    def num_blood(self) -> int:
        return self._num_blood

    def set_num_blood(
            self,
            num_blood: int,
    ):
        self._num_blood = max(num_blood, 0)

    def is_dead(self) -> bool:
        return self._num_blood == 0
