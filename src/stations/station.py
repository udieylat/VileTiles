from __future__ import annotations

from abc import abstractmethod


class Station:

    def __init__(
            self,
            next_station: Station,
    ) -> None:
        self._next_station = next_station

    @abstractmethod
    def start(self) -> None:
        ...

    def complete(self) -> Station:
        self._next_station.start()
        return self._next_station
