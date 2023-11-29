from src.enemy_manager.enemy_manager_factory import EnemyManagerFactory
from src.fight_manager.fight_manager import FightManager
from src.game_manager.blood_manager import BloodManager
from src.game_manager.stations_builder import StationsBuilder
from src.starter_deck_generator.starter_deck_generator import StarterDeckGenerator
from src.stations.station import Station


class GameManager:

    def __init__(
            self,
            num_blood: int = 25,
    ):
        self._deck = StarterDeckGenerator.generate_starter_deck()
        self._enemy_manager = EnemyManagerFactory.generate_enemy_manager()  # TODO: should be generated per fight?
        self._blood_manager = BloodManager(
            num_blood=num_blood,
        )
        self._stations: list[Station] = StationsBuilder.build_stations(
            deck=self._deck,
            enemy_manager=self._enemy_manager,
            blood_manager=self._blood_manager,
        )
        self._stations[0].start()

    @property
    def cur_station(self) -> Station:
        return next(
            station
            for station in self._stations
            if station.is_active
        )

    def start_fight(self) -> FightManager:
        # TODO: deprecate this
        fight_manager = FightManager(
            deck=self._deck,
            enemy_manager=self._enemy_manager,
            blood_manager=self._blood_manager,
        )
        fight_manager.start_fight()
        return fight_manager
