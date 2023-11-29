from __future__ import annotations

from abc import abstractmethod


class Station:

    def __init__(
            self,
            next_station: Station = None,
    ):
        self._next_station = next_station
        self._is_active = False

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @property
    def is_active(self) -> bool:
        return self._is_active

    def start(self):
        self._is_active = True
        self._start()

    def complete(self) -> Station:
        self._is_active = False
        self._next_station.start()
        return self._next_station

    @abstractmethod
    def _start(self):
        ...
