from __future__ import annotations

from abc import abstractmethod


class Station:

    def __init__(
            self,
            next_station: Station,
    ):
        self._next_station = next_station

    # TODO: __repr__, station number, name, description, etc

    @abstractmethod
    def start(self):
        ...

    def complete(self) -> Station:
        self._next_station.start()
        return self._next_station
