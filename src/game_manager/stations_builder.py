from src.enemy_manager.enemy_manager import EnemyManager
from src.fight_manager.fight_manager import FightManager
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
        return [
            # TODO: add ability chooser
            FightManager(
                deck=deck,
                enemy_manager=enemy_manager,
                blood_manager=blood_manager,
            ),
            # TODO: add next fight
            Victory(),
        ]
