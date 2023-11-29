from src.fight_manager.fight_manager import FightManager
from src.stations.station import Station


class StationsBuilder:

    @classmethod
    def build_stations(cls) -> list[Station]:
        return [
            FightManager(),
        ]
