from src.enemy_manager.enemy_manager import EnemyManager
from src.stations.fight import Fight
from src.game_manager.blood_manager import BloodManager
from src.models.deck import Deck
from src.stations.station import Station
from src.stations.victory import Victory


class StationsBuilder:

    @classmethod
    def build_stations(
            cls,
            deck: Deck,
            enemy_manager: EnemyManager,
            blood_manager: BloodManager,
    ) -> list[Station]:
        stations = [
            # TODO: add ability chooser
            Fight(
                deck=deck,
                enemy_manager=enemy_manager,
                blood_manager=blood_manager,
            ),
            # TODO: add next fight
            Victory(),
        ]

        for station, next_station in zip(stations[:-1], stations[1:]):
            station.set_next_station(
                next_station=next_station,
            )

        return stations
